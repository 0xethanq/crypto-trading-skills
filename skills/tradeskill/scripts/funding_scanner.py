#!/usr/bin/env python3
"""Zero-dependency keyless cross-exchange perpetual funding-rate & basis scanner.

Fetches public perpetual futures tickers and funding rates concurrently across
Hyperliquid, OKX, Gate, Bitget, Binance, and Bybit using Python stdlib only.
Normalizes 1h/4h/8h funding intervals to equivalent 8h rates and annualized APR,
then surfaces cross-venue carry and mark-price basis opportunities.
"""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
import json
import re
import sys
import time
import urllib.error
import urllib.request

USER_AGENT = 'TradeSkill-FundingScanner/1.0'
ALL_VENUES = ('hyperliquid', 'okx', 'gate', 'bitget', 'binance', 'bybit')
HOURS_PER_YEAR = 24.0 * 365.0


def _http_json(url: str, *, data: dict | None = None, timeout: float = 10.0) -> object:
    """Perform an unsigned GET or JSON POST request and decode the JSON body."""
    headers = {'User-Agent': USER_AGENT, 'Accept': 'application/json'}
    body = None
    if data is not None:
        headers['Content-Type'] = 'application/json'
        body = json.dumps(data).encode('utf-8')
    req = urllib.request.Request(url, data=body, headers=headers, method='POST' if body is not None else 'GET')
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode('utf-8'))


def _to_float(val: object, default: float = 0.0) -> float:
    """Safely convert numeric API fields (including empty strings/None) to float."""
    if val is None or val == '':
        return default
    try:
        return float(val)
    except (TypeError, ValueError):
        return default


def normalize_symbol(raw: str) -> str:
    """Normalize venue-specific perp symbols to canonical base tickers (e.g. BTC, ETH, 1000PEPE)."""
    sym = str(raw or '').strip()
    if not sym:
        return ''
    sym = re.sub(r'^k([A-Z0-9]{2,})$', r'1000\1', sym)
    sym = sym.upper()
    for suffix in ('-USDT-SWAP', '_USDT', '-USDT', 'USDT'):
        if sym.endswith(suffix):
            sym = sym[:-len(suffix)]
            break
    if sym == 'XBT':
        return 'BTC'
    return sym


def normalize_funding(funding_rate: float, interval_h: float) -> tuple[float, float]:
    """Convert raw per-interval funding rate into (rate_8h_pct, apr_pct)."""
    ih = interval_h if interval_h and interval_h > 0 else 8.0
    rate_8h_pct = funding_rate * (8.0 / ih) * 100.0
    apr_pct = funding_rate * (HOURS_PER_YEAR / ih) * 100.0
    return rate_8h_pct, apr_pct


def _make_leg(
    venue: str,
    contract: str,
    mark_px: float,
    funding_rate: float,
    interval_h: float,
    vol_24h_usd: float,
) -> dict | None:
    """Build one normalized perpetual market entry, or None if invalid."""
    symbol = normalize_symbol(contract)
    if not symbol or mark_px <= 0.0:
        return None
    ih = interval_h if interval_h > 0 else 8.0
    rate_8h_pct, apr_pct = normalize_funding(funding_rate, ih)
    return {
        'venue': venue,
        'symbol': symbol,
        'contract': contract,
        'mark_px': mark_px,
        'funding_rate': funding_rate,
        'interval_h': ih,
        'rate_8h_pct': rate_8h_pct,
        'apr_pct': apr_pct,
        'vol_24h_usd': max(0.0, vol_24h_usd),
    }


def fetch_hyperliquid(timeout: float = 10.0) -> list[dict]:
    """Fetch Hyperliquid perp metadata and live asset contexts (1h funding)."""
    payload = _http_json('https://api.hyperliquid.xyz/info', data={'type': 'metaAndAssetCtxs'}, timeout=timeout)
    if not isinstance(payload, list) or len(payload) < 2:
        raise ValueError('Unexpected Hyperliquid metaAndAssetCtxs payload')
    universe = payload[0].get('universe', [])
    ctxs = payload[1]
    rows: list[dict] = []
    for meta, ctx in zip(universe, ctxs):
        if meta.get('isDelisted'):
            continue
        name = str(meta.get('name') or '')
        mark_px = _to_float(ctx.get('markPx')) or _to_float(ctx.get('midPx'))
        funding = _to_float(ctx.get('funding'))
        vol_usd = _to_float(ctx.get('dayNtlVlm'))
        leg = _make_leg('hyperliquid', name, mark_px, funding, 1.0, vol_usd)
        if leg:
            rows.append(leg)
    return rows


def fetch_okx(timeout: float = 10.0) -> list[dict]:
    """Fetch OKX USDT-SWAP funding rates, mark prices, and 24h USD notional volumes."""
    funding_res = _http_json('https://www.okx.com/api/v5/public/funding-rate?instId=ANY', timeout=timeout)
    ticker_res = _http_json('https://www.okx.com/api/v5/market/tickers?instType=SWAP', timeout=timeout)
    mark_res = _http_json('https://www.okx.com/api/v5/public/mark-price?instType=SWAP', timeout=timeout)

    tickers = {
        r['instId']: r
        for r in (ticker_res.get('data') or [])
        if str(r.get('instId', '')).endswith('-USDT-SWAP')
    }
    marks = {
        r['instId']: _to_float(r.get('markPx'))
        for r in (mark_res.get('data') or [])
        if str(r.get('instId', '')).endswith('-USDT-SWAP')
    }
    rows: list[dict] = []
    for f in funding_res.get('data') or []:
        inst_id = str(f.get('instId') or '')
        if not inst_id.endswith('-USDT-SWAP'):
            continue
        t = tickers.get(inst_id, {})
        last_px = _to_float(t.get('last'))
        mark_px = marks.get(inst_id) or last_px
        vol_ccy = _to_float(t.get('volCcy24h'))
        vol_usd = vol_ccy * (last_px or mark_px)
        t_cur = _to_float(f.get('fundingTime'))
        t_next = _to_float(f.get('nextFundingTime'))
        diff_h = (t_next - t_cur) / 3_600_000.0 if (t_next > t_cur > 0) else 8.0
        interval_h = round(diff_h, 2) if 0.5 <= diff_h <= 24.0 else 8.0
        leg = _make_leg('okx', inst_id, mark_px, _to_float(f.get('fundingRate')), interval_h, vol_usd)
        if leg:
            rows.append(leg)
    return rows


def fetch_gate(timeout: float = 10.0) -> list[dict]:
    """Fetch Gate USDT perpetual contracts and 24h settle volumes."""
    contracts = _http_json('https://api.gateio.ws/api/v4/futures/usdt/contracts', timeout=timeout)
    tickers = _http_json('https://api.gateio.ws/api/v4/futures/usdt/tickers', timeout=timeout)
    tmap = {
        str(t.get('contract') or ''): t
        for t in (tickers if isinstance(tickers, list) else [])
    }
    rows: list[dict] = []
    for c in (contracts if isinstance(contracts, list) else []):
        if c.get('in_delisting'):
            continue
        name = str(c.get('name') or '')
        if not name.endswith('_USDT'):
            continue
        t = tmap.get(name, {})
        mark_px = _to_float(c.get('mark_price')) or _to_float(t.get('mark_price')) or _to_float(c.get('last_price'))
        funding = _to_float(c.get('funding_rate'))
        interval_sec = _to_float(c.get('funding_interval'), 28800.0)
        interval_h = interval_sec / 3600.0 if interval_sec > 0 else 8.0
        vol_usd = _to_float(t.get('volume_24h_settle')) or _to_float(t.get('volume_24h_quote'))
        leg = _make_leg('gate', name, mark_px, funding, interval_h, vol_usd)
        if leg:
            rows.append(leg)
    return rows


def fetch_bitget(timeout: float = 10.0) -> list[dict]:
    """Fetch Bitget USDT-FUTURES tickers and contract funding intervals."""
    tickers_res = _http_json('https://api.bitget.com/api/v2/mix/market/tickers?productType=USDT-FUTURES', timeout=timeout)
    intervals: dict[str, float] = {}
    try:
        contracts_res = _http_json('https://api.bitget.com/api/v2/mix/market/contracts?productType=USDT-FUTURES', timeout=timeout)
        for c in contracts_res.get('data') or []:
            sym = str(c.get('symbol') or '')
            ih = _to_float(c.get('fundInterval'), 8.0)
            if sym and ih > 0:
                intervals[sym] = ih
    except Exception:
        intervals = {}

    rows: list[dict] = []
    for t in tickers_res.get('data') or []:
        sym = str(t.get('symbol') or '')
        if not sym.endswith('USDT'):
            continue
        mark_px = _to_float(t.get('markPrice')) or _to_float(t.get('lastPr'))
        funding = _to_float(t.get('fundingRate'))
        vol_usd = _to_float(t.get('usdtVolume')) or _to_float(t.get('quoteVolume'))
        interval_h = intervals.get(sym, 8.0)
        leg = _make_leg('bitget', sym, mark_px, funding, interval_h, vol_usd)
        if leg:
            rows.append(leg)
    return rows


def fetch_binance(timeout: float = 10.0) -> list[dict]:
    """Fetch Binance USD-M Futures premiumIndex, 24h volume, and funding intervals."""
    premiums = _http_json('https://fapi.binance.com/fapi/v1/premiumIndex', timeout=timeout)
    tickers = _http_json('https://fapi.binance.com/fapi/v1/ticker/24hr', timeout=timeout)
    intervals: dict[str, float] = {}
    try:
        finfo = _http_json('https://fapi.binance.com/fapi/v1/fundingInfo', timeout=timeout)
        if isinstance(finfo, list):
            for fi in finfo:
                sym = str(fi.get('symbol') or '')
                ih = _to_float(fi.get('fundingIntervalHours'), 8.0)
                if sym and ih > 0:
                    intervals[sym] = ih
    except Exception:
        intervals = {}

    vol_map = {
        str(t.get('symbol') or ''): _to_float(t.get('quoteVolume'))
        for t in (tickers if isinstance(tickers, list) else [])
    }
    rows: list[dict] = []
    for p in (premiums if isinstance(premiums, list) else []):
        sym = str(p.get('symbol') or '')
        if not sym.endswith('USDT'):
            continue
        mark_px = _to_float(p.get('markPrice')) or _to_float(p.get('indexPrice'))
        funding = _to_float(p.get('lastFundingRate'))
        interval_h = intervals.get(sym, 8.0)
        vol_usd = vol_map.get(sym, 0.0)
        leg = _make_leg('binance', sym, mark_px, funding, interval_h, vol_usd)
        if leg:
            rows.append(leg)
    return rows


def fetch_bybit(timeout: float = 10.0) -> list[dict]:
    """Fetch Bybit linear USDT perpetual tickers and funding intervals."""
    res = _http_json('https://api.bybit.com/v5/market/tickers?category=linear', timeout=timeout)
    rows: list[dict] = []
    for t in (res.get('result') or {}).get('list') or []:
        sym = str(t.get('symbol') or '')
        if not sym.endswith('USDT'):
            continue
        mark_px = _to_float(t.get('markPrice')) or _to_float(t.get('lastPrice'))
        funding = _to_float(t.get('fundingRate'))
        interval_h = _to_float(t.get('fundingIntervalHour'), 8.0)
        vol_usd = _to_float(t.get('turnover24h'))
        leg = _make_leg('bybit', sym, mark_px, funding, interval_h, vol_usd)
        if leg:
            rows.append(leg)
    return rows


FETCHERS = {
    'hyperliquid': fetch_hyperliquid,
    'okx': fetch_okx,
    'gate': fetch_gate,
    'bitget': fetch_bitget,
    'binance': fetch_binance,
    'bybit': fetch_bybit,
}


def scan_venues(venues: list[str], timeout: float = 10.0) -> tuple[dict[str, dict], list[dict]]:
    """Fetch all requested venues concurrently and collect status + normalized rows."""
    status: dict[str, dict] = {}
    all_rows: list[dict] = []
    with ThreadPoolExecutor(max_workers=len(venues) or 1) as pool:
        future_map = {}
        start_times = {}
        for v in venues:
            start_times[v] = time.monotonic()
            future_map[pool.submit(FETCHERS[v], timeout)] = v
        for fut in as_completed(future_map):
            v = future_map[fut]
            elapsed_ms = int((time.monotonic() - start_times[v]) * 1000)
            try:
                rows = fut.result()
                all_rows.extend(rows)
                status[v] = {'ok': True, 'contracts': len(rows), 'latencyMs': elapsed_ms}
            except urllib.error.HTTPError as exc:
                status[v] = {'ok': False, 'error': f'HTTP {exc.code}: {exc.reason}', 'latencyMs': elapsed_ms}
            except Exception as exc:
                status[v] = {'ok': False, 'error': f'{type(exc).__name__}: {exc}', 'latencyMs': elapsed_ms}
    ordered_status = {v: status[v] for v in venues}
    return ordered_status, all_rows


def compute_opportunities(
    rows: list[dict],
    *,
    min_vol: float = 5_000_000.0,
    symbols_filter: list[str] | None = None,
    top: int = 12,
) -> tuple[list[dict], dict[str, list[dict]]]:
    """Group legs by normalized symbol and compute cross-venue carry & basis spreads."""
    by_sym: dict[str, list[dict]] = {}
    want = [normalize_symbol(s) or s.upper() for s in (symbols_filter or []) if s.strip()]
    want_set = set(want)

    for r in rows:
        sym = r['symbol']
        if want_set and sym not in want_set:
            continue
        if not want_set and r['vol_24h_usd'] < min_vol:
            continue
        by_sym.setdefault(sym, []).append(r)

    opportunities: list[dict] = []
    for sym, legs in by_sym.items():
        # Keep the highest-volume entry if one venue exposes duplicate contracts for a base ticker.
        deduped: dict[str, dict] = {}
        for leg in legs:
            prev = deduped.get(leg['venue'])
            if prev is None or leg['vol_24h_usd'] > prev['vol_24h_usd']:
                deduped[leg['venue']] = leg
        clean_legs = sorted(deduped.values(), key=lambda x: x['apr_pct'])
        by_sym[sym] = clean_legs
        if len(clean_legs) < 2:
            continue
        long_leg = clean_legs[0]
        short_leg = clean_legs[-1]
        spread_apr = short_leg['apr_pct'] - long_leg['apr_pct']
        spread_8h = short_leg['rate_8h_pct'] - long_leg['rate_8h_pct']
        basis_bps = (
            ((short_leg['mark_px'] - long_leg['mark_px']) / long_leg['mark_px']) * 10_000.0
            if long_leg['mark_px'] > 0 else 0.0
        )
        opportunities.append({
            'symbol': sym,
            'longVenue': long_leg['venue'],
            'shortVenue': short_leg['venue'],
            'longRate8hPct': round(long_leg['rate_8h_pct'], 6),
            'shortRate8hPct': round(short_leg['rate_8h_pct'], 6),
            'longAprPct': round(long_leg['apr_pct'], 2),
            'shortAprPct': round(short_leg['apr_pct'], 2),
            'spread8hPct': round(spread_8h, 6),
            'spreadAprPct': round(spread_apr, 2),
            'basisBps': round(basis_bps, 2),
            'longMarkPx': long_leg['mark_px'],
            'shortMarkPx': short_leg['mark_px'],
            'minLegVolUsd': round(min(long_leg['vol_24h_usd'], short_leg['vol_24h_usd']), 2),
            'venueCount': len(clean_legs),
        })

    opportunities.sort(key=lambda o: (o['spreadAprPct'], o['minLegVolUsd']), reverse=True)
    if not want_set and top > 0:
        opportunities = opportunities[:top]

    ordered_keys = want if want else [o['symbol'] for o in opportunities]
    matrix = {sym: by_sym[sym] for sym in ordered_keys if sym in by_sym}
    return opportunities, matrix


def _fmt_vol(usd: float) -> str:
    if usd >= 1_000_000_000:
        return f'${usd / 1_000_000_000:.2f}B'
    if usd >= 1_000_000:
        return f'${usd / 1_000_000:.1f}M'
    if usd >= 1_000:
        return f'${usd / 1_000:.0f}K'
    return f'${usd:.0f}'


def _fmt_px(px: float) -> str:
    if px >= 1000:
        return f'${px:,.2f}'
    if px >= 1:
        return f'${px:.4f}'
    return f'${px:.6f}'


def format_markdown(
    generated_at: str,
    venues_status: dict[str, dict],
    opportunities: list[dict],
    matrix: dict[str, list[dict]],
    *,
    symbols_filter: list[str] | None,
    min_vol: float,
) -> str:
    """Format scan results as clean Markdown tables."""
    lines = [
        f'# Cross-Exchange Perpetual Funding & Basis Scan ({generated_at})',
        '',
        '## Venue Feed Status',
        '| Venue | Status | Perp Contracts | Latency |',
        '|---|---|---:|---:|',
    ]
    for v, info in venues_status.items():
        if info.get('ok'):
            lines.append(f"| `{v}` | OK | {info['contracts']} | {info['latencyMs']} ms |")
        else:
            lines.append(f"| `{v}` | Unavailable ({info.get('error', 'error')}) | 0 | {info.get('latencyMs', 0)} ms |")

    lines.extend(['', '## Top Cross-Venue Funding Carry Spreads'])
    if not symbols_filter:
        lines.append(f'*Filter: 24h notional volume >= {_fmt_vol(min_vol)} per leg; funding normalized to equivalent 8h rate & APR.*')
    else:
        lines.append('*Funding normalized across 1h/4h/8h intervals to equivalent 8h rate & annualized APR.*')
    lines.append('')

    if opportunities:
        lines.extend([
            '| Symbol | Long Leg (Low Funding) | Short Leg (High Funding) | Long 8h / APR | Short 8h / APR | Spread APR | Mark Basis | Min Leg 24h Vol |',
            '|---|---|---|---:|---:|---:|---:|---:|',
        ])
        for o in opportunities:
            lines.append(
                f"| **{o['symbol']}** | `{o['longVenue']}` | `{o['shortVenue']}` | "
                f"{o['longRate8hPct']:+.4f}% ({o['longAprPct']:+.2f}%) | "
                f"{o['shortRate8hPct']:+.4f}% ({o['shortAprPct']:+.2f}%) | "
                f"**+{o['spreadAprPct']:.2f}%** | {o['basisBps']:+.1f} bps | {_fmt_vol(o['minLegVolUsd'])} |"
            )
    else:
        lines.append('_No symbols met the multi-venue filter criteria._')

    if symbols_filter and matrix:
        lines.extend(['', '## Per-Symbol Venue Matrix'])
        for sym, legs in matrix.items():
            lines.extend([
                f'### {sym}',
                '| Venue | Contract | Mark Price | Interval | Raw Funding | Equiv 8h | Ann. APR | 24h Vol |',
                '|---|---|---:|---:|---:|---:|---:|---:|',
            ])
            for leg in legs:
                lines.append(
                    f"| `{leg['venue']}` | `{leg['contract']}` | {_fmt_px(leg['mark_px'])} | "
                    f"{leg['interval_h']:g}h | {leg['funding_rate'] * 100:+.5f}% | "
                    f"{leg['rate_8h_pct']:+.4f}% | {leg['apr_pct']:+.2f}% | {_fmt_vol(leg['vol_24h_usd'])} |"
                )
            lines.append('')

    return '\n'.join(lines).rstrip() + '\n'


def run_self_test() -> None:
    """Run deterministic offline assertions covering normalization, carry math, and formatting."""
    assert normalize_symbol('BTC-USDT-SWAP') == 'BTC'
    assert normalize_symbol('ETH_USDT') == 'ETH'
    assert normalize_symbol('SOLUSDT') == 'SOL'
    assert normalize_symbol('XBTUSDT') == 'BTC'
    assert normalize_symbol('kPEPE') == '1000PEPE'
    assert normalize_symbol('1000PEPEUSDT') == '1000PEPE'

    r8_1h, apr_1h = normalize_funding(0.0000125, 1.0)
    r8_8h, apr_8h = normalize_funding(0.0001, 8.0)
    assert abs(r8_1h - 0.01) < 1e-9 and abs(apr_1h - 10.95) < 1e-9
    assert abs(r8_8h - r8_1h) < 1e-9 and abs(apr_8h - apr_1h) < 1e-9

    mock_rows = [
        _make_leg('hyperliquid', 'BTC', 60000.0, 0.00001, 1.0, 1_500_000_000.0),
        _make_leg('okx', 'BTC-USDT-SWAP', 60030.0, 0.00020, 8.0, 2_000_000_000.0),
        _make_leg('gate', 'LOWVOL_USDT', 1.0, 0.001, 8.0, 100_000.0),
        _make_leg('bitget', 'LOWVOLUSDT', 1.01, -0.001, 8.0, 200_000.0),
    ]
    clean_rows = [r for r in mock_rows if r is not None]
    opps, matrix = compute_opportunities(clean_rows, min_vol=5_000_000.0, top=10)
    assert len(opps) == 1 and opps[0]['symbol'] == 'BTC'
    assert opps[0]['longVenue'] == 'hyperliquid' and opps[0]['shortVenue'] == 'okx'
    # HL: 0.00001 * 24 * 365 * 100 = 8.76%; OKX: 0.0002 * 3 * 365 * 100 = 21.90%; spread = 13.14%
    assert abs(opps[0]['spreadAprPct'] - 13.14) < 0.01, opps[0]
    # Mark basis = (60030 - 60000) / 60000 * 10000 = +5.0 bps
    assert abs(opps[0]['basisBps'] - 5.0) < 0.01, opps[0]

    opps_sym, matrix_sym = compute_opportunities(clean_rows, symbols_filter=['BTC', 'LOWVOL'], top=10)
    assert {o['symbol'] for o in opps_sym} == {'BTC', 'LOWVOL'} and 'BTC' in matrix_sym

    md = format_markdown(
        '2026-11-27T00:00:00Z',
        {'hyperliquid': {'ok': True, 'contracts': 1, 'latencyMs': 10}, 'okx': {'ok': True, 'contracts': 1, 'latencyMs': 12}},
        opps_sym,
        matrix_sym,
        symbols_filter=['BTC'],
        min_vol=5_000_000.0,
    )
    assert 'Cross-Exchange Perpetual Funding' in md and 'BTC' in md
    payload = json.dumps({'generatedAt': '2026-11-27T00:00:00Z', 'opportunities': opps_sym, 'matrix': matrix_sym})
    assert '"spreadAprPct": 13.14' in payload
    print('funding_scanner.py self-test passed.')


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description='Keyless cross-exchange perpetual funding-rate & basis scanner.')
    parser.add_argument('--symbols', help='Comma-separated base tickers to inspect (e.g. BTC,ETH,SOL,HYPE).')
    parser.add_argument(
        '--venues',
        default=','.join(ALL_VENUES),
        help=f'Comma-separated venues ({",".join(ALL_VENUES)}).',
    )
    parser.add_argument('--top', type=int, default=12, help='Top N cross-venue opportunities in discovery mode.')
    parser.add_argument('--min-vol', type=float, default=5_000_000.0, help='Min 24h USD volume per leg (ignored with --symbols).')
    parser.add_argument('--timeout', type=float, default=10.0, help='Per-request HTTP timeout in seconds.')
    parser.add_argument('--json', action='store_true', help='Emit machine-readable JSON output.')
    parser.add_argument('--self-test', action='store_true', help='Run deterministic offline unit tests and exit.')
    args = parser.parse_args(argv)

    if args.self_test:
        run_self_test()
        return 0

    venues = [v.strip().lower() for v in args.venues.split(',') if v.strip()]
    unknown = [v for v in venues if v not in FETCHERS]
    if unknown:
        print(f'Unknown venues: {", ".join(unknown)}. Valid: {", ".join(ALL_VENUES)}', file=sys.stderr)
        return 2

    symbols_filter = [s.strip() for s in args.symbols.split(',') if s.strip()] if args.symbols else None
    generated_at = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    venues_status, rows = scan_venues(venues, timeout=args.timeout)
    opportunities, matrix = compute_opportunities(
        rows,
        min_vol=args.min_vol,
        symbols_filter=symbols_filter,
        top=args.top,
    )

    if args.json:
        print(json.dumps({
            'generatedAt': generated_at,
            'venues': venues_status,
            'opportunities': opportunities,
            'matrix': matrix,
        }, indent=2, ensure_ascii=False))
    else:
        print(format_markdown(
            generated_at,
            venues_status,
            opportunities,
            matrix,
            symbols_filter=symbols_filter,
            min_vol=args.min_vol,
        ))

    return 0 if any(v.get('ok') for v in venues_status.values()) else 1


if __name__ == '__main__':
    raise SystemExit(main())

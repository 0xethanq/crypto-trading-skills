<div align="center">

# TradeSkill | Crypto Trading AI Agent Skills

**95 ready-to-install AI Agent skills + 156 official catalog entries across 15 crypto exchanges & DEXs**

**English** · [简体中文](README.zh-CN.md) · [Official Web Directory](https://tradeskill.si/en/) · [Source & Commit Locks](SOURCES.md) · [AstraQuant 24/7 Bot](https://astraquant.top/)

[![Agent Skills](https://img.shields.io/badge/Agent_Skills-95_Bundled-10b981?style=flat-square)](catalog.json)
[![Exchanges & DEXs](https://img.shields.io/badge/Exchanges_%26_DEXs-15_Supported-3b82f6?style=flat-square)](https://tradeskill.si/en/)
[![Clients](https://img.shields.io/badge/Clients-Claude_Code_%7C_Cursor_%7C_Codex_%7C_Windsurf-111827?style=flat-square)](#quick-start)
[![Website](https://img.shields.io/badge/Website-tradeskill.si-f59e0b?style=flat-square)](https://tradeskill.si/en/)
[![AstraQuant](https://img.shields.io/badge/Sister_Engine-AstraQuant_24%2F7-00E599?style=flat-square)](https://github.com/0xethanq/astra-quant-agent)
[![License](https://img.shields.io/badge/License-MIT_%2F_Apache--2.0-6366f1?style=flat-square)](LICENSE)

</div>

---

**TradeSkill** aggregates verified official AI Agent skills for crypto CEXs and DEXs into a single reproducible repository compatible with **Claude Code**, **Cursor**, **OpenAI Codex CLI**, **Windsurf**, **OpenCode**, and **Google Antigravity**.

- **100% locked upstream commits**: Every bundled skill preserves its upstream MIT or Apache-2.0 `LICENSE`, full `SKILL.md` instructions, and `references/` docs.
- **Safety first**: Zero API keys are ever handled or stored by TradeSkill; keyless market intelligence & paper/demo modes are highlighted across supported exchanges.
- **Multi-format distribution**: Works natively with `npx skills add`, Claude Code `/plugin marketplace add`, Cursor Plugins, and SHA-256 verified shell/PowerShell installers.

---

## Quick Start

### 1. Universal Skills CLI (`npx skills`)

Works across Claude Code, Cursor, Codex CLI, Windsurf, OpenCode, and more:

```sh
# Browse & install from all 95 bundled skills
npx skills add 0xethanq/crypto-trading-skills

# Install specific skills directly
npx skills add 0xethanq/crypto-trading-skills --skill tradeskill
npx skills add 0xethanq/crypto-trading-skills --skill okx-cex-trade
npx skills add 0xethanq/crypto-trading-skills --skill kraken-market-intel
npx skills add 0xethanq/crypto-trading-skills --skill swap-planner
```

### 2. Claude Code Plugin Marketplace

Register this repo once and install exchange packs cleanly by platform:

```text
/plugin marketplace add 0xethanq/crypto-trading-skills

# Install the flagship hub router or exchange bundles
/plugin install tradeskill-hub@crypto-trading-skills
/plugin install okx-skills@crypto-trading-skills
/plugin install binance-skills@crypto-trading-skills
/plugin install kraken-skills@crypto-trading-skills
/plugin install uniswap-skills@crypto-trading-skills
```

### 3. One-Line SHA-256 Verified Installer

Supports installing any skill ID, an entire exchange (e.g. `kraken`, `okx`, `htx`), or `all`:

**macOS / Linux:**

```sh
curl -fsSL "https://tradeskill.si/install.sh" | sh -s okx-cex-market
curl -fsSL "https://tradeskill.si/install.sh" | sh -s -- --client cursor kraken
```

**Windows PowerShell:**

```powershell
powershell -NoProfile -Command "& ([scriptblock]::Create((irm 'https://tradeskill.si/install.ps1'))) okx-cex-market"
```

### 4. Prompt-Based Agent Install

Paste directly into your AI coding assistant:

> Follow `https://tradeskill.si/install/skillhub.en.md` to inspect the TradeSkill catalog and install `okx-cex-market` and `kraken-market-intel` into my active skills directory.

---

## Supported Exchanges & DEXs (15 Platforms · 156 Official Skills)

| Platform | Type | Coverage | License | Links |
|---|---|---|---|---|
| **OKX** (`okx`) | CEX | **13** bundled + 5 upstream | MIT | [Docs & CLI](https://tradeskill.si/en/exchanges/okx.html) · [GitHub](https://github.com/okx/agent-skills) |
| **Gate** (`gate`) | CEX | 20 upstream-only | No explicit redistribution license | [Docs & CLI](https://tradeskill.si/en/exchanges/gate.html) · [GitHub](https://github.com/gate/gate-skills) |
| **Binance** (`binance`) | CEX | **3** bundled + 18 upstream | MIT for CEX skills; follow upstream Web3 docs | [Docs & CLI](https://tradeskill.si/en/exchanges/binance.html) · [GitHub](https://github.com/binance/binance-skills-hub) |
| **Bybit** (`bybit`) | CEX | **1** bundled + 1 upstream | MIT (Base Trading Skill) | [Docs & CLI](https://tradeskill.si/en/exchanges/bybit.html) · [GitHub](https://github.com/bybit-exchange/skills) |
| **Bitget** (`bitget`) | CEX | **2** bundled | MIT | [Docs & CLI](https://tradeskill.si/en/exchanges/bitget.html) · [GitHub](https://github.com/Bitget-AI/agent-skill) |
| **Coinbase** (`coinbase`) | CEX | **3** bundled + 1 upstream | MIT | [Docs & CLI](https://tradeskill.si/en/exchanges/coinbase.html) · [GitHub](https://github.com/coinbase/agents) |
| **Kraken** (`kraken`) | CEX | **18** bundled | MIT | [Docs & CLI](https://tradeskill.si/en/exchanges/kraken.html) · [GitHub](https://github.com/krakenfx/kraken-cli) |
| **HTX** (`htx`) | CEX | **17** bundled | MIT | [Docs & CLI](https://tradeskill.si/en/exchanges/htx.html) · [GitHub](https://github.com/htx-exchange/htx-skills-hub) |
| **MEXC** (`mexc`) | CEX | **16** bundled | MIT | [Docs & CLI](https://tradeskill.si/en/exchanges/mexc.html) · [GitHub](https://github.com/mexcdevelop/mexc-cli) |
| **KuCoin** (`kucoin`) | CEX | **7** bundled | MIT | [Docs & CLI](https://tradeskill.si/en/exchanges/kucoin.html) · [GitHub](https://github.com/Kucoin/kucoin-skills-hub) |
| **Crypto.com** (`cryptocom`) | CEX | **2** bundled | Apache-2.0 (Exchange notes MIT) | [Docs & CLI](https://tradeskill.si/en/exchanges/cryptocom.html) · [GitHub](https://github.com/crypto-com/crypto-agent-trading) |
| **BingX** (`bingx`) | CEX | 14 upstream-only | No explicit redistribution license | [Docs & CLI](https://tradeskill.si/en/exchanges/bingx.html) · [GitHub](https://github.com/BingX-API/api-ai-skills) |
| **BitMart** (`bitmart`) | CEX | 3 upstream-only | No explicit redistribution license | [Docs & CLI](https://tradeskill.si/en/exchanges/bitmart.html) · [GitHub](https://github.com/bitmartexchange/bitmart-skills) |
| **Uniswap** (`uniswap`) | DEX | **8** bundled | MIT | [Docs & CLI](https://tradeskill.si/en/exchanges/uniswap.html) · [GitHub](https://github.com/Uniswap/uniswap-ai) |
| **Jupiter** (`jupiter`) | DEX | **4** bundled | MIT | [Docs & CLI](https://tradeskill.si/en/exchanges/jupiter.html) · [GitHub](https://github.com/jup-ag/agent-skills) |

---

## Bundled Skills Directory (95 Skills)

Expand any exchange below to browse every bundled `SKILL.md` directly on GitHub or jump to interactive prompts and CLI docs on [tradeskill.si](https://tradeskill.si/en/):

- [`tradeskill`](skills/tradeskill/SKILL.md) — Discover, verify, and install 156 official crypto trading AI skills across 15 exchanges and DEXs (OKX, Gate, Binance, Bybit, Bitget, Coinbase, Kraken, HTX, MEXC, KuCoin, Crypto.com, BingX, BitMart, Uniswap, Jupiter) from TradeSkill (tradeskill.si) or GitHub. ([TradeSkill En](https://tradeskill.si/en/))
<details>
<summary><strong>OKX (<code>okx</code>) — 13 bundled skills · Claude pack: <code>okx-skills</code></strong></summary>

| Skill (`SKILL.md` & `npx --skill`) | Version | Description | Docs |
|---|---|---|---|
| [`okx-cex-trade`](skills/okx-cex-trade/SKILL.md) *(order tag)* | `1.5.1` | Order management across spot, perpetual, futures, options, and event contracts. | [TradeSkill](https://tradeskill.si/en/skills/okx-cex-trade.html) |
| [`okx-cex-bot`](skills/okx-cex-bot/SKILL.md) *(order tag)* | `1.5.1` | Create and manage grid, DCA, smart portfolio, and recurring buy strategies. | [TradeSkill](https://tradeskill.si/en/skills/okx-cex-bot.html) |
| [`okx-cex-market`](skills/okx-cex-market/SKILL.md) | `1.5.1` | Query prices, orderbooks, K-lines, funding rates, and technical indicators without API keys. | [TradeSkill](https://tradeskill.si/en/skills/okx-cex-market.html) |
| [`okx-cex-portfolio`](skills/okx-cex-portfolio/SKILL.md) | `1.5.1` | Inspect balances, positions, PnL, fee tiers, and perform account fund transfers. | [TradeSkill](https://tradeskill.si/en/skills/okx-cex-portfolio.html) |
| [`okx-cex-smartmoney`](skills/okx-cex-smartmoney/SKILL.md) | `1.5.1` | Track top trader leaderboards, historical fills, open positions, and aggregated signals. | [TradeSkill](https://tradeskill.si/en/skills/okx-cex-smartmoney.html) |
| [`okx-sentiment-tracker`](skills/okx-sentiment-tracker/SKILL.md) | `1.5.1` | Fetch crypto news, trending assets, market sentiment, and macro economic calendars. | [TradeSkill](https://tradeskill.si/en/skills/okx-sentiment-tracker.html) |
| [`okx-cex-auth`](skills/okx-cex-auth/SKILL.md) | `1.5.1` | Configure official CLI login profiles and local API credentials safely on your device. | [TradeSkill](https://tradeskill.si/en/skills/okx-cex-auth.html) |
| [`okx-cex-skill-mp`](skills/okx-cex-skill-mp/SKILL.md) | `1.5.1` | Search, install, update skills and verify official marketplace signatures via CLI. | [TradeSkill](https://tradeskill.si/en/skills/okx-cex-skill-mp.html) |
| [`okx-cex-earn`](skills/okx-cex-earn/SKILL.md) | `1.5.1` | Query and manage Simple Earn, Flash Earn, and on-chain yield products. | [TradeSkill](https://tradeskill.si/en/skills/okx-cex-earn.html) |
| [`earn-hunter`](skills/earn-hunter/SKILL.md) | `1.5.1` | Monitor Flash Earn, fixed, and flexible yield openings with optional scheduled alerts. | [TradeSkill](https://tradeskill.si/en/skills/earn-hunter.html) |
| [`okx-defi`](skills/okx-defi/SKILL.md) | `4.6.12` | Discover and manage multi-chain staking, lending, LP pools, and APY/TVL analytics via OKX OnchainOS. | [TradeSkill](https://tradeskill.si/en/skills/okx-defi.html) |
| [`okx-dapp-discovery`](skills/okx-dapp-discovery/SKILL.md) | `latest` | Search and route multi-chain DApps (Aave, Hyperliquid, Polymarket, pump.fun) without signing. | [TradeSkill](https://tradeskill.si/en/skills/okx-dapp-discovery.html) |
| [`okx-mcp-services`](skills/okx-mcp-services/SKILL.md) | `4.6.12` | Query NewsLiquid / 6551 MCP feeds and X crypto intelligence via wallet credentials. | [TradeSkill](https://tradeskill.si/en/skills/okx-mcp-services.html) |

</details>

<details>
<summary><strong>Binance (<code>binance</code>) — 3 bundled skills · Claude pack: <code>binance-skills</code></strong></summary>

| Skill (`SKILL.md` & `npx --skill`) | Version | Description | Docs |
|---|---|---|---|
| [`binance`](skills/binance/SKILL.md) | `2.1.0` | Spot, USD-M futures, and Convert via binance-cli (excludes Binance Wallet / Binance.US). | [TradeSkill](https://tradeskill.si/en/skills/binance.html) |
| [`binance-p2p`](skills/binance-p2p/SKILL.md) (`--skill p2p`) | `1.1.0` | Query P2P buy/sell offers, payment methods, order history, appeals, and merchant ads. | [TradeSkill](https://tradeskill.si/en/skills/binance-p2p.html) |
| [`binance-onchain-pay`](skills/binance-onchain-pay/SKILL.md) (`--skill onchain-pay-open-api`) | `0.1.2` | Real-time fiat quotes, payment channels, and direct withdrawal orders to on-chain wallets. | [TradeSkill](https://tradeskill.si/en/skills/binance-onchain-pay.html) |

</details>

<details>
<summary><strong>Bybit (<code>bybit</code>) — 1 bundled skill · Claude pack: <code>bybit-skills</code></strong></summary>

| Skill (`SKILL.md` & `npx --skill`) | Version | Description | Docs |
|---|---|---|---|
| [`bybit-trading`](skills/bybit-trading/SKILL.md) | `1.7.13` | Bybit V5 market data, spot, derivatives, strategies, and account ops with modular specs. | [TradeSkill](https://tradeskill.si/en/skills/bybit-trading.html) |

</details>

<details>
<summary><strong>Bitget (<code>bitget</code>) — 2 bundled skills · Claude pack: <code>bitget-skills</code></strong></summary>

| Skill (`SKILL.md` & `npx --skill`) | Version | Description | Docs |
|---|---|---|---|
| [`bitget`](skills/bitget/SKILL.md) | `3.0.0` | Operate Bitget Unified Trading Account via bgc CLI across quotes, spot, futures, and demo. | [TradeSkill](https://tradeskill.si/en/skills/bitget-agent-skill.html) |
| [`bitget-wallet`](skills/bitget-wallet/SKILL.md) | `2026.10.29-2` | Multi-chain ETH/SOL/BSC/Base quotes, Swap routing, token security checks, K-lines, and RWA stocks. | [TradeSkill](https://tradeskill.si/en/skills/bitget-wallet.html) |

</details>

<details>
<summary><strong>Coinbase (<code>coinbase</code>) — 3 bundled skills · Claude pack: <code>coinbase-skills</code></strong></summary>

| Skill (`SKILL.md` & `npx --skill`) | Version | Description | Docs |
|---|---|---|---|
| [`coinbase-cli`](skills/coinbase-cli/SKILL.md) | `latest` | Run local portfolio queries, market data, spot trades, convert, and perps checks via @coinbase/coinbase-cli. | [TradeSkill](https://tradeskill.si/en/skills/coinbase-cli.html) |
| [`coinbase-mcp`](skills/coinbase-mcp/SKILL.md) | `latest` | Connect natively via OAuth to Coinbase Hosted MCP for remote trading, portfolio, and paid research tools. | [TradeSkill](https://tradeskill.si/en/skills/coinbase-mcp.html) |
| [`coinbase-wallet-mcp`](skills/coinbase-wallet-mcp/SKILL.md) (`--skill wallet-mcp`) | `0.1.0` | Link AI assistants to Coinbase Wallet Account for balances, transfers, on-chain swaps, signing & x402. | [TradeSkill](https://tradeskill.si/en/skills/coinbase-wallet-mcp.html) |

</details>

<details>
<summary><strong>Kraken (<code>kraken</code>) — 18 bundled skills · Claude pack: <code>kraken-skills</code></strong></summary>

| Skill (`SKILL.md` & `npx --skill`) | Version | Description | Docs |
|---|---|---|---|
| [`kraken-setup`](skills/kraken-setup/SKILL.md) | `1.1.0` | Install single-binary kraken / kraken-mcp in minutes and initialize zero-auth Paper Trading workspaces. | [TradeSkill](https://tradeskill.si/en/skills/kraken-setup.html) |
| [`kraken-market-intel`](skills/kraken-market-intel/SKILL.md) | `1.0.0` | Fetch low-noise Kraken spot & futures tickers, OHLC candles, orderbook depth, and recent trades with no key. | [TradeSkill](https://tradeskill.si/en/skills/kraken-market-intel.html) |
| [`kraken-spot-execution`](skills/kraken-spot-execution/SKILL.md) | `1.0.0` | Verified Kraken spot execution workflow featuring pre-flight checks, confirmation gates, and fill audit. | [TradeSkill](https://tradeskill.si/en/skills/kraken-spot-execution.html) |
| [`kraken-futures-trading`](skills/kraken-futures-trading/SKILL.md) | `1.0.0` | Manage Kraken Futures open/close positions, margin, leverage settings, and full order lifecycles. | [TradeSkill](https://tradeskill.si/en/skills/kraken-futures-trading.html) |
| [`kraken-portfolio-intel`](skills/kraken-portfolio-intel/SKILL.md) | `1.0.0` | Aggregate Kraken account equity, trade attribution, realized/unrealized PnL, and report exports. | [TradeSkill](https://tradeskill.si/en/skills/kraken-portfolio-intel.html) |
| [`kraken-order-types`](skills/kraken-order-types/SKILL.md) | `1.0.0` | Master Kraken spot & futures market, limit, Post-Only, Iceberg, and Time-in-Force flags. | [TradeSkill](https://tradeskill.si/en/skills/kraken-order-types.html) |
| [`kraken-stop-take-profit`](skills/kraken-stop-take-profit/SKILL.md) | `1.0.0` | Attach stop-loss triggers, take-profit limits, and trailing exits to bound Kraken position risk. | [TradeSkill](https://tradeskill.si/en/skills/kraken-stop-take-profit.html) |
| [`kraken-twap-execution`](skills/kraken-twap-execution/SKILL.md) | `1.0.0` | Split large orders over fixed time intervals to minimize market impact and slippage on Kraken. | [TradeSkill](https://tradeskill.si/en/skills/kraken-twap-execution.html) |
| [`kraken-grid-trading`](skills/kraken-grid-trading/SKILL.md) | `1.0.0` | Deploy arithmetic or geometric buy/sell grids across defined ranges to capture range volatility. | [TradeSkill](https://tradeskill.si/en/skills/kraken-grid-trading.html) |
| [`kraken-dca-strategy`](skills/kraken-dca-strategy/SKILL.md) | `1.0.0` | Execute scheduled fixed-amount buys, track cost basis, and monitor cumulative DCA ROI on Kraken. | [TradeSkill](https://tradeskill.si/en/skills/kraken-dca-strategy.html) |
| [`kraken-basis-trading`](skills/kraken-basis-trading/SKILL.md) | `1.0.0` | Monitor spot-futures spreads and construct Delta-neutral long spot + short futures yield positions. | [TradeSkill](https://tradeskill.si/en/skills/kraken-basis-trading.html) |
| [`kraken-funding-carry`](skills/kraken-funding-carry/SKILL.md) | `1.0.0` | Scan elevated perpetual funding rates and hedge directional exposure while collecting carry yield. | [TradeSkill](https://tradeskill.si/en/skills/kraken-funding-carry.html) |
| [`kraken-earn-staking`](skills/kraken-earn-staking/SKILL.md) | `1.0.0` | Compare on-chain Staking and Earn APYs on Kraken, manage allocations, and audit payout history. | [TradeSkill](https://tradeskill.si/en/skills/kraken-earn-staking.html) |
| [`kraken-rebalancing`](skills/kraken-rebalancing/SKILL.md) | `1.0.0` | Detect weight drift across multi-asset Kraken holdings and compute cost-capped rebalance orders. | [TradeSkill](https://tradeskill.si/en/skills/kraken-rebalancing.html) |
| [`kraken-liquidation-guard`](skills/kraken-liquidation-guard/SKILL.md) | `1.0.0` | Monitor futures margin ratios and distance-to-liquidation to trigger timely de-risking alerts. | [TradeSkill](https://tradeskill.si/en/skills/kraken-liquidation-guard.html) |
| [`kraken-paper-strategy`](skills/kraken-paper-strategy/SKILL.md) | `1.0.0` | Run simulated strategies and replays locally on live Kraken market feeds with zero funds or keys. | [TradeSkill](https://tradeskill.si/en/skills/kraken-paper-strategy.html) |
| [`kraken-mcp-integration`](skills/kraken-mcp-integration/SKILL.md) | `1.1.0` | Wire kraken-mcp directly into Claude Code, Cursor, and Codex without shell wrapper overhead. | [TradeSkill](https://tradeskill.si/en/skills/kraken-mcp-integration.html) |
| [`kraken-ws-streaming`](skills/kraken-ws-streaming/SKILL.md) | `1.0.0` | Subscribe to Kraken spot & futures WebSocket trades, L2 orderbooks, candles, and private updates. | [TradeSkill](https://tradeskill.si/en/skills/kraken-ws-streaming.html) |

</details>

<details>
<summary><strong>HTX (<code>htx</code>) — 17 bundled skills · Claude pack: <code>htx-skills</code></strong></summary>

| Skill (`SKILL.md` & `npx --skill`) | Version | Description | Docs |
|---|---|---|---|
| [`htx-spot-market`](skills/htx-spot-market/SKILL.md) (`--skill htx/spot-market`) | `2.0.0` | Query HTX spot tickers, K-lines, orderbooks, trades, and symbol rules via htx-cli without keys. | [TradeSkill](https://tradeskill.si/en/skills/htx-spot-market.html) |
| [`htx-spot-trading`](skills/htx-spot-trading/SKILL.md) (`--skill htx/spot-trading`) | `2.0.0` | Execute limit/market spot orders, cancels, edits, order lookups & margin borrows with confirmation. | [TradeSkill](https://tradeskill.si/en/skills/htx-spot-trading.html) |
| [`htx-spot-account`](skills/htx-spot-account/SKILL.md) (`--skill htx/spot-account`) | `2.0.0` | Inspect HTX spot balances, valuation, ledger history, and transfer assets between spot & futures. | [TradeSkill](https://tradeskill.si/en/skills/htx-spot-account.html) |
| [`htx-futures-market`](skills/htx-futures-market/SKILL.md) (`--skill htx/futures-market`) | `2.0.0` | Query HTX USDT-M perpetual contracts, index prices, K-lines, BBO & orderbook depth with no keys. | [TradeSkill](https://tradeskill.si/en/skills/htx-futures-market.html) |
| [`htx-futures-trading`](skills/htx-futures-trading/SKILL.md) (`--skill htx/futures-trading`) | `2.0.0` | Manage HTX perpetual opens, closes, TP/SL, trigger orders, edits & cancels with write guardrails. | [TradeSkill](https://tradeskill.si/en/skills/htx-futures-trading.html) |
| [`htx-futures-account`](skills/htx-futures-account/SKILL.md) (`--skill htx/futures-account`) | `2.0.0` | Inspect HTX futures equity, open positions, leverage tiers, margin factors & account mode. | [TradeSkill](https://tradeskill.si/en/skills/htx-futures-account.html) |
| [`htx-funding-rate`](skills/htx-funding-rate/SKILL.md) (`--skill htx/funding-rate`) | `2.0.0` | Batch-scan current, historical & estimated funding rates across all HTX USDT-M perpetuals. | [TradeSkill](https://tradeskill.si/en/skills/htx-funding-rate.html) |
| [`htx-market-overview`](skills/htx-market-overview/SKILL.md) | `1.0.0` | Scan top gainers/losers, volume spikes, breadth, and sector rotations across HTX spot & futures. | [TradeSkill](https://tradeskill.si/en/skills/htx-market-overview.html) |
| [`htx-oi-tracker`](skills/htx-oi-tracker/SKILL.md) | `1.0.0` | Monitor HTX USDT-M open interest snapshots and sudden OI build-ups across perpetual pairs. | [TradeSkill](https://tradeskill.si/en/skills/htx-oi-tracker.html) |
| [`htx-liquidation-stream`](skills/htx-liquidation-stream/SKILL.md) | `1.0.0` | Query recent HTX perpetual forced liquidations to spot long/short squeezes and liquidity zones. | [TradeSkill](https://tradeskill.si/en/skills/htx-liquidation-stream.html) |
| [`htx-elite-positioning`](skills/htx-elite-positioning/SKILL.md) | `1.0.0` | Track HTX top trader long/short positioning by account count and position size. | [TradeSkill](https://tradeskill.si/en/skills/htx-elite-positioning.html) |
| [`htx-mark-price`](skills/htx-mark-price/SKILL.md) | `1.0.0` | Fetch HTX perpetual mark prices, premium index & basis K-lines for risk & arbitrage pricing. | [TradeSkill](https://tradeskill.si/en/skills/htx-mark-price.html) |
| [`htx-settlement`](skills/htx-settlement/SKILL.md) | `1.0.0` | Inspect HTX estimated delivery prices, settlement history, and insurance fund balance trends. | [TradeSkill](https://tradeskill.si/en/skills/htx-settlement.html) |
| [`htx-derivatives-analyst`](skills/htx-derivatives-analyst/SKILL.md) | `1.0.0` | Synthesize funding, OI, elite ratios, liquidations & basis into crowding and squeeze diagnoses. | [TradeSkill](https://tradeskill.si/en/skills/htx-derivatives-analyst.html) |
| [`htx-sentiment-analyst`](skills/htx-sentiment-analyst/SKILL.md) | `1.0.0` | Combine Fear & Greed index, whale positioning & market breadth into quantified sentiment reports. | [TradeSkill](https://tradeskill.si/en/skills/htx-sentiment-analyst.html) |
| [`htx-technical-analysis`](skills/htx-technical-analysis/SKILL.md) (`--skill htx/technical-analysis`) | `3.0.0` | Compute 51 technical indicators, 12 candle patterns, 5 BTC cycle metrics & divergence alerts locally. | [TradeSkill](https://tradeskill.si/en/skills/htx-technical-analysis.html) |
| [`htx-ta-master`](skills/htx-ta-master/SKILL.md) (`--skill htx/ta-master`) | `1.0.0` | Compute a 0–100 score weighted 50% price/volume + 30% derivatives + 20% cycle with strategy notes. | [TradeSkill](https://tradeskill.si/en/skills/htx-ta-master.html) |

</details>

<details>
<summary><strong>MEXC (<code>mexc</code>) — 16 bundled skills · Claude pack: <code>mexc-skills</code></strong></summary>

| Skill (`SKILL.md` & `npx --skill`) | Version | Description | Docs |
|---|---|---|---|
| [`mexc-setup`](skills/mexc-setup/SKILL.md) | `latest` | Install or upgrade @mexc-ai/cli, run diagnostics, configure key profiles & register MCP. | [TradeSkill](https://tradeskill.si/en/skills/mexc-setup.html) |
| [`mexc-auth`](skills/mexc-auth/SKILL.md) | `latest` | Guide to configuring and repairing signed MEXC OpenAPI credentials and local CLI profiles. | [TradeSkill](https://tradeskill.si/en/skills/mexc-auth.html) |
| [`mexc-spot-market`](skills/mexc-spot-market/SKILL.md) (`--skill mexc-spot-marketv2`) | `latest` | Fetch full MEXC symbol lists, real-time spot tickers, new listings & risk tags without keys. | [TradeSkill](https://tradeskill.si/en/skills/mexc-spot-market.html) |
| [`mexc-spot-kline`](skills/mexc-spot-kline/SKILL.md) | `latest` | Fetch multi-timeframe MEXC spot OHLCV candles and earliest lookback boundaries with no API key. | [TradeSkill](https://tradeskill.si/en/skills/mexc-spot-kline.html) |
| [`mexc-spot-trade`](skills/mexc-spot-trade/SKILL.md) | `latest` | Place limit/market spot orders with TP/SL, cancel, run dry-run simulations & inspect fills. | [TradeSkill](https://tradeskill.si/en/skills/mexc-spot-trade.html) |
| [`mexc-spot-account`](skills/mexc-spot-account/SKILL.md) | `latest` | Subscribe to private MEXC WebSocket feeds for live order fills and spot balance updates. | [TradeSkill](https://tradeskill.si/en/skills/mexc-spot-account.html) |
| [`mexc-spot-asset`](skills/mexc-spot-asset/SKILL.md) | `latest` | Aggregate balances across MEXC spot, contract, OTC, and strategy accounts in one overview. | [TradeSkill](https://tradeskill.si/en/skills/mexc-spot-asset.html) |
| [`mexc-spot-convert`](skills/mexc-spot-convert/SKILL.md) | `latest` | Query eligible tokens and convert between spot assets instantly at locked zero-slippage quotes. | [TradeSkill](https://tradeskill.si/en/skills/mexc-spot-convert.html) |
| [`mexc-spot-grid`](skills/mexc-spot-grid/SKILL.md) | `latest` | Fetch AI-recommended grid parameters plus create, monitor, and stop automated spot range bots. | [TradeSkill](https://tradeskill.si/en/skills/mexc-spot-grid.html) |
| [`mexc-spot-dca`](skills/mexc-spot-dca/SKILL.md) | `latest` | Check supported DCA pairs, historical ROI, and manage recurring spot auto-invest plans. | [TradeSkill](https://tradeskill.si/en/skills/mexc-spot-dca.html) |
| [`mexc-contract-market`](skills/mexc-contract-market/SKILL.md) | `latest` | Query MEXC contract specs, fair/index prices, funding rates, depth & 24h stats without keys. | [TradeSkill](https://tradeskill.si/en/skills/mexc-contract-market.html) |
| [`mexc-contract-trade`](skills/mexc-contract-trade/SKILL.md) | `latest` | Place MEXC limit/market futures orders, trigger plans, SL/TP & batch edits/cancellations. | [TradeSkill](https://tradeskill.si/en/skills/mexc-contract-trade.html) |
| [`mexc-contract-account`](skills/mexc-contract-account/SKILL.md) | `latest` | Inspect MEXC futures equity, position margin risk, transfer records, and trade summaries. | [TradeSkill](https://tradeskill.si/en/skills/mexc-contract-account.html) |
| [`mexc-earn-flexible`](skills/mexc-earn-flexible/SKILL.md) (`--skill mexc-financial-openapi-flexible`) | `latest` | Toggle auto-stake settings, inspect interest rewards & check flexible savings on MEXC. | [TradeSkill](https://tradeskill.si/en/skills/mexc-earn-flexible.html) |
| [`mexc-earn-fixed`](skills/mexc-earn-fixed/SKILL.md) (`--skill mexc-financial-openapi-fixed`) | `latest` | Browse locked-term yields, lock durations, subscription orders & reward payouts on MEXC. | [TradeSkill](https://tradeskill.si/en/skills/mexc-earn-fixed.html) |
| [`mexc-ws`](skills/mexc-ws/SKILL.md) | `latest` | Line caps, JSON Lines streaming output, and dry-run conventions for all MEXC CLI WebSocket feeds. | [TradeSkill](https://tradeskill.si/en/skills/mexc-ws.html) |

</details>

<details>
<summary><strong>KuCoin (<code>kucoin</code>) — 7 bundled skills · Claude pack: <code>kucoin-skills</code></strong></summary>

| Skill (`SKILL.md` & `npx --skill`) | Version | Description | Docs |
|---|---|---|---|
| [`kucoin-spot`](skills/kucoin-spot/SKILL.md) (`--skill spot`) | `1.0.0` | Inspect KuCoin spot tickers, HF orders, stop orders & OCO history (read-only GET only). | [TradeSkill](https://tradeskill.si/en/skills/kucoin-spot.html) |
| [`kucoin-futures-trading`](skills/kucoin-futures-trading/SKILL.md) (`--skill futures-trading`) | `1.0.0` | Query KuCoin Futures contracts, position risk, active orders & funding history (read-only GET). | [TradeSkill](https://tradeskill.si/en/skills/kucoin-futures-trading.html) |
| [`kucoin-margin-trading`](skills/kucoin-margin-trading/SKILL.md) (`--skill margin-trading`) | `1.0.0` | Inspect KuCoin cross/isolated margin rates, borrow/repay ledgers, and risk limits (read-only GET). | [TradeSkill](https://tradeskill.si/en/skills/kucoin-margin-trading.html) |
| [`kucoin-assets`](skills/kucoin-assets/SKILL.md) (`--skill assets`) | `1.0.0` | Aggregate KuCoin balances, ledgers, deposits/withdrawals, sub-accounts & VIP fee levels. | [TradeSkill](https://tradeskill.si/en/skills/kucoin-assets.html) |
| [`kucoin-convert`](skills/kucoin-convert/SKILL.md) (`--skill convert`) | `1.0.0` | Fetch instant KuCoin Convert rate estimates and inspect past swap orders and statuses. | [TradeSkill](https://tradeskill.si/en/skills/kucoin-convert.html) |
| [`kucoin-earn`](skills/kucoin-earn/SKILL.md) (`--skill earn`) | `1.0.0` | Browse KuCoin Simple Earn flexible/staking & structured yields alongside subscription records. | [TradeSkill](https://tradeskill.si/en/skills/kucoin-earn.html) |
| [`kucoin-broker`](skills/kucoin-broker/SKILL.md) (`--skill broker`) | `1.0.0` | Query KuCoin Broker referrals, rebate breakdowns, Broker Pro clients & stats (read-only GET). | [TradeSkill](https://tradeskill.si/en/skills/kucoin-broker.html) |

</details>

<details>
<summary><strong>Crypto.com (<code>cryptocom</code>) — 2 bundled skills · Claude pack: <code>cryptocom-skills</code></strong></summary>

| Skill (`SKILL.md` & `npx --skill`) | Version | Description | Docs |
|---|---|---|---|
| [`cryptocom-exchange`](skills/cryptocom-exchange/SKILL.md) (`--skill crypto-com-exchange`) | `2.0.0` | Operate Crypto.com Exchange via @cryptocom/cdcx-cli: spot/perps/OCO, paper sandbox & 4-tier guards. | [TradeSkill](https://tradeskill.si/en/skills/cryptocom-exchange.html) |
| [`cryptocom-app`](skills/cryptocom-app/SKILL.md) (`--skill crypto-com-app`) | `1.0.2` | Run market buys/sells, token swaps, bank/card fiat rails, and weekly limits via App API. | [TradeSkill](https://tradeskill.si/en/skills/cryptocom-app.html) |

</details>

<details>
<summary><strong>Uniswap (<code>uniswap</code>) — 8 bundled skills · Claude pack: <code>uniswap-skills</code></strong></summary>

| Skill (`SKILL.md` & `npx --skill`) | Version | Description | Docs |
|---|---|---|---|
| [`uniswap-swap-planner`](skills/uniswap-swap-planner/SKILL.md) (`--skill swap-planner`) | `latest` | Discover tokens, compare routes, set slippage guards, and build safe EVM swaps across Uniswap chains. | [TradeSkill](https://tradeskill.si/en/skills/uniswap-swap-planner.html) |
| [`uniswap-liquidity-planner`](skills/uniswap-liquidity-planner/SKILL.md) (`--skill liquidity-planner`) | `0.2.0` | Analyze fee tiers, concentrated price ticks, and impermanent loss before deploying v3/v4 LP positions. | [TradeSkill](https://tradeskill.si/en/skills/uniswap-liquidity-planner.html) |
| [`uniswap-swap-integration`](skills/uniswap-swap-integration/SKILL.md) (`--skill swap-integration`) | `1.6.0` | Official guide to integrating Uniswap Trading API and Universal Router into apps and bots. | [TradeSkill](https://tradeskill.si/en/skills/uniswap-swap-integration.html) |
| [`uniswap-dca-bot`](skills/uniswap-dca-bot/SKILL.md) (`--skill dca-bot`) | `0.2.0` | Automate recurring time-based or dip-triggered token accumulation directly on-chain via Uniswap. | [TradeSkill](https://tradeskill.si/en/skills/uniswap-dca-bot.html) |
| [`uniswap-index-bot`](skills/uniswap-index-bot/SKILL.md) (`--skill index-bot`) | `0.2.0` | Acquire multi-token baskets at target weights and automate periodic on-chain rebalancing. | [TradeSkill](https://tradeskill.si/en/skills/uniswap-index-bot.html) |
| [`uniswap-copy-trade`](skills/uniswap-copy-trade/SKILL.md) (`--skill copy-trade`) | `0.2.0` | Track target EVM Smart Money addresses on DEX and mirror swaps proportionally on-chain. | [TradeSkill](https://tradeskill.si/en/skills/uniswap-copy-trade.html) |
| [`uniswap-v4-hook-generator`](skills/uniswap-v4-hook-generator/SKILL.md) (`--skill v4-hook-generator`) | `1.0.0` | Generate OpenZeppelin-aligned v4 Hooks for dynamic fees, limit orders, MEV guards & custom curves. | [TradeSkill](https://tradeskill.si/en/skills/uniswap-v4-hook-generator.html) |
| [`uniswap-v4-security-foundations`](skills/uniswap-v4-security-foundations/SKILL.md) (`--skill v4-security-foundations`) | `1.1.0` | Audit PoolManager callback permissions, reentrancy, and slippage vectors in custom v4 Hooks. | [TradeSkill](https://tradeskill.si/en/skills/uniswap-v4-security-foundations.html) |

</details>

<details>
<summary><strong>Jupiter (<code>jupiter</code>) — 4 bundled skills · Claude pack: <code>jupiter-skills</code></strong></summary>

| Skill (`SKILL.md` & `npx --skill`) | Version | Description | Docs |
|---|---|---|---|
| [`jupiter-integrate`](skills/jupiter-integrate/SKILL.md) (`--skill integrating-jupiter`) | `1.2.0` | Integrate Jupiter Swap v2, Perps, Trigger/Limit orders, DCA, Lend, and Price APIs on Solana. | [TradeSkill](https://tradeskill.si/en/skills/jupiter-integrate.html) |
| [`jupiter-lend`](skills/jupiter-lend/SKILL.md) | `0.1.3` | Inspect Jupiter Lend pools, jlTokens yields, and execute vault supply/borrow via official SDKs. | [TradeSkill](https://tradeskill.si/en/skills/jupiter-lend.html) |
| [`jupiter-swap-migration`](skills/jupiter-swap-migration/SKILL.md) | `1.1.0` | Migrate legacy Metis v1 or Ultra swap flows to unified Jupiter Swap v2 routes and builders. | [TradeSkill](https://tradeskill.si/en/skills/jupiter-swap-migration.html) |
| [`jupiter-vrfd`](skills/jupiter-vrfd/SKILL.md) | `1.0.1` | Route Solana token submissions for Jupiter VRFD verification, eligibility checks & metadata updates. | [TradeSkill](https://tradeskill.si/en/skills/jupiter-vrfd.html) |

</details>


### Official Upstream-Only Skills (62 Skills)

For platforms whose upstream repositories do not permit third-party ZIP redistribution or rely on dynamic CLI skill generation, TradeSkill indexes verified metadata and links straight to official upstream instructions:

- **OKX** (5 skills): Install via OKX OnchainOS / Trade CLI — [TradeSkill OKX Hub](https://tradeskill.si/en/exchanges/okx.html) · [Upstream Repo](https://github.com/okx/agent-skills)
- **Gate** (20 skills): Install via Gate CLI / MCP generator — [TradeSkill Gate Hub](https://tradeskill.si/en/exchanges/gate.html) · [Upstream Repo](https://github.com/gate/gate-skills)
- **Binance** (18 skills): Install from binance/binance-skills-hub — [TradeSkill Binance Hub](https://tradeskill.si/en/exchanges/binance.html) · [Upstream Repo](https://github.com/binance/binance-skills-hub)
- **Bybit** (1 skill): Install from bybit-exchange/trading-cli — [TradeSkill Bybit Hub](https://tradeskill.si/en/exchanges/bybit.html) · [Upstream Repo](https://github.com/bybit-exchange/skills)
- **Coinbase** (1 skill): Route skill in coinbase/agents — [TradeSkill Coinbase Hub](https://tradeskill.si/en/exchanges/coinbase.html) · [Upstream Repo](https://github.com/coinbase/agents)
- **BingX** (14 skills): Clone from BingX-API/api-ai-skills — [TradeSkill BingX Hub](https://tradeskill.si/en/exchanges/bingx.html) · [Upstream Repo](https://github.com/BingX-API/api-ai-skills)
- **BitMart** (3 skills): Clone from bitmartexchange/bitmart-skills — [TradeSkill BitMart Hub](https://tradeskill.si/en/exchanges/bitmart.html) · [Upstream Repo](https://github.com/bitmartexchange/bitmart-skills)

---

## Tutorials & Exchange Comparisons

Read full bilingual engineering guides, keyless market workflows, and exchange comparisons on [tradeskill.si/en/guides.html](https://tradeskill.si/en/guides.html):

- [OKX vs Binance vs Gate AI Trading Skills Compared (2026)](https://tradeskill.si/en/guides/okx-vs-binance-vs-gate-ai-skills.html) — Compare OKX (18 skills), Binance (21 skills), and Gate (20 skills) official AI agent suites, CLI runtimes, keyless data coverage, and 20% fee rebates.
- [Claude Code Crypto Trading Tutorial (~/.claude/skills)](https://tradeskill.si/en/guides/claude-code-crypto-trading-tutorial.html) — Install verified crypto trading skills into ~/.claude/skills in Claude Code, verify SHA-256 checksums, and set CLAUDE.md guardrails.
- [Cursor, Codex & Windsurf Crypto Skills Multi-IDE Setup](https://tradeskill.si/en/guides/cursor-codex-windsurf-trading-skills.html) — Map global skills folders across Cursor, Codex, Windsurf, and OpenCode, and install multi-exchange trading bundles in one command.
- [Keyless Crypto Market Data AI Skills (No API Key)](https://tradeskill.si/en/guides/keyless-crypto-market-data-skills.html) — Run zero-credential crypto market data, klines, funding-rate monitors, and token security audits across OKX, Kraken, HTX, MEXC, Binance, Gate, and BitMart.
- [Crypto Exchange Fee Rebates for AI Traders (15%–20% Off)](https://tradeskill.si/en/guides/exchange-fee-rebates-for-ai-traders.html) — Compare verified official invite fee rebates at Gate (20%), OKX (20%), Binance (20%), and Bitget (15%), model high-frequency fee savings, and isolate bot risk.
- [OKX Agent Skills: Trade CLI 1.5.1 & OnchainOS Guide](https://tradeskill.si/en/guides/okx-agent-trade-cli-tutorial.html) — Install all 18 official OKX CEX and OnchainOS AI skills, run keyless market checks, test simulated demo trading, and switch ZIP or upstream.
- [Binance 21 AI Trading Skills: CEX, P2P & Web3 Audits](https://tradeskill.si/en/guides/binance-cex-web3-ai-skills-guide.html) — Explore all 21 official Binance AI agent skills spanning CEX spot/futures, C2C P2P, smart-money market rankings, and Web3 token contract audits.
- [Gate vs Bitget AI Trading Bots Guide: Research Intel vs UTA v3](https://tradeskill.si/en/guides/gate-bitget-ai-trading-bots-guide.html) — Compare Gate modular CLI/MCP trading & intel skills (20% rebate) against Bitget bgc UTA v3 and Bitget Wallet RWA skills (15% rebate).
- [Coinbase vs Kraken vs Bybit AI Trading Skills Compared](https://tradeskill.si/en/guides/coinbase-kraken-bybit-ai-agent-comparison.html) — Compare Coinbase (CLI + hosted OAuth MCP + x402), Kraken (18 Rust CLI/MCP skills with zero-key paper trading), and Bybit V5 Trading Skills.
- [DEX AI Trading Guide: Uniswap vs Jupiter vs OKX OnchainOS Skills](https://tradeskill.si/en/guides/dex-ai-trading-uniswap-vs-jupiter.html) — Compare official DEX AI skills from Uniswap Labs (Swap, v3/v4 LP, DCA, Hook security), Jupiter Solana (Swap v2, Lend, VRFD), and OKX OnchainOS.
- [24/7 OKX AI Trading Bot: AstraQuant & 20% Rebate Guide](https://tradeskill.si/en/guides/astraquant-247-okx-ai-trading-bot.html) — Pair TradeSkill exchange skills with AstraQuant (astraquant.top): multi-model AI Council, 17 fail-closed risk gates, and 20% OKX fee rebates.

---

## Exchange Trading Fee Rebates

Active official invitation links listed on [tradeskill.si/en/rebates.html](https://tradeskill.si/en/rebates.html) for traders registering new exchange accounts:

| Exchange | Invite Code | Fee Rebate | Official Link |
|---|---|---|---|
| **OKX** | `48039151` | **20%** | [Official Invite Link](https://www.okx.com/join/48039151) |
| **Gate** | `MCHDBKYF` | **20%** | [Official Invite Link](https://www.gate.com/share/MCHDBKYF) |
| **Binance** | `1142479220` | **20%** | [Official Invite Link](https://accounts.binance.com/register?ref=1142479220) |
| **Bitget** | `DY6CJDUY` | **15%** | [Official Invite Link](https://www.bitget.com/referral/register?clacCode=DY6CJDUY&source=events&utmSource=PremierInviter) |

---

## Sister Project: AstraQuant (24/7 OKX AI Trading Bot)

Need unattended 24/7 algorithmic trading instead of manual IDE sessions? Pair these AI skills with **[AstraQuant (astraquant.top)](https://astraquant.top/)** ([`0xethanq/astra-quant-agent`](https://github.com/0xethanq/astra-quant-agent)) — an open-source, self-hosted OKX investment-committee quant engine featuring 17 fail-closed physical risk gates, cloud OCO stop-losses, and integrated 20% OKX fee rebates.

---

## Security, Risk & Attribution Transparency

1. **Credentials stay on your machine**: API keys, secrets, CDP credentials, and wallet private keys are configured strictly for the corresponding local exchange CLI (`okx`, `kraken`, `htx-cli`, `cdcx`, `bgc`, etc.).
2. **Verify before live execution**: Test with keyless market-data skills (`okx-cex-market`, `kraken-market-intel`, `htx-market-overview`) or built-in paper/demo environments before signing live trades.
3. **OKX AI Builder Attribution**: `skills/okx-cex-trade` and `skills/okx-cex-bot` preserve TradeSkill's `--aiBuilderCode` CLI order tag configuration per [OKX's AI Builder integration rules](https://www.okx.com/zh-hans/help/ai-builder-program-integration-guide) (unmodified official OKX snapshots are linked on their [OKX GitHub repository](https://github.com/okx/agent-skills)). All remaining 92 exchange skills are byte-for-byte upstream MIT / Apache-2.0 copies.
4. **Automated CI verification**: Every commit runs [`.github/workflows/validate.yml`](.github/workflows/validate.yml) to verify all `SKILL.md` frontmatter, licenses, and plugin manifests.

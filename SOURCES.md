# TradeSkill — Upstream Sources & Commit Locks

All bundled skills in this repository are extracted from pinned upstream Git commits audited for [TradeSkill](https://tradeskill.si/en/).

| Platform | Bundled / Official-Only | Upstream License | Pinned Commit | Upstream Repository |
|---|---|---|---|---|
| **OKX** (`okx`) | 13 / 5 | MIT | `3cff92b6a5` | [https://github.com/okx/agent-skills](https://github.com/okx/agent-skills) |
| **Gate** (`gate`) | 0 / 20 | No explicit redistribution license | `b96c34099f` | [https://github.com/gate/gate-skills](https://github.com/gate/gate-skills) |
| **Binance** (`binance`) | 3 / 18 | MIT for CEX skills; follow upstream Web3 docs | `7d1b1f78d5` | [https://github.com/binance/binance-skills-hub](https://github.com/binance/binance-skills-hub) |
| **Bybit** (`bybit`) | 1 / 1 | MIT (Base Trading Skill) | `dc98490ad4` | [https://github.com/bybit-exchange/skills](https://github.com/bybit-exchange/skills) |
| **Bitget** (`bitget`) | 2 / 0 | MIT | `55747b8a33` | [https://github.com/Bitget-AI/agent-skill](https://github.com/Bitget-AI/agent-skill) |
| **Coinbase** (`coinbase`) | 3 / 1 | MIT | `6076c3e267` | [https://github.com/coinbase/agents](https://github.com/coinbase/agents) |
| **Kraken** (`kraken`) | 18 / 0 | MIT | `671cdd7f14` | [https://github.com/krakenfx/kraken-cli](https://github.com/krakenfx/kraken-cli) |
| **HTX** (`htx`) | 17 / 0 | MIT | `1c04d78d5e` | [https://github.com/htx-exchange/htx-skills-hub](https://github.com/htx-exchange/htx-skills-hub) |
| **MEXC** (`mexc`) | 16 / 0 | MIT | `c2b63fd04e` | [https://github.com/mexcdevelop/mexc-cli](https://github.com/mexcdevelop/mexc-cli) |
| **KuCoin** (`kucoin`) | 7 / 0 | MIT | `a9bda62ce7` | [https://github.com/Kucoin/kucoin-skills-hub](https://github.com/Kucoin/kucoin-skills-hub) |
| **Crypto.com** (`cryptocom`) | 2 / 0 | Apache-2.0 (Exchange notes MIT) | `92e80c5527` | [https://github.com/crypto-com/crypto-agent-trading](https://github.com/crypto-com/crypto-agent-trading) |
| **BingX** (`bingx`) | 0 / 14 | No explicit redistribution license | `5d96e72561` | [https://github.com/BingX-API/api-ai-skills](https://github.com/BingX-API/api-ai-skills) |
| **BitMart** (`bitmart`) | 0 / 3 | No explicit redistribution license | `79a4d7f5e9` | [https://github.com/bitmartexchange/bitmart-skills](https://github.com/bitmartexchange/bitmart-skills) |
| **Uniswap** (`uniswap`) | 8 / 0 | MIT | `989dbafd07` | [https://github.com/Uniswap/uniswap-ai](https://github.com/Uniswap/uniswap-ai) |
| **Jupiter** (`jupiter`) | 4 / 0 | MIT | `a2211e3f6a` | [https://github.com/jup-ag/agent-skills](https://github.com/jup-ag/agent-skills) |
| **Hyperliquid** (`hyperliquid`) | 8 / 0 | MIT (Galleon Labs skills + Official SDK) | `98331af5c4` | [https://github.com/galleonlabs/hypergrok-trading-desk](https://github.com/galleonlabs/hypergrok-trading-desk) |

## Redistribution & Attribution Notes

- **102 bundled exchange & DEX skills**: Extracted cleanly with their original `LICENSE` / `LICENSE.md` files preserved inside each `skills/<skill-name>/` directory (cross-parent `../../docs/` links in Hyperliquid skills are normalized to pinned upstream GitHub commit URLs for standalone extraction).
- **62 official-upstream-only skills**: Gate, Binance Web3, BingX, BitMart, and selected router/CLI targets are indexed in `catalog.json` (`officialOnlySkills`) and linked back to official repositories instead of mirrored here.
- **OKX AI Builder Attribution**: `skills/okx-cex-trade` and `skills/okx-cex-bot` retain TradeSkill's local `--aiBuilderCode` CLI tag configuration as disclosed in `skills/okx-cex-trade/references/attribution.md` and `skills/okx-cex-bot/references/attribution.md`.
- **Flagship Router & Funding Scanner (`skills/tradeskill`)**: Ships TradeSkill's zero-dependency stdlib script `scripts/funding_scanner.py` using public keyless exchange endpoints only.

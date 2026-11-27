---
name: tradeskill
description: Keyless cross-exchange perpetual funding-rate & basis scanner (Hyperliquid, OKX, Gate, Bitget, Binance, Bybit) plus discovery, SHA-256 verification, and install router for 164 official crypto trading AI skills across 16 exchanges and DEXs from TradeSkill (tradeskill.si) or GitHub.
---

# TradeSkill — Multi-Exchange Funding Arbitrage Scanner & Skill Router

Use this flagship meta-skill whenever the user wants to:
1. **Scan live cross-exchange perpetual funding rates & mark-price basis keylessly** across **Hyperliquid (1h)**, **OKX**, **Gate**, **Bitget**, **Binance**, and **Bybit** using Python stdlib (`scripts/funding_scanner.py`) with **zero API keys**; or
2. **Discover, verify, and install** AI agent trading skills across **16 supported exchanges and DEXs** (**164 catalog skills total**: **102 bundled redistributable MIT/Apache-2.0 skills** in this repository + **62 upstream-only official repository targets**).

- **Hub Website**: https://tradeskill.si/en/ (Chinese: https://tradeskill.si/)
- **GitHub Registry**: https://github.com/0xethanq/crypto-trading-skills
- **Machine-Readable Catalog**: https://tradeskill.si/catalog.json

## 1. Live Keyless Cross-Exchange Funding-Rate & Basis Scanner

Run `scripts/funding_scanner.py` (Python 3.9+ stdlib only, zero external packages, zero credentials) directly from this skill directory:

```sh
# 1) Compare flagship tokens across all reachable perp venues (normalizes 1h vs 8h funding to 8h & APR)
python3 scripts/funding_scanner.py --symbols BTC,ETH,SOL,HYPE

# 2) Discover top cross-venue carry spreads filtered by >= $5M 24h notional volume per leg
python3 scripts/funding_scanner.py --top 15 --min-vol 5000000

# 3) Emit structured JSON for downstream agent sizing & execution routing
python3 scripts/funding_scanner.py --symbols BTC,ETH,SOL,HYPE --json

# 4) Offline deterministic self-test (no network needed)
python3 scripts/funding_scanner.py --self-test
```

### How to Interpret & Route Execution After Scanning
- **Interval normalization**: Hyperliquid settles funding every **1h**, while OKX, Gate, Bitget, Binance, and Bybit settle every **8h** (or 4h/1h on select pairs). `funding_scanner.py` normalizes every venue onto an equivalent **8h rate (%)** and **annualized APR (%)** plus **mark-price basis (bps)** (`(short_mark - long_mark) / long_mark * 10000`).
- **Geo-blocked venues degrade cleanly**: If an endpoint returns HTTP 403/451 (e.g. Binance/Bybit from restricted regions), the scanner reports the status and computes live spreads across all reachable venues (e.g. Hyperliquid, OKX, Gate, Bitget).
- **Execution handoff**: Once an opportunity clears slippage and fees, route execution to the matching venue skills in this hub (`hyperliquid-orders` / `hyperliquid-positions`, `okx-cex-trade`, `gate-cex-trade`, `binance`, `bitget-agent-skill`), or pair with **[AstraQuant](https://astraquant.top/)** (`0xethanq/astra-quant-agent`) for 24/7 automated OKX execution.

## 2. Detect Active Agent Skills Directory

Before installing venue skills, resolve the active agent's global (or workspace) skills folder:

- **Claude Code**: `~/.claude/skills/`
- **Cursor**: `~/.cursor/skills/`
- **Windsurf**: `~/.codeium/windsurf/skills/`
- **Codex / Agents**: `~/.agents/skills/` (or `~/.codex/skills/`)
- **OpenCode**: `~/.config/opencode/skills/`
- **Google Antigravity**: `~/.gemini/antigravity/skills/`
- **WorkBuddy**: `~/.workbuddy/skills/`
- **CodeBuddy**: `~/.codebuddy/skills/`

## 3. Recommended Installation Methods

### Option A — Universal Skills CLI (`npx skills`)

Install any bundled exchange or DEX skill directly from GitHub:

```sh
# Interactive or batch selection
npx skills add 0xethanq/crypto-trading-skills

# Single skill install (examples)
npx skills add 0xethanq/crypto-trading-skills --skill hyperliquid-market-data
npx skills add 0xethanq/crypto-trading-skills --skill okx-cex-trade
npx skills add 0xethanq/crypto-trading-skills --skill kraken-market-intel
npx skills add 0xethanq/crypto-trading-skills --skill swap-planner
```

### Option B — Claude Code Plugin Marketplace

Install by exchange or DEX pack in Claude Code:

```text
/plugin marketplace add 0xethanq/crypto-trading-skills
/plugin install tradeskill-hub@crypto-trading-skills
/plugin install hyperliquid-skills@crypto-trading-skills
/plugin install okx-skills@crypto-trading-skills
/plugin install kraken-skills@crypto-trading-skills
```

### Option C — SHA-256 Verified Direct Installer (supports individual IDs, platform names, or `all`)

**macOS / Linux:**

```sh
curl -fsSL "https://tradeskill.si/install.sh" | sh -s hyperliquid-market-data
curl -fsSL "https://tradeskill.si/install.sh" | sh -s kraken
curl -fsSL "https://tradeskill.si/install.sh" | sh -s all
```

**Windows PowerShell:**

```powershell
powershell -NoProfile -Command "& ([scriptblock]::Create((irm 'https://tradeskill.si/install.ps1'))) hyperliquid-market-data"
```

## 4. Resolving Upstream-Only Skills (62 Official Targets)

Some platforms (such as **Gate**'s 20 skills, **Binance Web3**'s 14 skills, **BingX**'s 14 skills, and **BitMart**'s 3 skills) do not declare permissive third-party ZIP redistribution or depend on upstream CLI generators.

When the user asks for one of these:
1. Fetch `https://tradeskill.si/catalog.json` (or read `catalog.json` in this repo under `officialOnlySkills`).
2. Follow the entry's `source` or `upstream` URL and official CLI instructions instead of searching `skills/`.

## 5. Supported Platforms (16 Exchanges & DEXs)

- `okx` (OKX): CEX spot/futures markets, orders, and bots alongside OnchainOS wallet, DeFi, and DEX skills. [13 bundled in repo / 5 upstream-only] — Runtime: OKX Trade CLI 1.5.1 for CEX skills; onchainos CLI for OnchainOS skills (public quotes need no key).
- `gate` (Gate): Official CEX spot, derivatives, grid bots, research/risk intel, plus Gate DEX quotes, swaps, and wallets. [0 bundled in repo / 20 upstream-only] — Runtime: Install Gate CLI / MCP first and generate standalone skill folders per upstream instructions.
- `binance` (Binance): Official Binance CEX suite and Web3 on-chain toolkit: spot, futures, P2P, Smart Money signals, audits, and Meme Rush. [3 bundled in repo / 18 upstream-only] — Runtime: Install official Binance CLI or baw CLI. Public quotes run anonymously; trading requires local auth.
- `bybit` (Bybit): Official Bybit Trading Skill and V5 CLI source entrypoints for market data, spot, derivatives, and accounts. [1 bundled in repo / 1 upstream-only] — Runtime: Base skill runs on Bybit V5 API with local auth config; official trading CLI is optional.
- `bitget` (Bitget): Bitget Agent Hub UTA v3 exchange skills (bgc CLI) plus official Bitget Wallet on-chain quotes, swaps, and RWA stocks. [2 bundled in repo / 0 upstream-only] — Runtime: Node.js >= 20; use official bgc CLI for CEX skills and Bitget Wallet docs for on-chain skills.
- `coinbase` (Coinbase): Official Coinbase Agent suite spanning local Coinbase CLI (CDP keys), hosted OAuth MCP, Wallet MCP, and x402 payments. [3 bundled in repo / 1 upstream-only] — Runtime: Local CLI requires Node.js >= 22, @coinbase/coinbase-cli & CDP API keys; hosted & wallet MCP use OAuth.
- `kraken` (Kraken): Single-binary Rust Kraken CLI & MCP matrix with built-in zero-auth Paper Trading across spot, futures, grids, and basis strategies. [18 bundled in repo / 0 upstream-only] — Runtime: Install official kraken / kraken-mcp binaries; public quotes & Paper Trading sandbox require no API keys.
- `htx` (HTX): Complete 17-skill HTX suite: spot & USDT-M futures markets/orders, funding rates, OI & liquidation streams, 51 indicators, and 3-pillar scoring. [17 bundled in repo / 0 upstream-only] — Runtime: Uses official htx-cli with SHA-256 verification; market, OI, funding, and liquidation streams work without API keys.
- `mexc` (MEXC): Official MEXC CLI skill suite built on @mexc-ai/cli: spot & contract markets/orders/accounts, AI grid bots, DCA, convert, and earn. [16 bundled in repo / 0 upstream-only] — Runtime: Node.js >= 20 with @mexc-ai/cli. Public spot & futures quotes need no key; trading requires local API keys.
- `kucoin` (KuCoin): Official 7-module KuCoin Skills Hub for read-only REST analytics across spot, futures, margin, assets, convert, earn, and broker APIs. [7 bundled in repo / 0 upstream-only] — Runtime: Uses KuCoin Classic REST API (read-only GET queries; authenticated endpoints need Key, Secret & Passphrase).
- `cryptocom` (Crypto.com): Official dual-app Crypto.com agent skills: Exchange via @cryptocom/cdcx-cli (with paper trading) and Crypto.com App fiat/buy flows. [2 bundled in repo / 0 upstream-only] — Runtime: Exchange uses @cryptocom/cdcx-cli with OAuth & paper simulation; App requires App API credentials.
- `bingx` (BingX): BingX API AI Skills Hub covering spot, USDT-M/coin-M perpetuals, standard futures, copy trading, dynamic ATR SL/TP, Maker entry & 78 indicators. [0 bundled in repo / 14 upstream-only] — Runtime: Python 3 with strategy dependencies (pandas / pandas-ta-classic); follow upstream repository installation guide.
- `bitmart` (BitMart): Official BitMart AI suite covering spot trading & WebSocket streams, perpetual futures with demo mode, and 12 keyless Web3 Wallet endpoints. [0 bundled in repo / 3 upstream-only] — Runtime: Configure BitMart SDK / API keys for exchange skills; all 12 Web3 Wallet AI endpoints run without API keys.
- `uniswap` (Uniswap): Uniswap Labs official AI skills for EVM swap planning, v3/v4 LP liquidity, on-chain DCA/index/copy bots, and v4 hook security. [8 bundled in repo / 0 upstream-only] — Runtime: Decentralized on-chain protocol skills; no exchange account needed — bring your own wallet & RPC for execution.
- `jupiter` (Jupiter): Official Solana aggregator Jupiter Agent Skills covering Swap v2, Lend, Perps, DCA/Trigger integration and VRFD token verification. [4 bundled in repo / 0 upstream-only] — Runtime: Decentralized Solana protocol integration skills; docs & quotes need no private key, swaps use your own wallet & RPC.
- `hyperliquid` (Hyperliquid): High-performance L1 perp & spot orderbook DEX skills: keyless quotes/funding/WS, trade-only API Wallet auth, positions, TWAP & HIP-3 reference. [8 bundled in repo / 0 upstream-only] — Runtime: Decentralized L1 perp DEX: /info quotes & WebSocket require no key; live orders use a trade-only Agent API Wallet with the official Python/TS SDK (Testnet supported).

## 6. Security, Paper Trading & Attribution Checklist

1. **Credentials stay local**: API keys, passphrases, CDP tokens, and wallet/API Wallet private keys are always configured locally for the corresponding official exchange CLI/SDK; TradeSkill never handles credentials.
2. **Read-only & paper/testnet mode first**: Start with keyless market skills (`hyperliquid-market-data`, `okx-cex-market`, `kraken-market-intel`, `htx-market-overview`) or built-in paper/testnet sandboxes (`kraken-paper-strategy`, Hyperliquid Testnet, OKX demo, Crypto.com paper mode) before enabling live order execution.
3. **Attribution transparency**: In `okx-cex-trade` and `okx-cex-bot`, local CLI trade execution commands pass `--aiBuilderCode` order tags per the [OKX AI Builder Program](https://www.okx.com/zh-hans/help/ai-builder-program-integration-guide). All other 100 exchange & DEX skills preserve their upstream MIT / Apache-2.0 `SKILL.md` commands unmodified (Hyperliquid cross-parent `../../docs/` links are normalized to pinned upstream GitHub commit URLs for standalone ZIP compatibility).

---
name: tradeskill
description: Discover, verify, and install 156 official crypto trading AI skills across 15 exchanges and DEXs (OKX, Gate, Binance, Bybit, Bitget, Coinbase, Kraken, HTX, MEXC, KuCoin, Crypto.com, BingX, BitMart, Uniswap, Jupiter) from TradeSkill (astraquant.tech) or GitHub.
---

# TradeSkill — Multi-Exchange Crypto Trading Skill Router

Use this flagship skill whenever the user wants to discover, compare, install, or set up AI agent trading skills for cryptocurrencies across **15 supported exchanges and DEXs** (**156 official skills total**: **94 bundled redistributable MIT/Apache-2.0 skills** in this repository + **62 upstream-only official repository targets**).

- **Hub Website**: https://astraquant.tech/en/ (Chinese: https://astraquant.tech/)
- **GitHub Registry**: https://github.com/0xethanq/crypto-trading-skills
- **Machine-Readable Catalog**: https://astraquant.tech/catalog.json

## 1. Detect Active Agent Skills Directory

Before installing, resolve the active agent's global (or workspace) skills folder:

- **Claude Code**: `~/.claude/skills/`
- **Cursor**: `~/.cursor/skills/`
- **Windsurf**: `~/.codeium/windsurf/skills/`
- **Codex / Agents**: `~/.agents/skills/` (or `~/.codex/skills/`)
- **OpenCode**: `~/.config/opencode/skills/`
- **Google Antigravity**: `~/.gemini/antigravity/skills/`
- **WorkBuddy**: `~/.workbuddy/skills/`
- **CodeBuddy**: `~/.codebuddy/skills/`

## 2. Recommended Installation Methods

### Option A — Universal Skills CLI (`npx skills`)

Install any bundled exchange skill directly from GitHub:

```sh
# Interactive or batch selection
npx skills add 0xethanq/crypto-trading-skills

# Single skill install (examples)
npx skills add 0xethanq/crypto-trading-skills --skill okx-cex-trade
npx skills add 0xethanq/crypto-trading-skills --skill kraken-market-intel
npx skills add 0xethanq/crypto-trading-skills --skill swap-planner
```

### Option B — Claude Code Plugin Marketplace

Install by exchange pack in Claude Code:

```text
/plugin marketplace add 0xethanq/crypto-trading-skills
/plugin install okx-skills@crypto-trading-skills
/plugin install kraken-skills@crypto-trading-skills
/plugin install tradeskill-hub@crypto-trading-skills
```

### Option C — SHA-256 Verified Direct Installer (supports individual IDs, platform names, or `all`)

**macOS / Linux:**

```sh
curl -fsSL "https://astraquant.tech/install.sh" | sh -s okx-cex-market
curl -fsSL "https://astraquant.tech/install.sh" | sh -s kraken
curl -fsSL "https://astraquant.tech/install.sh" | sh -s all
```

**Windows PowerShell:**

```powershell
powershell -NoProfile -Command "& ([scriptblock]::Create((irm 'https://astraquant.tech/install.ps1'))) okx-cex-market"
```

## 3. Resolving Upstream-Only Skills (62 Official Targets)

Some platforms (such as **Gate**'s 20 skills, **Binance Web3**'s 14 skills, **BingX**'s 14 skills, and **BitMart**'s 3 skills) do not declare permissive third-party ZIP redistribution or depend on upstream CLI generators.

When the user asks for one of these:
1. Fetch `https://astraquant.tech/catalog.json` (or read `catalog.json` in this repo under `officialOnlySkills`).
2. Follow the entry's `source` or `upstream` URL and official CLI instructions instead of searching `skills/`.

## 4. Supported Platforms (15 Exchanges & DEXs)

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

## 5. Security, Paper Trading & Attribution Checklist

1. **Credentials stay local**: API keys, passphrases, CDP tokens, and wallet private keys are always configured locally for the corresponding official exchange CLI; TradeSkill never handles credentials.
2. **Read-only & paper mode first**: Start with keyless market skills (`okx-cex-market`, `kraken-market-intel`, `htx-market-overview`) or built-in paper/demo sandboxes (`kraken-paper-strategy`, OKX demo, Crypto.com paper mode) before enabling live order execution.
3. **Attribution transparency**: In `okx-cex-trade` and `okx-cex-bot`, local CLI trade execution commands pass `--aiBuilderCode` order tags per the [OKX AI Builder Program](https://www.okx.com/zh-hans/help/ai-builder-program-integration-guide). All other 92 exchange skills are byte-for-byte upstream MIT / Apache-2.0 snapshots with unmodified commands.

<div align="center">

# TradeSkill — 加密货币交易所 AI Agent 技能仓库

**收录 15 大主流交易所与 DEX · 95 个可直装技能包 + 156 个官方技能全量索引**

[English](README.md) · **简体中文** · [中文站点目录](https://astraquant.tech/) · [来源与 Commit 锁定](SOURCES.md)

[![Agent Skills](https://img.shields.io/badge/Agent_Skills-95_可直装-10b981?style=flat-square)](catalog.json)
[![Exchanges & DEXs](https://img.shields.io/badge/覆盖平台-15_家-3b82f6?style=flat-square)](https://astraquant.tech/)
[![Clients](https://img.shields.io/badge/适配客户端-Claude_Code_%7C_Cursor_%7C_Codex_%7C_Windsurf-111827?style=flat-square)](#快速开始)
[![Website](https://img.shields.io/badge/官方网站-astraquant.tech-f59e0b?style=flat-square)](https://astraquant.tech/)

</div>

---

**TradeSkill** 为加密货币交易场景打造统一的 AI Agent 技能分发仓库，兼容 **Claude Code**、**Cursor**、**Codex CLI**、**Windsurf**、**OpenCode** 与 **Google Antigravity**。

- **上游 Commit 锁定与许可完整**：仓库内 94 个交易所与 DEX 技能均保留原仓库 MIT / Apache-2.0 `LICENSE`、完整 `SKILL.md` 及 `references/` 文档，外加旗舰路由总技能 `tradeskill`。
- **本地凭证零托管**：所有 API Key、Secret 与钱包签名均仅在你本地官方文档对应的官方 CLI 中运行。
- **多种安装通道**：原生兼容 `npx skills add`、Claude Code `/plugin marketplace add`、Cursor 插件市场以及带 SHA-256 校验的一键安装脚本。

---

## 快速开始

### 1. 通用 Skills CLI 安装（推荐，兼容主流 Agent）

```sh
# 浏览并选择要安装的技能
npx skills add 0xethanq/crypto-trading-skills

# 按名称直装单个技能
npx skills add 0xethanq/crypto-trading-skills --skill tradeskill
npx skills add 0xethanq/crypto-trading-skills --skill okx-cex-trade
npx skills add 0xethanq/crypto-trading-skills --skill kraken-market-intel
npx skills add 0xethanq/crypto-trading-skills --skill swap-planner
```

### 2. Claude Code 插件市场安装

添加一次市场后即可按交易所整套安装：

```text
/plugin marketplace add 0xethanq/crypto-trading-skills

# 安装全平台路由或指定交易所技能包
/plugin install tradeskill-hub@crypto-trading-skills
/plugin install okx-skills@crypto-trading-skills
/plugin install binance-skills@crypto-trading-skills
/plugin install kraken-skills@crypto-trading-skills
/plugin install uniswap-skills@crypto-trading-skills
```

### 3. 一键脚本安装（带 SHA-256 校验）

支持传入单个技能 ID、交易所名称（如 `okx`、`kraken`、`htx`）或 `all`：

**macOS / Linux：**

```sh
curl -fsSL "https://astraquant.tech/install.sh" | sh -s okx-cex-market
curl -fsSL "https://astraquant.tech/install.sh" | sh -s -- --client cursor kraken
```

**Windows PowerShell：**

```powershell
powershell -NoProfile -Command "& ([scriptblock]::Create((irm 'https://astraquant.tech/install.ps1'))) okx-cex-market"
```

### 4. 对话提示词全自动安装

把下面这句话直接发给你的 AI 助手：

> 根据 `https://astraquant.tech/install/skillhub.md` 帮我检查目录，并在当前客户端安装 `okx-cex-market` 和 `kraken-market-intel`。

---

## 支持平台矩阵（15 家交易所与 DEX · 156 个官方技能）

| 平台 | 类型 | 收录与分发方式 | 开源许可 | 相关入口 |
|---|---|---|---|---|
| **OKX** (`okx`) | CEX | **13** 直装 + 5 官方源 | MIT | [平台专页](https://astraquant.tech/exchanges/okx.html) · [上游仓库](https://github.com/okx/agent-skills) |
| **Gate** (`gate`) | CEX | 仅官方源（20 个） | 未找到明确的再分发许可 | [平台专页](https://astraquant.tech/exchanges/gate.html) · [上游仓库](https://github.com/gate/gate-skills) |
| **Binance** (`binance`) | CEX | **3** 直装 + 18 官方源 | CEX 交易技能目录为 MIT；Web3 子目录按上游仓库说明使用 | [平台专页](https://astraquant.tech/exchanges/binance.html) · [上游仓库](https://github.com/binance/binance-skills-hub) |
| **Bybit** (`bybit`) | CEX | **1** 直装 + 1 官方源 | 基础交易技能 MIT | [平台专页](https://astraquant.tech/exchanges/bybit.html) · [上游仓库](https://github.com/bybit-exchange/skills) |
| **Bitget** (`bitget`) | CEX | **2** 个直装 | MIT | [平台专页](https://astraquant.tech/exchanges/bitget.html) · [上游仓库](https://github.com/Bitget-AI/agent-skill) |
| **Coinbase** (`coinbase`) | CEX | **3** 直装 + 1 官方源 | MIT | [平台专页](https://astraquant.tech/exchanges/coinbase.html) · [上游仓库](https://github.com/coinbase/agents) |
| **Kraken** (`kraken`) | CEX | **18** 个直装 | MIT | [平台专页](https://astraquant.tech/exchanges/kraken.html) · [上游仓库](https://github.com/krakenfx/kraken-cli) |
| **HTX** (`htx`) | CEX | **17** 个直装 | MIT | [平台专页](https://astraquant.tech/exchanges/htx.html) · [上游仓库](https://github.com/htx-exchange/htx-skills-hub) |
| **MEXC** (`mexc`) | CEX | **16** 个直装 | MIT | [平台专页](https://astraquant.tech/exchanges/mexc.html) · [上游仓库](https://github.com/mexcdevelop/mexc-cli) |
| **KuCoin** (`kucoin`) | CEX | **7** 个直装 | MIT | [平台专页](https://astraquant.tech/exchanges/kucoin.html) · [上游仓库](https://github.com/Kucoin/kucoin-skills-hub) |
| **Crypto.com** (`cryptocom`) | CEX | **2** 个直装 | Apache-2.0（Exchange Skill 标注 MIT） | [平台专页](https://astraquant.tech/exchanges/cryptocom.html) · [上游仓库](https://github.com/crypto-com/crypto-agent-trading) |
| **BingX** (`bingx`) | CEX | 仅官方源（14 个） | 未找到明确的再分发许可 | [平台专页](https://astraquant.tech/exchanges/bingx.html) · [上游仓库](https://github.com/BingX-API/api-ai-skills) |
| **BitMart** (`bitmart`) | CEX | 仅官方源（3 个） | 未找到明确的再分发许可 | [平台专页](https://astraquant.tech/exchanges/bitmart.html) · [上游仓库](https://github.com/bitmartexchange/bitmart-skills) |
| **Uniswap** (`uniswap`) | DEX | **8** 个直装 | MIT | [平台专页](https://astraquant.tech/exchanges/uniswap.html) · [上游仓库](https://github.com/Uniswap/uniswap-ai) |
| **Jupiter** (`jupiter`) | DEX | **4** 个直装 | MIT | [平台专页](https://astraquant.tech/exchanges/jupiter.html) · [上游仓库](https://github.com/jup-ag/agent-skills) |

---

## 可直装技能目录（共 95 个）

展开任意交易所即可直接查看仓库内的 `SKILL.md`，或跳转至 [astraquant.tech](https://astraquant.tech/) 查看在线文件预览与一键提问提示词：

- [`tradeskill`](skills/tradeskill/SKILL.md) — 探索、校验并安装覆盖 15 家主流交易所与 DEX 的 156 个官方加密货币 AI 交易技能。（[站点首页](https://astraquant.tech/)）
<details>
<summary><strong>欧易 OKX（<code>okx</code>）— 13 个可直装技能 · 插件包 <code>okx-skills</code></strong></summary>

| 技能目录（含 `npx --skill` 名称） | 版本 | 说明 | 详情页 |
|---|---|---|---|
| [`okx-cex-trade`](skills/okx-cex-trade/SKILL.md) *（含订单归因）* | `1.5.1` | OKX 下单：现货、永续、交割、期权及可用站点的事件合约订单管理。 | [TradeSkill](https://astraquant.tech/skills/okx-cex-trade.html) |
| [`okx-cex-bot`](skills/okx-cex-bot/SKILL.md) *（含订单归因）* | `1.5.1` | OKX Bot 策略：创建与管理网格、DCA、智能组合及定投策略。 | [TradeSkill](https://astraquant.tech/skills/okx-cex-bot.html) |
| [`okx-cex-market`](skills/okx-cex-market/SKILL.md) | `1.5.1` | OKX 行情速览：查询报价、盘口、K 线、资金费率与技术指标，不需要交易凭证。 | [TradeSkill](https://astraquant.tech/skills/okx-cex-market.html) |
| [`okx-cex-portfolio`](skills/okx-cex-portfolio/SKILL.md) | `1.5.1` | OKX 账户与持仓：查看余额、持仓、盈亏和费率，也包含资金划转等写操作。 | [TradeSkill](https://astraquant.tech/skills/okx-cex-portfolio.html) |
| [`okx-cex-smartmoney`](skills/okx-cex-smartmoney/SKILL.md) | `1.5.1` | OKX 聪明钱：查询交易员榜单、历史成交、持仓与聚合信号。 | [TradeSkill](https://astraquant.tech/skills/okx-cex-smartmoney.html) |
| [`okx-sentiment-tracker`](skills/okx-sentiment-tracker/SKILL.md) | `1.5.1` | OKX 情绪追踪器：查询加密新闻、热门资产、市场情绪与经济日历。 | [TradeSkill](https://astraquant.tech/skills/okx-sentiment-tracker.html) |
| [`okx-cex-auth`](skills/okx-cex-auth/SKILL.md) | `1.5.1` | OKX CLI 授权配置：在用户自己的设备上配置官方 CLI 登录或 API 凭证。 | [TradeSkill](https://astraquant.tech/skills/okx-cex-auth.html) |
| [`okx-cex-skill-mp`](skills/okx-cex-skill-mp/SKILL.md) | `1.5.1` | OKX 技能市场工具：通过官方 CLI 搜索、安装、更新技能并校验官方市场的签名。 | [TradeSkill](https://astraquant.tech/skills/okx-cex-skill-mp.html) |
| [`okx-cex-earn`](skills/okx-cex-earn/SKILL.md) | `1.5.1` | OKX 赚币 Skill：查询和管理可用的简单赚币、闪赚、链上赚币等产品。 | [TradeSkill](https://astraquant.tech/skills/okx-cex-earn.html) |
| [`earn-hunter`](skills/earn-hunter/SKILL.md) | `1.5.1` | OKX 赚币猎手：监控闪赚、定期和活期机会，可选定时通知；不是自动成交模块。 | [TradeSkill](https://astraquant.tech/skills/earn-hunter.html) |
| [`okx-defi`](skills/okx-defi/SKILL.md) | `4.6.12` | OKX Onchain DeFi 聚合管理：发现与管理 OKX 聚合的多链 DeFi 质押、借贷、流动性池及 APY / TVL 历史收益与持仓。 | [TradeSkill](https://astraquant.tech/skills/okx-defi.html) |
| [`okx-dapp-discovery`](skills/okx-dapp-discovery/SKILL.md) | `latest` | OKX 链上 DApp 路由发现：检索并路由多链第三方 DApp 能力（Aave、Hyperliquid、Polymarket、pump.fun 等），不包含签名广播。 | [TradeSkill](https://astraquant.tech/skills/okx-dapp-discovery.html) |
| [`okx-mcp-services`](skills/okx-mcp-services/SKILL.md) | `4.6.12` | OKX Onchain MCP 情报服务：通过钱包凭据调用 NewsLiquid / 6551 MCP 情报与推特加密资讯数据源，辅助链上研究。 | [TradeSkill](https://astraquant.tech/skills/okx-mcp-services.html) |

</details>

<details>
<summary><strong>币安 Binance（<code>binance</code>）— 3 个可直装技能 · 插件包 <code>binance-skills</code></strong></summary>

| 技能目录（含 `npx --skill` 名称） | 版本 | 说明 | 详情页 |
|---|---|---|---|
| [`binance`](skills/binance/SKILL.md) | `2.1.0` | 币安 CEX 交易：通过 binance-cli 做现货、U 本位合约和闪兑。不是 Binance Wallet 或 Binance.US。 | [TradeSkill](https://astraquant.tech/skills/binance.html) |
| [`binance-p2p`](skills/binance-p2p/SKILL.md) (`--skill p2p`) | `1.1.0` | 币安 C2C / P2P 交易：查询 P2P 买卖挂单报价、支付方式、历史订单、申诉进度与商家广告管理。 | [TradeSkill](https://astraquant.tech/skills/binance-p2p.html) |
| [`binance-onchain-pay`](skills/binance-onchain-pay/SKILL.md) (`--skill onchain-pay-open-api`) | `0.1.2` | 币安法币买币直提：法币入金实时报价、支付方式查询与预下单直提外部链上钱包。 | [TradeSkill](https://astraquant.tech/skills/binance-onchain-pay.html) |

</details>

<details>
<summary><strong>Bybit Bybit（<code>bybit</code>）— 1 个可直装技能 · 插件包 <code>bybit-skills</code></strong></summary>

| 技能目录（含 `npx --skill` 名称） | 版本 | 说明 | 详情页 |
|---|---|---|---|
| [`bybit-trading`](skills/bybit-trading/SKILL.md) | `1.7.13` | Bybit Trading Skill：Bybit V5 的行情、现货、衍生品、策略与账户操作，含模块说明文件，装机即可用。 | [TradeSkill](https://astraquant.tech/skills/bybit-trading.html) |

</details>

<details>
<summary><strong>Bitget Bitget（<code>bitget</code>）— 2 个可直装技能 · 插件包 <code>bitget-skills</code></strong></summary>

| 技能目录（含 `npx --skill` 名称） | 版本 | 说明 | 详情页 |
|---|---|---|---|
| [`bitget`](skills/bitget/SKILL.md) | `3.0.0` | Bitget UTA 交易：用 bgc 命令行操作 Bitget 统一交易账户，覆盖行情、现货、合约和账户，附模拟盘说明。 | [TradeSkill](https://astraquant.tech/skills/bitget-agent-skill.html) |
| [`bitget-wallet`](skills/bitget-wallet/SKILL.md) | `2026.10.29-2` | Bitget Wallet 链上行情与 Swap：覆盖 ETH/SOL/BSC/Base 多链行情、Swap 报价、K 线榜单、代币安全审计与 RWA 美股交易。 | [TradeSkill](https://astraquant.tech/skills/bitget-wallet.html) |

</details>

<details>
<summary><strong>Coinbase Coinbase（<code>coinbase</code>）— 3 个可直装技能 · 插件包 <code>coinbase-skills</code></strong></summary>

| 技能目录（含 `npx --skill` 名称） | 版本 | 说明 | 详情页 |
|---|---|---|---|
| [`coinbase-cli`](skills/coinbase-cli/SKILL.md) | `latest` | Coinbase CLI 交易与组合管理：通过 @coinbase/coinbase-cli 与 CDP API Key 本地执行投资组合查询、行情、交易、闪兑与衍生品风控。 | [TradeSkill](https://astraquant.tech/skills/coinbase-cli.html) |
| [`coinbase-mcp`](skills/coinbase-mcp/SKILL.md) | `latest` | Coinbase 托管 MCP（OAuth）：通过原生 OAuth 连接 Coinbase 官方托管 MCP（agents.coinbase.com/mcp），远程调用交易、组合与付费研报工具。 | [TradeSkill](https://astraquant.tech/skills/coinbase-mcp.html) |
| [`coinbase-wallet-mcp`](skills/coinbase-wallet-mcp/SKILL.md) (`--skill wallet-mcp`) | `0.1.0` | Coinbase Wallet MCP 链上钱包：为 AI 助手接入 Coinbase Wallet Account，支持余额查询、代币发送、链上兑换、消息签名与 x402 支付。 | [TradeSkill](https://astraquant.tech/skills/coinbase-wallet-mcp.html) |

</details>

<details>
<summary><strong>Kraken Kraken（<code>kraken</code>）— 18 个可直装技能 · 插件包 <code>kraken-skills</code></strong></summary>

| 技能目录（含 `npx --skill` 名称） | 版本 | 说明 | 详情页 |
|---|---|---|---|
| [`kraken-setup`](skills/kraken-setup/SKILL.md) | `1.1.0` | Kraken CLI 安装与模拟盘初始化：5 分钟安装单二进制 kraken / kraken-mcp、创建免密 Paper Trading 模拟盘工作区并配置凭证。 | [TradeSkill](https://astraquant.tech/skills/kraken-setup.html) |
| [`kraken-market-intel`](skills/kraken-market-intel/SKILL.md) | `1.0.0` | Kraken 低噪实时行情与盘口：免密拉取 Kraken 现货与合约 Ticker、OHLC K 线、盘口深度与近期成交快照。 | [TradeSkill](https://astraquant.tech/skills/kraken-market-intel.html) |
| [`kraken-spot-execution`](skills/kraken-spot-execution/SKILL.md) | `1.0.0` | Kraken 现货下单与成交校验：带参数前置校验、二次确认闸门与成交后复核的 Kraken 现货标准下单技能。 | [TradeSkill](https://astraquant.tech/skills/kraken-spot-execution.html) |
| [`kraken-futures-trading`](skills/kraken-futures-trading/SKILL.md) | `1.0.0` | Kraken 期货与永续全周期交易：覆盖 Kraken Futures 合约开平仓、保证金调整、杠杆设置与全生命周期委托管理。 | [TradeSkill](https://astraquant.tech/skills/kraken-futures-trading.html) |
| [`kraken-portfolio-intel`](skills/kraken-portfolio-intel/SKILL.md) | `1.0.0` | Kraken 资产组合与盈亏分析：汇总 Kraken 账户净值、历史成交归因、已实现/浮动盈亏并支持报表导出。 | [TradeSkill](https://astraquant.tech/skills/kraken-portfolio-intel.html) |
| [`kraken-order-types`](skills/kraken-order-types/SKILL.md) | `1.0.0` | Kraken 全订单类型与高级参数：详解 Kraken 现货与期货市价、限价、Post-Only、Iceberg、Time-in-Force 等全部委托参数。 | [TradeSkill](https://astraquant.tech/skills/kraken-order-types.html) |
| [`kraken-stop-take-profit`](skills/kraken-stop-take-profit/SKILL.md) | `1.0.0` | Kraken 止损与止盈风控委托：为 Kraken 持仓配置触发止损、限价止盈及跟踪风控退出条件，严格限制单笔风险敞口。 | [TradeSkill](https://astraquant.tech/skills/kraken-stop-take-profit.html) |
| [`kraken-twap-execution`](skills/kraken-twap-execution/SKILL.md) | `1.0.0` | Kraken TWAP 拆单执行：将大额委托按时间加权切分拆单执行，显著降低盘口滑点与市场冲击成本。 | [TradeSkill](https://astraquant.tech/skills/kraken-twap-execution.html) |
| [`kraken-grid-trading`](skills/kraken-grid-trading/SKILL.md) | `1.0.0` | Kraken 自动网格交易策略：在指定价格区间内自动铺设等差/等比买卖网格挂单，高抛低吸捕获震荡收益。 | [TradeSkill](https://astraquant.tech/skills/kraken-grid-trading.html) |
| [`kraken-dca-strategy`](skills/kraken-dca-strategy/SKILL.md) | `1.0.0` | Kraken DCA 定投策略：按周期自动执行定额买入、记录平均持仓成本并持续追踪定投收益率表现。 | [TradeSkill](https://astraquant.tech/skills/kraken-dca-strategy.html) |
| [`kraken-basis-trading`](skills/kraken-basis-trading/SKILL.md) | `1.0.0` | Kraken 期现基差 Delta 中性套利：监测现货与期货基差溢价，构建现货做多 + 期货做空的 Delta 中性套利头寸。 | [TradeSkill](https://astraquant.tech/skills/kraken-basis-trading.html) |
| [`kraken-funding-carry`](skills/kraken-funding-carry/SKILL.md) | `1.0.0` | Kraken 永续资金费率套利：扫描高资金费率永续合约标的，在收取费率一侧建仓并对冲方向性风险。 | [TradeSkill](https://astraquant.tech/skills/kraken-funding-carry.html) |
| [`kraken-earn-staking`](skills/kraken-earn-staking/SKILL.md) | `1.0.0` | Kraken 质押与理财收益：对比 Kraken 链上 Staking 与赚币产品年化利率，管理质押配置并追踪收益明细。 | [TradeSkill](https://astraquant.tech/skills/kraken-earn-staking.html) |
| [`kraken-rebalancing`](skills/kraken-rebalancing/SKILL.md) | `1.0.0` | Kraken 投资组合自动再平衡：按设定权重监控多币种仓位偏离度，生成调仓清单并控制单次调仓换手成本。 | [TradeSkill](https://astraquant.tech/skills/kraken-rebalancing.html) |
| [`kraken-liquidation-guard`](skills/kraken-liquidation-guard/SKILL.md) | `1.0.0` | Kraken 合约强平哨兵监控：实时监测合约保证金率与强平线距离，在风险临近时自动触发减仓或紧急风控预案。 | [TradeSkill](https://astraquant.tech/skills/kraken-liquidation-guard.html) |
| [`kraken-paper-strategy`](skills/kraken-paper-strategy/SKILL.md) | `1.0.0` | Kraken 零风险 Paper 模拟盘测试：基于 Kraken 实时真实行情在本地沙盒运行模拟策略与回放评估，无需真实资金或密钥。 | [TradeSkill](https://astraquant.tech/skills/kraken-paper-strategy.html) |
| [`kraken-mcp-integration`](skills/kraken-mcp-integration/SKILL.md) | `1.1.0` | Kraken MCP 原生服务端配置：将 kraken-mcp 原生接入 Claude Code、Cursor 与 Codex，免除子进程封装直接调用工具。 | [TradeSkill](https://astraquant.tech/skills/kraken-mcp-integration.html) |
| [`kraken-ws-streaming`](skills/kraken-ws-streaming/SKILL.md) | `1.0.0` | Kraken WebSocket 实时流：订阅 Kraken 现货与合约 WebSocket 逐笔成交、增量盘口、K 线与私有委托更新流。 | [TradeSkill](https://astraquant.tech/skills/kraken-ws-streaming.html) |

</details>

<details>
<summary><strong>火币 HTX（<code>htx</code>）— 17 个可直装技能 · 插件包 <code>htx-skills</code></strong></summary>

| 技能目录（含 `npx --skill` 名称） | 版本 | 说明 | 详情页 |
|---|---|---|---|
| [`htx-spot-market`](skills/htx-spot-market/SKILL.md) (`--skill htx/spot-market`) | `2.0.0` | HTX 现货实时行情：免密通过 htx-cli 查询火币 HTX 现货聚合行情、K 线、盘口深度、逐笔成交与交易规则。 | [TradeSkill](https://astraquant.tech/skills/htx-spot-market.html) |
| [`htx-spot-trading`](skills/htx-spot-trading/SKILL.md) (`--skill htx/spot-trading`) | `2.0.0` | HTX 现货交易与杠杆借币：强制人工参数确认后执行 HTX 现货限价/市价下单、撤单、改单、订单查询与杠杆借贷。 | [TradeSkill](https://astraquant.tech/skills/htx-spot-trading.html) |
| [`htx-spot-account`](skills/htx-spot-account/SKILL.md) (`--skill htx/spot-account`) | `2.0.0` | HTX 现货账户与划转：查询火币 HTX 现货余额、持仓估值与流水，并支持现货与合约账户间资产划转。 | [TradeSkill](https://astraquant.tech/skills/htx-spot-account.html) |
| [`htx-futures-market`](skills/htx-futures-market/SKILL.md) (`--skill htx/futures-market`) | `2.0.0` | HTX U 本位永续行情：免密查询 HTX USDT-M 永续合约信息、指数价格、K 线、最优挂单与深度盘口。 | [TradeSkill](https://astraquant.tech/skills/htx-futures-market.html) |
| [`htx-futures-trading`](skills/htx-futures-trading/SKILL.md) (`--skill htx/futures-trading`) | `2.0.0` | HTX U 本位永续下单：覆盖 HTX 永续合约开仓、平仓、止盈止损、计划委托、改单与撤单（写操作二次确认）。 | [TradeSkill](https://astraquant.tech/skills/htx-futures-trading.html) |
| [`htx-futures-account`](skills/htx-futures-account/SKILL.md) (`--skill htx/futures-account`) | `2.0.0` | HTX 永续合约账户与杠杆：查询 HTX 永续合约权益余额、当前持仓、杠杆梯度、调整系数与统一账户模式切换。 | [TradeSkill](https://astraquant.tech/skills/htx-futures-account.html) |
| [`htx-funding-rate`](skills/htx-funding-rate/SKILL.md) (`--skill htx/funding-rate`) | `2.0.0` | HTX 永续资金费率追踪：批量扫描全市场 HTX 永续当前资金费率、历史费率记录及下期预估费率 K 线。 | [TradeSkill](https://astraquant.tech/skills/htx-funding-rate.html) |
| [`htx-market-overview`](skills/htx-market-overview/SKILL.md) | `1.0.0` | HTX 全市场涨跌与板块扫描：扫描火币 HTX 现货与合约全市场领涨领跌榜、放量异动、市场宽度与板块轮动信号。 | [TradeSkill](https://astraquant.tech/skills/htx-market-overview.html) |
| [`htx-oi-tracker`](skills/htx-oi-tracker/SKILL.md) | `1.0.0` | HTX 合约持仓量 (OI) 追踪：实时监测 HTX USDT-M 永续合约总持仓量快照与历史 OI 增仓飙升趋势。 | [TradeSkill](https://astraquant.tech/skills/htx-oi-tracker.html) |
| [`htx-liquidation-stream`](skills/htx-liquidation-stream/SKILL.md) | `1.0.0` | HTX 合约强平爆仓流监控：查询 HTX 永续近期强平爆仓单，捕捉多空踩踏挤压（Squeeze）与流动性密集区。 | [TradeSkill](https://astraquant.tech/skills/htx-liquidation-stream.html) |
| [`htx-elite-positioning`](skills/htx-elite-positioning/SKILL.md) | `1.0.0` | HTX 大户多空持仓比：追踪 HTX 精英交易员按账户数与按持仓量统计的多空比例，识别头部资金风向。 | [TradeSkill](https://astraquant.tech/skills/htx-elite-positioning.html) |
| [`htx-mark-price`](skills/htx-mark-price/SKILL.md) | `1.0.0` | HTX 标记价格与期现基差：拉取 HTX 永续标记价格、溢价指数与基差 K 线序列，用于强平保护与套利定价参考。 | [TradeSkill](https://astraquant.tech/skills/htx-mark-price.html) |
| [`htx-settlement`](skills/htx-settlement/SKILL.md) | `1.0.0` | HTX 合约交割与风险准备金：查看 HTX USDT-M 预估交割价、历史结算记录以及平台风险准备金余额走势。 | [TradeSkill](https://astraquant.tech/skills/htx-settlement.html) |
| [`htx-derivatives-analyst`](skills/htx-derivatives-analyst/SKILL.md) | `1.0.0` | HTX 衍生品多因子压力分析：融合资金费率、OI、精英多空比、爆仓数据与基差，输出多空挤压方向与拥挤度判断。 | [TradeSkill](https://astraquant.tech/skills/htx-derivatives-analyst.html) |
| [`htx-sentiment-analyst`](skills/htx-sentiment-analyst/SKILL.md) | `1.0.0` | HTX 市场情绪与拥挤度分析：结合恐慌贪婪指数、大户持仓与全市场涨跌分布，生成量化的市场情绪诊断结论。 | [TradeSkill](https://astraquant.tech/skills/htx-sentiment-analyst.html) |
| [`htx-technical-analysis`](skills/htx-technical-analysis/SKILL.md) (`--skill htx/technical-analysis`) | `3.0.0` | HTX 本地技术指标与形态引擎：在本地计算 51 种技术指标、12 种 K 线形态、5 大 BTC 周期指标并自动检测量价背离。 | [TradeSkill](https://astraquant.tech/skills/htx-technical-analysis.html) |
| [`htx-ta-master`](skills/htx-ta-master/SKILL.md) (`--skill htx/ta-master`) | `1.0.0` | HTX 三柱加权技术评分大师：按价量 50% + 衍生品 30% + 周期 20% 权重输出 0–100 综合技术评分与区间策略解读。 | [TradeSkill](https://astraquant.tech/skills/htx-ta-master.html) |

</details>

<details>
<summary><strong>抹茶 MEXC（<code>mexc</code>）— 16 个可直装技能 · 插件包 <code>mexc-skills</code></strong></summary>

| 技能目录（含 `npx --skill` 名称） | 版本 | 说明 | 详情页 |
|---|---|---|---|
| [`mexc-setup`](skills/mexc-setup/SKILL.md) | `latest` | MEXC CLI 安装与初始化：安装升级 @mexc-ai/cli、运行健康检查、配置 API Key 档案与可选 MCP 注册。 | [TradeSkill](https://astraquant.tech/skills/mexc-setup.html) |
| [`mexc-auth`](skills/mexc-auth/SKILL.md) | `latest` | MEXC CLI API Key 认证引导：指引在本地安全配置及修复 MEXC OpenAPI 签名凭据与身份 Profile。 | [TradeSkill](https://astraquant.tech/skills/mexc-auth.html) |
| [`mexc-spot-market`](skills/mexc-spot-market/SKILL.md) (`--skill mexc-spot-marketv2`) | `latest` | MEXC 现货实时行情 (V2)：免密查询抹茶 MEXC 全市场交易对清单、实时行情 Ticker、新币信息与风险提示。 | [TradeSkill](https://astraquant.tech/skills/mexc-spot-market.html) |
| [`mexc-spot-kline`](skills/mexc-spot-kline/SKILL.md) | `latest` | MEXC 现货 K 线历史数据：免密拉取 MEXC 现货多周期蜡烛图 K 线数据，支持查询最早可回溯时间窗口。 | [TradeSkill](https://astraquant.tech/skills/mexc-spot-kline.html) |
| [`mexc-spot-trade`](skills/mexc-spot-trade/SKILL.md) | `latest` | MEXC 现货下单与止盈止损：支持 MEXC 现货限价/市价委托（含附加 TP/SL）、撤单、只读模拟演练及成交明细查询。 | [TradeSkill](https://astraquant.tech/skills/mexc-spot-trade.html) |
| [`mexc-spot-account`](skills/mexc-spot-account/SKILL.md) | `latest` | MEXC 现货实时成交推送：通过签名 WebSocket 订阅个人 MEXC 现货账户的最新成交实时推送与余额变动。 | [TradeSkill](https://astraquant.tech/skills/mexc-spot-account.html) |
| [`mexc-spot-asset`](skills/mexc-spot-asset/SKILL.md) | `latest` | MEXC 全账户资产概览：汇总 MEXC 现货、合约、OTC 与策略各子账户余额与资产明细统计。 | [TradeSkill](https://astraquant.tech/skills/mexc-spot-asset.html) |
| [`mexc-spot-convert`](skills/mexc-spot-convert/SKILL.md) | `latest` | MEXC 现货一键闪兑：查询可闪兑资产并按锁定报价零滑点将一种代币即时兑换为另一种代币。 | [TradeSkill](https://astraquant.tech/skills/mexc-spot-convert.html) |
| [`mexc-spot-grid`](skills/mexc-spot-grid/SKILL.md) | `latest` | MEXC AI 现货网格机器人：查询 MEXC AI 推荐的现货网格参数，创建、监控并终止区间自动化低买高卖策略。 | [TradeSkill](https://astraquant.tech/skills/mexc-spot-grid.html) |
| [`mexc-spot-dca`](skills/mexc-spot-dca/SKILL.md) | `latest` | MEXC 现货自动定投 (DCA)：查看支持定投的交易对与历史盈亏收益，全自动管理 MEXC 现货定投计划。 | [TradeSkill](https://astraquant.tech/skills/mexc-spot-dca.html) |
| [`mexc-contract-market`](skills/mexc-contract-market/SKILL.md) | `latest` | MEXC 永续合约公开行情：免密查询 MEXC 合约规格、合理/指数价格、资金费率、深度盘口与 24h 行情统计。 | [TradeSkill](https://astraquant.tech/skills/mexc-contract-market.html) |
| [`mexc-contract-trade`](skills/mexc-contract-trade/SKILL.md) | `latest` | MEXC 永续合约下单：支持 MEXC 合约限价/市价下单、计划委托、止盈止损参数设定与批量撤改单。 | [TradeSkill](https://astraquant.tech/skills/mexc-contract-trade.html) |
| [`mexc-contract-account`](skills/mexc-contract-account/SKILL.md) | `latest` | MEXC 合约账户与划转记录：查询 MEXC 合约账户权益快照、持仓风险、资金划转流水与成交统计。 | [TradeSkill](https://astraquant.tech/skills/mexc-contract-account.html) |
| [`mexc-earn-flexible`](skills/mexc-earn-flexible/SKILL.md) (`--skill mexc-financial-openapi-flexible`) | `latest` | MEXC 活期理财与自动复利：管理 MEXC 活期理财产品的自动质押开关、利息收益与活期余额查询。 | [TradeSkill](https://astraquant.tech/skills/mexc-earn-flexible.html) |
| [`mexc-earn-fixed`](skills/mexc-earn-fixed/SKILL.md) (`--skill mexc-financial-openapi-fixed`) | `latest` | MEXC 定期理财查询：查询 MEXC 定期理财产品列表、锁仓期限利率、申购订单与收益明细。 | [TradeSkill](https://astraquant.tech/skills/mexc-earn-fixed.html) |
| [`mexc-ws`](skills/mexc-ws/SKILL.md) | `latest` | MEXC WebSocket 执行模型：定义 MEXC CLI 全部 WebSocket 实时订阅流的行数限制、JSON Lines 输出与 Dry-Run 规范。 | [TradeSkill](https://astraquant.tech/skills/mexc-ws.html) |

</details>

<details>
<summary><strong>库币 KuCoin（<code>kucoin</code>）— 7 个可直装技能 · 插件包 <code>kucoin-skills</code></strong></summary>

| 技能目录（含 `npx --skill` 名称） | 版本 | 说明 | 详情页 |
|---|---|---|---|
| [`kucoin-spot`](skills/kucoin-spot/SKILL.md) (`--skill spot`) | `1.0.0` | KuCoin 现货行情与订单查询：查询库币 KuCoin 现货实时行情、高频委托单、止损单及 OCO 挂单历史（当前仅支持只读 GET 接口）。 | [TradeSkill](https://astraquant.tech/skills/kucoin-spot.html) |
| [`kucoin-futures-trading`](skills/kucoin-futures-trading/SKILL.md) (`--skill futures-trading`) | `1.0.0` | KuCoin 合约持仓与费率查询：查询 KuCoin Futures 合约行情、当前持仓风险、委托列表与历史资金费率明细（只读 GET）。 | [TradeSkill](https://astraquant.tech/skills/kucoin-futures-trading.html) |
| [`kucoin-margin-trading`](skills/kucoin-margin-trading/SKILL.md) (`--skill margin-trading`) | `1.0.0` | KuCoin 杠杆借贷与风控查询：查看 KuCoin 全仓/逐仓杠杆行情、借还币流水、借贷利率及风控限额信息（只读 GET）。 | [TradeSkill](https://astraquant.tech/skills/kucoin-margin-trading.html) |
| [`kucoin-assets`](skills/kucoin-assets/SKILL.md) (`--skill assets`) | `1.0.0` | KuCoin 资产账单与费率：汇总 KuCoin 多账户余额、账单流水、充提记录、子账户明细及账户当前手续费等级。 | [TradeSkill](https://astraquant.tech/skills/kucoin-assets.html) |
| [`kucoin-convert`](skills/kucoin-convert/SKILL.md) (`--skill convert`) | `1.0.0` | KuCoin 闪兑询价与记录：获取 KuCoin Convert 即时兑价估算，查询历史闪兑订单详情与兑换状态。 | [TradeSkill](https://astraquant.tech/skills/kucoin-convert.html) |
| [`kucoin-earn`](skills/kucoin-earn/SKILL.md) (`--skill earn`) | `1.0.0` | KuCoin 赚币产品查询：浏览 KuCoin Simple Earn 活期/质押与结构化理财产品收益率及个人申购记录。 | [TradeSkill](https://astraquant.tech/skills/kucoin-earn.html) |
| [`kucoin-broker`](skills/kucoin-broker/SKILL.md) (`--skill broker`) | `1.0.0` | KuCoin 经纪商与返佣数据：查询 KuCoin Broker 邀请关系、佣金返还明细、Broker Pro 客户及渠道统计（只读 GET）。 | [TradeSkill](https://astraquant.tech/skills/kucoin-broker.html) |

</details>

<details>
<summary><strong>Crypto.com Crypto.com（<code>cryptocom</code>）— 2 个可直装技能 · 插件包 <code>cryptocom-skills</code></strong></summary>

| 技能目录（含 `npx --skill` 名称） | 版本 | 说明 | 详情页 |
|---|---|---|---|
| [`cryptocom-exchange`](skills/cryptocom-exchange/SKILL.md) (`--skill crypto-com-exchange`) | `2.0.0` | Crypto.com 交易所 CLI (cdcx)：通过 cdcx CLI 操作 Crypto.com Exchange：现货/衍生品/OCO 下单、模拟盘演练与四级安全确认。 | [TradeSkill](https://astraquant.tech/skills/cryptocom-exchange.html) |
| [`cryptocom-app`](skills/cryptocom-app/SKILL.md) (`--skill crypto-com-app`) | `1.0.2` | Crypto.com App 交易与法币：调用 Crypto.com App API 完成市价买卖、代币兑换、法币银行卡出入金及每周限额查询。 | [TradeSkill](https://astraquant.tech/skills/cryptocom-app.html) |

</details>

<details>
<summary><strong>Uniswap Uniswap（<code>uniswap</code>）— 8 个可直装技能 · 插件包 <code>uniswap-skills</code></strong></summary>

| 技能目录（含 `npx --skill` 名称） | 版本 | 说明 | 详情页 |
|---|---|---|---|
| [`uniswap-swap-planner`](skills/uniswap-swap-planner/SKILL.md) (`--skill swap-planner`) | `latest` | Uniswap 链上 Swap 交易规划：在多条 EVM 链上协助代币发现、路径比价、滑点保护以及构建安全的 Uniswap 兑换交易。 | [TradeSkill](https://astraquant.tech/skills/uniswap-swap-planner.html) |
| [`uniswap-liquidity-planner`](skills/uniswap-liquidity-planner/SKILL.md) (`--skill liquidity-planner`) | `0.2.0` | Uniswap v3/v4 做市 LP 规划：分析池子费率层、价格区间范围与无常损失敞口，辅助生成 v3 / v4 集中流动性建仓方案。 | [TradeSkill](https://astraquant.tech/skills/uniswap-liquidity-planner.html) |
| [`uniswap-swap-integration`](skills/uniswap-swap-integration/SKILL.md) (`--skill swap-integration`) | `1.6.0` | Uniswap Trading API 集成指南：将 Uniswap Trading API 与通用路由集成到应用、前端或自动化交易脚本中的官方规范。 | [TradeSkill](https://astraquant.tech/skills/uniswap-swap-integration.html) |
| [`uniswap-dca-bot`](skills/uniswap-dca-bot/SKILL.md) (`--skill dca-bot`) | `0.2.0` | Uniswap 链上定投机器人：按固定时间周期或回调价格条件自动在链上定投目标代币的自动化策略技能。 | [TradeSkill](https://astraquant.tech/skills/uniswap-dca-bot.html) |
| [`uniswap-index-bot`](skills/uniswap-index-bot/SKILL.md) (`--skill index-bot`) | `0.2.0` | Uniswap 一篮子指数再平衡：按目标权重买入多资产篮子并定期在链上自动再平衡，适合构建链上指数组合。 | [TradeSkill](https://astraquant.tech/skills/uniswap-index-bot.html) |
| [`uniswap-copy-trade`](skills/uniswap-copy-trade/SKILL.md) (`--skill copy-trade`) | `0.2.0` | Uniswap 链上钱包镜像跟单：追踪指定 EVM 聪明钱地址在 DEX 上的建仓减仓动态并按比例镜像复刻链上交易。 | [TradeSkill](https://astraquant.tech/skills/uniswap-copy-trade.html) |
| [`uniswap-v4-hook-generator`](skills/uniswap-v4-hook-generator/SKILL.md) (`--skill v4-hook-generator`) | `1.0.0` | Uniswap v4 Hook 合约生成器：结合 OpenZeppelin 规范生成支持动态费率、限价单、防 MEV 与定制曲线的 v4 Hook 合约。 | [TradeSkill](https://astraquant.tech/skills/uniswap-v4-hook-generator.html) |
| [`uniswap-v4-security-foundations`](skills/uniswap-v4-security-foundations/SKILL.md) (`--skill v4-security-foundations`) | `1.1.0` | Uniswap v4 Hook 安全审计：梳理 Uniswap v4 PoolManager 回调权限、重入与滑点攻击面，保障自定义 Hook 安全性。 | [TradeSkill](https://astraquant.tech/skills/uniswap-v4-security-foundations.html) |

</details>

<details>
<summary><strong>Jupiter Jupiter（<code>jupiter</code>）— 4 个可直装技能 · 插件包 <code>jupiter-skills</code></strong></summary>

| 技能目录（含 `npx --skill` 名称） | 版本 | 说明 | 详情页 |
|---|---|---|---|
| [`jupiter-integrate`](skills/jupiter-integrate/SKILL.md) (`--skill integrating-jupiter`) | `1.2.0` | Jupiter Solana 全套 API 集成：全面集成 Jupiter Swap v2、Perps 永续、限价单、定投、Lend 与代币价格组合接口。 | [TradeSkill](https://astraquant.tech/skills/jupiter-integrate.html) |
| [`jupiter-lend`](skills/jupiter-lend/SKILL.md) | `0.1.3` | Jupiter Lend 借贷与金库 SDK：通过只读与写入 SDK 查询 Jupiter Lend 流动性池、jlTokens 收益及金库借贷头寸操作。 | [TradeSkill](https://astraquant.tech/skills/jupiter-lend.html) |
| [`jupiter-swap-migration`](skills/jupiter-swap-migration/SKILL.md) | `1.1.0` | Jupiter Swap API v2 迁移：将原有 Jupiter Metis v1 或 Ultra 接口迁移至最新 Swap v2 统一构建接口与路由端点。 | [TradeSkill](https://astraquant.tech/skills/jupiter-swap-migration.html) |
| [`jupiter-vrfd`](skills/jupiter-vrfd/SKILL.md) | `1.0.1` | Jupiter VRFD 代币认证工作流：路由引导 Solana 代币提交 Jupiter VRFD 资质审核、快速验证资格及元数据更新。 | [TradeSkill](https://astraquant.tech/skills/jupiter-vrfd.html) |

</details>


### 仅官方源安装技能（62 个）

对于未提供可再分发许可或依赖上游 CLI 生成器（如 Gate、Binance Web3、BingX、BitMart）的技能，仓库索引指向其官方上游源与安装指南：

- **欧易 OKX**（5 个）：使用 OKX OnchainOS / Trade CLI 安装 — [OKX 专区](https://astraquant.tech/exchanges/okx.html) · [官方仓库](https://github.com/okx/agent-skills)
- **Gate Gate**（20 个）：使用 Gate CLI / MCP 官方生成器安装 — [Gate 专区](https://astraquant.tech/exchanges/gate.html) · [官方仓库](https://github.com/gate/gate-skills)
- **币安 Binance**（18 个）：从 binance/binance-skills-hub 安装 — [Binance 专区](https://astraquant.tech/exchanges/binance.html) · [官方仓库](https://github.com/binance/binance-skills-hub)
- **Bybit Bybit**（1 个）：从 bybit-exchange/trading-cli 安装 — [Bybit 专区](https://astraquant.tech/exchanges/bybit.html) · [官方仓库](https://github.com/bybit-exchange/skills)
- **Coinbase Coinbase**（1 个）：coinbase/agents 总入口路由 — [Coinbase 专区](https://astraquant.tech/exchanges/coinbase.html) · [官方仓库](https://github.com/coinbase/agents)
- **BingX BingX**（14 个）：从 BingX-API/api-ai-skills 安装 — [BingX 专区](https://astraquant.tech/exchanges/bingx.html) · [官方仓库](https://github.com/BingX-API/api-ai-skills)
- **BitMart BitMart**（3 个）：从 bitmartexchange/bitmart-skills 安装 — [BitMart 专区](https://astraquant.tech/exchanges/bitmart.html) · [官方仓库](https://github.com/bitmartexchange/bitmart-skills)

---

## 精选交易教程与交易所对比

完整中文教程与横向评测见 [astraquant.tech/guides.html](https://astraquant.tech/guides.html)：

- [OKX vs 币安 vs Gate AI 交易技能对比：CLI、免密行情与返佣怎么选](https://astraquant.tech/guides/okx-vs-binance-vs-gate-ai-skills.html) — 深度对比欧易 OKX（18 技能）、币安 Binance（21 技能）与 Gate（20 技能）官方 AI Agent 能力、CLI 架构、免密行情与 20% 手续费返佣。
- [Claude Code 加密货币交易教程：1 分钟安装交易所 Skill 并模拟试跑](https://astraquant.tech/guides/claude-code-crypto-trading-tutorial.html) — 手把手教你在 Claude Code 中通过一句提示词自动安装 ~/.claude/skills 加密货币交易技能，配置只读行情、模拟盘与安全防呆护栏。
- [Cursor / Codex / Windsurf 接入 AI 交易技能：多客户端目录与打包部署](https://astraquant.tech/guides/cursor-codex-windsurf-trading-skills.html) — 一次搞懂 Cursor (~/.cursor/skills)、Codex (~/.agents/skills)、Windsurf 与 OpenCode 的技能目录差异，如何批量组合打包并跨 IDE 同步。
- [免 API Key 的加密货币 AI 行情与投研技能盘点（7 大交易所零凭证直连）](https://astraquant.tech/guides/keyless-crypto-market-data-skills.html) — 盘点 OKX、Kraken、HTX、MEXC、币安、Gate 与 BitMart 无需配置交易所私钥或 API Key 即可免费运行的实时盘口、K 线、情绪与风控技能。
- [AI 高频与量化交易返佣省钱指南：OKX/Gate/币安/Bitget 费率对比与防风控](https://astraquant.tech/guides/exchange-fee-rebates-for-ai-traders.html) — 对比 Gate 20%、欧易 OKX 20%、币安 Binance 20% 与 Bitget 15% 官方邀请返佣政策，算清高频 Bot 手续费节省空间，并掌握子账户/独立小号隔离防风控做法。
- [OKX 官方 Agent Skills 全套教程：Trade CLI 1.5.1 与 OnchainOS 实战](https://astraquant.tech/guides/okx-agent-trade-cli-tutorial.html) — 详解 @okx_ai/okx-trade-cli 与 onchainos CLI 安装配置、免密看盘、模拟盘下单、网格 Bot、以及官方 20% 返佣与原版切换方法。
- [币安 Binance 官方 21 个 AI 技能全解析：CEX 下单、P2P 与 Web3 代币审计](https://astraquant.tech/guides/binance-cex-web3-ai-skills-guide.html) — 全面拆解币安官方 Binance Skills Hub 共 21 个 CEX 与 Web3 技能：包含现货合约、C2C P2P、市场热点排行、聪明钱追踪与新币合约安全审计。
- [Gate vs Bitget AI 交易与 Bot 机器人指南：投研风控 vs UTA 统一账户](https://astraquant.tech/guides/gate-bitget-ai-trading-bots-guide.html) — 对比 Gate 官方 CEX/Bot/情报风控 20 技能矩阵与 Bitget UTA v3 (bgc CLI) + Bitget Wallet RWA 链上套件，附 Gate 20% 与 Bitget 15% 返佣配置说明。
- [Coinbase vs Kraken vs Bybit AI 技能对比：OAuth MCP、Rust 模拟盘与 V5 CLI](https://astraquant.tech/guides/coinbase-kraken-bybit-ai-agent-comparison.html) — 深入比较 Coinbase（CLI + 托管 OAuth MCP + x402）、Kraken（Rust 单二进制 + 内置免密 Paper 模拟盘 18 技能）与 Bybit V5 Trading Skill 适用场景。
- [链上 DEX AI 交易指南：Uniswap vs Jupiter vs OnchainOS 多链技能对比](https://astraquant.tech/guides/dex-ai-trading-uniswap-vs-jupiter.html) — 深度对比 Uniswap Labs（8 个 Swap/v4 LP/DCA/Hook 安全审计技能）、Jupiter（Solana Swap v2/Lend/Perps）与 OKX OnchainOS 链上技能使用边界与私钥安全。

---

## 官方交易所手续费返佣专区

更多细则与费率说明见 [astraquant.tech/rebates.html](https://astraquant.tech/rebates.html)：

| 交易所 | 邀请码 | 返佣比例 | 官方注册入口 |
|---|---|---|---|
| **OKX** | `48039151` | **20%** | [官方海外链接](https://www.okx.com/join/48039151) · [官方备用链接](https://www.mitxcqvwnhj.com/join/48039151) |
| **Gate** | `MCHDBKYF` | **20%** | [官方海外链接](https://www.gate.com/share/MCHDBKYF) · [官方备用链接](https://www.gatewebsite.com/share/MCHDBKYF) |
| **Binance** | `1142479220` | **20%** | [官方海外链接](https://accounts.binance.com/register?ref=1142479220) · [官方备用链接](https://www.bsmkweb.net/register?ref=1142479220) |
| **Bitget** | `DY6CJDUY` | **15%** | [官方海外链接](https://www.bitget.com/referral/register?clacCode=DY6CJDUY&source=events&utmSource=PremierInviter) · [官方备用链接](https://www.bitget.ninja/zh-CN/referral/register?clacCode=DY6CJDUY&from=%2Fzh-CN%2Factivity%2Freferral-all-program&source=events&utmSource=PremierInviter) |

---

## 安全边界、归因透明与 CI 校验

1. **凭证仅留存在本地**：TradeSkill 不托管也不经过任何交易所 API Key、Passphrase 或钱包私钥。
2. **先行情/模拟盘，后实盘**：建议优先运行免密行情技能（如 `okx-cex-market`、`kraken-market-intel`、`htx-market-overview`）或交易所内置模拟盘验证工作流。
3. **OKX AI Builder 订单归因透明披露**：仅 `skills/okx-cex-trade` 与 `skills/okx-cex-bot` 按照 [OKX AI Builder 接入规范](https://www.okx.com/zh-hans/help/ai-builder-program-integration-guide) 保留 `--aiBuilderCode` 订单归因参数（[OKX 官方原仓地址](https://github.com/okx/agent-skills)）；其余 92 个可直装技能均为未改动的上游 MIT / Apache-2.0 原版快照。
4. **自动 CI 校验**：每次推送都会触发 [`.github/workflows/validate.yml`](.github/workflows/validate.yml)，自动校验全部 95 个技能的 `SKILL.md` Frontmatter、许可证文件与插件清单完整性。

# SkillHub attribution mapping

- Upstream skill snapshot: [3cff92b6a5](https://github.com/okx/agent-skills/tree/3cff92b6a5ced87422fbfe0ce4d7237c026589f9) (MIT).
- Local attribution argument: `--aiBuilderCode 6e2191f027c6SUDE`. The tested official Trade CLI version is `1.5.1`.
- The flag is forwarded as the OKX API order `tag`. Actual eligibility depends on the corresponding OKX project/code activation, eligible fills and site rules. No certification, rebate rate, or user discount is implied.
- No credential, trade, OAuth or account flow runs on the SkillHub website.
- Official references: [Builder integration guide](https://www.okx.com/zh-hans/help/ai-builder-program-integration-guide) · [Broker rules](https://www.okx.com/zh-hans/help/introduction-of-rules-on-okx-brokers).

## Supported CLI command paths

- `okx bot dca create`
- `okx bot grid create`
- `okx bot recurring create`
- `okx bot smart-portfolio create`

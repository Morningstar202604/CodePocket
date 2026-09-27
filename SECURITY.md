# 安全策略（Security Policy）

## 报告漏洞

如果发现安全漏洞，请**不要**在公开 Issue 中披露细节，以免被恶意利用。请通过以下方式私下联系维护者：

- 在 [仓库所有者主页](https://gitcode.com/badhope) 获取联系方式；
- 或在 Issue 区先声明"发现安全问题，请求私下沟通渠道"。

我们会尽快响应、确认并修复，修复后再公开披露细节。

## 支持的版本

仅最新发布版本（`main` 分支最新提交）接受安全修复。

## 已知的安全边界（诚实标注）

- **离线定位**：App 默认完全离线，代码与数据只存于设备本地；
- **AI 助手（BYOK）**：仅当你主动配置端点并调用时，相关文件内容才会发送到你自配的端点；不配置则零联网；
- **凭据保护**：请勿将任何 API Key / token 提交进仓库（`.gitignore` 已排除 `local.properties` 等敏感文件）；
- **标准库随包**：内置 CPython 与标准库来自官方上游构建，如有上游安全公告，会在 [CHANGELOG](CHANGELOG.md) 中记录升级情况。

## 依赖安全

- CPython 3.13.9（官方源码构建，PSF License）；
- SoraEditor（LGPL-2.1，动态链接）、JGit（纯 Java）；
- 依赖版本升级均记录于 [NOTICE.md](NOTICE.md) 与 [CHANGELOG.md](CHANGELOG.md)。

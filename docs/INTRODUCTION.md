# CodePocket「口袋码」—— 项目介绍

> 一句话：**真正离线的安卓 Python IDE，手机上的现代开发环境，装完就能跑。**

---

## 它是什么

CodePocket 是一款完全离线的安卓 Python IDE。我们把 CPython 3.13 用 NDK 交叉编译成 ARM64 原生库，连同标准库一起打包进 APK——用户安装后打开就能写代码、跑代码，全程不需要联网、不需要下载任何运行时、不需要付费订阅、没有任何广告。

**核心承诺：装完即离线。** 地铁上、课堂上、没有信号的山里，只要手机在手，代码就能跑。

---

## 为什么值得用

### 对学习者
- 打开即用的 Python 环境，不用配置任何东西；
- 20+ 高频错误的"人话翻译"，报错不再是天书；
- 内置模板、命令面板、AI 助手（可选），从"照着写"到"自己写"一路顺畅。

### 对脚本写手 / 极客
- 原生 ARM64 性能，跑计算脚本不卡壳；
- 真文件系统：脚本直接读写手机私有目录，cwd 就是项目目录；
- 标准库全量：math / json / socket / ssl / sqlite3 / ctypes 等 C 扩展随包可用；
- JGit 离线 Git：init / commit / push / pull 都能在手机上完成。

### 对所有人
- **开源**（Apache-2.0）：代码透明，可审查、可 fork、可贡献；
- **无广告无内购**：没有会员墙，功能不藏着掖着；
- **隐私友好**：代码和数据都在设备本地，AI 助手由用户自配端点（BYOK）。

---

## 它能做什么

| 场景 | 说明 |
|---|---|
| 写代码 | 多文件 Tab、文件树、语法高亮（18 种语言 TextMate）、静态补全、查找替换、全局搜索 |
| 跑代码 | 原生 CPython 3.13、流式输出、`input()` 交互、死循环超时中断、命令行参数 |
| 管项目 | 多项目切换、4 个 Python 模板、SAF 导入导出、离线 Git |
| 看结果 | Markdown / HTML 分屏预览、PNG 图片直接查看、输出复制与分享 |
| 提效率 | 命令面板 ⌘K、AI 助手（BYOK）、会话恢复、崩溃日志本地留存 |

---

## 技术底色

- **引擎**：CPython 3.13.9（官方 PEP 738 Android 支持）交叉编译为 arm64 原生库；
- **桥接**：自写 JNI 桥（`pybridge.c`，约 350 行 C），stdin/stdout/stderr 三路桥接，无死锁、中文不乱码；
- **界面**：Kotlin 2.0 + Jetpack Compose + Sora Editor；
- **构建**：零外部申请依赖——NDK（Google 官方）+ CPython 源码（GitHub）+ BeeWare 预编译依赖，全部免费公开。

---

## 诚实的能力边界

- Python 运行：✅ 完整（原生 CPython 3.13，arm64）；
- Java 运行：❌ 尚未集成 JVM 运行时（保留编辑高亮）；
- numpy / pandas / matplotlib：⚠️ **未预装**，离线导入第三方 wheel 的能力后续开放；
- pip 联网装包：❌ 离线定位，不提供在线包安装。

---

## 一起建设

CodePocket 是开源项目，欢迎一切形式的参与：提交 Issue、改进文档、修 bug、加功能、帮忙测试。

- 贡献指南：[CONTRIBUTING.md](../CONTRIBUTING.md)
- 路线图：[ROADMAP.md](ROADMAP.md)
- 行为准则：[CODE_OF_CONDUCT.md](../CODE_OF_CONDUCT.md)

---

*CodePocket「口袋码」——把 IDE 装进口袋，离线也能写代码。*

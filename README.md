<div align="center">

# 📱 CodePocket · 口袋码

**真正离线的安卓 Python IDE — 手机上的现代开发环境，装完就能跑**

原生 Python 运行时（CPython 3.13 交叉编译，含标准库 C 扩展）随 APK 打包，零下载、零网络、零广告、零订阅。

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg?style=flat-square)](LICENSE)
[![Platform](https://img.shields.io/badge/Android-8.0%2B-green?style=flat-square)](https://developer.android.com)
[![Kotlin](https://img.shields.io/badge/Kotlin%202.0%20%2B%20Compose-7F52FF?style=flat-square)](https://kotlinlang.org)
[![Runtime](https://img.shields.io/badge/%E8%BF%90%E8%A1%8C%E6%97%B6-100%25%20%E9%9A%8F%E5%8C%85-orange?style=flat-square)]()
[![Ads](https://img.shields.io/badge/%E5%B9%BF%E5%91%8A-0%20%E6%9D%A1-red?style=flat-square)]()

**[下载 APK](https://gitcode.com/badhope/CodePocket/releases)** · **[官网](https://x33834.github.io/CodePocket/)** · **[Gitee 镜像](https://gitee.com/badhope/CodePocket)**

> 把 IDE 装进口袋，离线也能写代码。

</div>

---

## ✨ 为什么是 CodePocket

| | Termux | Pydroid 3 | Acode | Spck | **CodePocket** |
|---|:---:|:---:|:---:|:---:|:---:|
| 装完即离线 | ⚠️ 要装包 | ⚠️ 部分 | ❌ 联网 | ❌ 联网 | ✅ **运行时随包** |
| 现代 IDE 界面 | ❌ 黑框 | ⚠️ 旧 | ✅ | ✅ | ✅ |
| 多文件 Tab / 查找替换 | ❌ | ✅ | ✅ | ✅ | ✅ |
| Git 离线集成 | ✅ | ❌ | ✅ | ✅ | ✅ **JGit** |
| 原生性能 | ✅ | ✅ | — | — | ✅ **原生 ARM64** |
| AI 助手（BYOK） | ❌ | ❌ | ✅ 云端 | ✅ 云端 | ✅ **自配端点** |
| 开源无广告 | ✅ GPL | ❌ 付费 | ⚠️ 广告 | ⚠️ 内购 | ✅ **Apache-2.0** |

> 我们的定位：**开源 + 无广告 + 装完即离线 + 原生性能**。

---

## 🏗 架构

```
┌─────────────────────────────────────────────┐
│  Compose UI 层                               │
│  文件树 · 编辑器(Sora) · 输出面板 · 命令面板    │
└──────────────────┬──────────────────────────┘
                   │ JNI（jobject 回调）
┌──────────────────▼──────────────────────────┐
│  NativeEngine（Kotlin）+ pybridge.c（JNI 桥） │
│  CPython 3.13 交叉编译为 arm64 原生库        │
│  流式 stdout/stderr · 超时中断 · stdin 交互   │
└──────────────────┬──────────────────────────┘
                   │ dlopen + sys.path
┌──────────────────▼──────────────────────────┐
│  jniLibs/arm64-v8a（随 APK）                 │
│  libpython3.13.so · libpybridge.so · C 扩展  │
│  assets/python-stdlib.zip（纯 Python 标准库） │
└─────────────────────────────────────────────┘
```

**核心取舍**：不自造终端模拟器，不依赖外置原生工具链。用 NDK 把 CPython 3.13 交叉编译成 arm64 原生库，随 APK 打包——装完即离线。当前只集成 Python 运行时；Java（JVM）尚未集成，仅保留编辑高亮。

---

## 🎯 功能一览

### 写代码
- **多文件 Tab** · **文件树**（新建/重命名/删除，长按操作）
- **Sora Editor** 代码编辑器 + 18 种语言 TextMate 语法高亮
- **静态补全**：Python 关键字/内置函数 + 当前文件符号提取（零进程开销）
- **查找替换**（计数跳转）· **全局搜索**（跨文件）
- **快捷符号栏** 26 键 · **双指缩放字号** · **自动闭合括号** · **自动换行** · **行号开关**
- **6 套编辑器主题**（Darcula / Monokai / 明日蓝 / Solarized…）

### 跑代码
- **原生 CPython 3.13（arm64）**，标准库全量（纯 Python 部分 + C 扩展）
- **math / json / random / datetime / socket / ssl / sqlite3 / ctypes** 等 C 扩展随包
- **流式输出** · **`input()` 交互** · **方向键/Tab 软键盘**
- **死循环保护**（超时中断）· **前台服务保活**
- **友好报错翻译**（20+ 高频错误）
- 运行配置（命令行参数）· 脚本内 `__file__` 等标准属性可用

### 管项目
- **多项目切换**（长按删除）· **4 个 Python 模板**
- **JGit Git 集成**：init / commit / push / pull，纯 Java 离线
- **SAF 导入导出**（无需存储权限）
- **离线包管理**：查看内置模块 / 导入本地 .whl

### 看结果
- **Markdown / HTML 分屏实时预览**，防抖刷新
- **外部浏览器打开** HTML 文件
- **输出面板**：拖拽调高 / 复制全部 / 分享
- **三态主题**（跟随系统 / 浅色 / 深色）

### 提效
- **命令面板 ⌘K**：搜索一切动作 + 代码片段
- **AI 助手**（BYOK，OpenAI 兼容端点）：解释文件 / 修错 / 生成测试
- **会话恢复**：重启回到上次编辑现场
- **崩溃日志**写私有目录，离线可反馈

---

## 🚀 快速开始

```bash
# 1) 前置：JDK 17+、Android SDK（platforms;android-35、build-tools;34.0.0）
#    本地生成 local.properties：sdk.dir=/path/to/android-sdk

# 2) clone 后直接出包
./gradlew assembleDebug
adb install -r app/build/outputs/apk/debug/app-debug.apk

# 3) 手机上打开 App → 新建项目 → 写代码 → 点 ▶ 运行
```

原生运行时（`libpython3.13.so` + C 扩展 + 纯 Python 标准库 zip，约 100MB）已随仓库提供，构建完成后 **App 运行零网络**。

> 重新编译 `libpybridge.so` 需 NDK 27.3 与 CPython 3.13 交叉编译环境，见 `scripts/package_native.sh`。日常构建不需要——预编译产物已在 `app/src/main/jniLibs/`。

> `assets/python-stdlib.zip` 必须配置 `noCompress`（已配置），否则 AAPT 压缩后 CPython 无法加载标准库。

---

## 📦 随包内置的运行时

- **纯 Python 标准库**：`assets/python-stdlib.zip`（解压到应用私有目录后加入 `sys.path`）
- **C 扩展模块**：math、json、_random、_datetime、_socket、_ssl、_sqlite3、_ctypes、zlib、binascii 等（`jniLibs/arm64-v8a`）
- **第三方科学计算库（numpy / pandas / matplotlib / pillow）当前未预装**，`import numpy` 会提示缺少模块。离线安装第三方 wheel 的能力后续版本开放。

---

## 📚 文档

| 文档 | 说明 |
|---|---|
| [品牌方案](docs/BRANDING.md) | 命名、定位、口号、视觉建议 |
| [项目介绍](docs/INTRODUCTION.md) | 一页式介绍，适合官网/宣传 |
| [用户手册](docs/USER_GUIDE.md) | 安装、界面、运行、Git、AI 完整说明 |
| [技术架构](docs/ARCHITECTURE.md) | 引擎、JNI 桥、线程模型、目录结构 |
| [路线图](docs/ROADMAP.md) | 已实现 / 进行中 / 规划 |
| [宣传文案包](docs/PROMOTION.md) | 商店描述、发布公告、社媒文案，复制即用 |
| [常见问题](docs/FAQ.md) | FAQ |
| [贡献指南](CONTRIBUTING.md) | 如何参与开发 |
| [行为准则](CODE_OF_CONDUCT.md) | Contributor Covenant |
| [安全政策](SECURITY.md) | 漏洞上报流程 |

---

## 🧭 能力边界（诚实标注）

| 能力 | 状态 |
|---|---|
| Python 运行 | ✅ 完整（原生 CPython 3.13，arm64） |
| Java 运行 | ❌ 尚未集成 JVM 运行时（保留编辑高亮） |
| 性能 | ✅ 原生执行，无 WASM 沙箱开销 |
| 第三方科学计算库 | ⚠️ numpy/pandas/matplotlib 未预装，离线导入后续开放 |
| pip 联网装包 | ❌ 离线定位，额外库需手动导入 wheel |

---

## 🤝 贡献

欢迎一切形式的贡献：提交 Issue、改进文档、修 bug、加功能。

贡献前跑 `python3 tools/selfcheck.py`（0 错误再提交），详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

---

## 📄 许可证

[Apache License 2.0](LICENSE) · 第三方组件声明见 [NOTICE.md](NOTICE.md)

---

*CodePocket「口袋码」——把 IDE 装进口袋，离线也能写代码。*

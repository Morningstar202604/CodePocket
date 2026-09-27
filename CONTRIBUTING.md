# 贡献指南（Contributing）

欢迎来到 CodePocket「口袋码」！无论是修 bug、加功能、改文档，还是帮忙测试，都非常欢迎。

---

## 一、快速路径

| 你想做什么 | 怎么做 |
|---|---|
| 反馈 bug / 提建议 | 开 [Issue](https://gitcode.com/badhope/CodePocket/issues)，写清现象、步骤、期望 |
| 改文档 | 直接提 PR，改动要小而清晰 |
| 修 bug / 加功能 | 先开 Issue 说明方案 → 认领 → 开发 → PR |
| 只想围观 | 点 Star、参与讨论，都是支持 |

---

## 二、开发环境

```bash
# 前置
#   JDK 17+
#   Android SDK：platforms;android-35、build-tools;34.0.0
#   local.properties：sdk.dir=/path/to/android-sdk

git clone https://gitcode.com/badhope/CodePocket.git
cd CodePocket
./gradlew assembleDebug
```

> 日常改 Kotlin/资源不需要 NDK：`libpybridge.so` 等预编译产物已随仓库提供。
> 只有改 `app/src/main/cpp/pybridge.c` 时才需要 NDK 27.3 + CPython 3.13 交叉编译环境（`scripts/package_native.sh`）。

---

## 三、提交规范

### 提交前必须通过

```bash
python3 tools/selfcheck.py        # 静态自检：0 错误
./gradlew compileDebugKotlin      # Kotlin 编译通过
```

### 提交信息格式

```
type(scope): 一句话描述

- 要点 1
- 要点 2
```

- `type`：`fix`（修 bug）/ `feat`（新功能）/ `docs`（文档）/ `refactor`（重构）/ `chore`（杂项）
- `scope`：`engine`（引擎）/ `ui`（界面）/ `build`（构建）/ `docs`（文档）等
- 示例：`fix(engine): 修复脚本引用 __file__ 时 NameError`

### PR 要求

- 标题清晰，描述动机 + 改动 + 验证方式；
- 每个 PR 只做一件事，避免夹带无关改动；
- 改动引擎（`pybridge.c` / `NativeEngine`）时，请在 PR 里说明真机/模拟器验证结果；
- 自检与编译全绿后再请求 review。

---

## 四、代码约定

- **Kotlin**：遵循官方风格；类/函数加简短 KDoc 说明意图；
- **C（pybridge.c）**：只使用 Python C API 公开接口；JNI 引用计数成对管理（New/Delete、Get/Release）；
- **资源与文案**：中文文案直接写中文（App 面向中文用户）；
- **防御性编程**：IO/网络/JNI 调用用 `runCatching` 或显式错误返回，不允许静默吞错。

---

## 五、测试

- **静态自检**：`python3 tools/selfcheck.py`（Kotlin 未用 import / 资源引用检查）；
- **构建**：`./gradlew assembleDebug`；
- **引擎冒烟（宿主模拟）**：改动 `pybridge.c` 后，可用宿主 CPython 模拟桥接路径做快速验证（中文输出、`input()`、错误路径）；
- **真机**：有真机/模拟器的同学请在 PR 里附验证截图或日志。

> 已知：`tools/test_suite.py` 仍驱动 Web 原型（Pyodide 时代遗留），尚未覆盖原生引擎；原生引擎的自动化冒烟测试在路线图中（见 [ROADMAP.md](docs/ROADMAP.md)）。

---

## 六、发布流程（维护者）

1. **定版本**：按语义化版本（SemVer）——修 Bug 升补丁位、新功能升次版本、破坏性改动升主版本；
2. **同步文档**：改代码的同时更新 README 与 [CHANGELOG.md](CHANGELOG.md)（Keep a Changelog 格式）；
3. **本地验证**：`python3 tools/selfcheck.py` + `./gradlew assembleDebug` 全绿才继续；
4. **合并**：以 PR 方式合入 `main`；
5. **打标签**：`git tag -a vX.Y.Z -m "vX.Y.Z"` 并推送；
6. **发布**：基于 tag 创建 Release，Notes 写清变更要点；
7. **部署**：确认站点/文档自动部署完成且可访问。

---

## 七、行为准则

参与即代表同意 [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)：尊重他人、对事不对人、共建友善社区。

---

*感谢每一个让 CodePocket 变得更好的人。*

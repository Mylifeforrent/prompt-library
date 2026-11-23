# 布局设计 Skill 推荐（不依赖 MCP）

确实有一些不依赖 MCP、纯粹以 Skill 形态工作的布局设计工具，它们在易用性和专注度上各有特色。这些 Skill 通常通过 `npx skills add` 或直接复制 `SKILL.md` 文件的方式安装，完全在本地运行。

这里整理了几个在“不依赖 MCP”这个前提下，口碑和设计思路都很不错的选项。

### 🛠️ 值得关注的纯 Skill 方案

#### 1. `justskill-design`：无MCP理念最彻底的“设计画布”

如果你想找的是**完全摆脱 MCP 和外部服务**的布局设计方式，`justskill-design` 是最贴合的选择。它明确宣称“没有 MCP，没有 APP，没有账号，没有云端”。

它的工作流很独特：你的编码 Agent 直接运行这个 Skill，产出的设计成果是**一张自包含的 HTML 文件**，而不是死板的规格文档。这张 HTML 文件就是设计稿，可以在浏览器里直接打开、评审，并且能像代码一样用 `git diff` 来管理版本和协作。它适合那些希望设计过程**深度融入代码仓库和 Git 工作流**，并且对 MCP 有严格限制的团队。

**安装**：`npx skills use "https://github.com/justskill-ai/justskill-design" --skill "justskill-design"`

#### 2. **布局设计师 (Layout Designer)**：专注结构化布局规格输出

这个 Skill 的定位非常清晰，就是一位“精通页面布局和网格系统设计的专家”。它不直接生成代码，而是产出一份**规范的布局规格文档**，内容涵盖结构图、网格系统、间距比例和响应式行为。

它内置了四种核心工作流：**落地页布局、仪表盘/应用布局、编辑/内容布局和网格系统创建**，基本覆盖了常见的页面类型。如果你需要一份**结构清晰、可供后续开发严格遵循的布局蓝图**，而不是一堆代码，这个 Skill 会非常对口。

**安装**：`npx skills add https://github.com/Kobshobe/qy_translate/tree/HEAD/.agents/skills/layout-designer`

#### 3. `Layout and Spacing Skill` (wensity-layout)：死磕间距与响应式的“纪律委员”

这个免费 Skill 的目标非常聚焦：**治好 AI “乱设间距”的毛病**。它强制 Agent 使用一套**单一的 4px 间距尺度**，并为每个尺度步骤赋予了明确的“职责”，从而杜绝 13px 这类随意数值的出现。

除了间距，它还深入覆盖了**分组节奏、对齐、网格以及从 320px 手机到宽屏桌面的响应式重构**。它的理念是“**用距离分组，空间不够时才用边框**”，并禁止用简单的“缩小”来应付移动端，而是要求真正的“重构”。如果你的 UI 总是看起来间距杂乱、缺乏节奏感，或者需要处理复杂的响应式适配，这个 Skill 的规则性会非常有帮助。

**安装**：`npx skills add wensity/skills --skill wensity-layout`

#### 4. **Grid Layout 技能**：轻量、专注栅格组件

这是一个非常轻量的纯 Markdown Skill，专门用于设计**页面组件与转化模块的栅格内容布局**。它会引导 Agent 明确组件目标（如导航、信任、转化），并给出文案、布局、无障碍注意事项以及可落地的组件规格说明。如果你的需求集中在卡片网格、Bento 布局或特定功能模块的排列上，它是一个很趁手的专项工具。

**安装**：`npx skills add https://github.com/kostja94/marketing-skills --skill grid`

#### 5. `frontend-design-director-plus`：在安全前提下设定视觉方向

这是一个单文件的 Claude Code Skill，不依赖 MCP。它的核心是在改动 UI 之前，先让 Agent 确立一个**清晰的视觉方向（Direction note）**，明确页面用途、受众、基调等。在此基础上，它才会去优化布局、字体、颜色等，同时**严格保护现有的路由、数据流和测试不被破坏**。它适合在**已有项目中渐进式改进布局**，而不希望 AI 的“发挥”搞坏现有功能的场景。

**安装方式**：参考其 GitHub README，手动下载 `SKILL.md` 文件到对应目录即可。

### 💎 如何选择？

可以这样判断：

- 追求**极致无依赖、Git 原生协作** → **`justskill-design`**
- 需要一份**严谨、可执行的布局规格文档** → **布局设计师**
- 想根治**间距随意、响应式混乱**的问题 → **`Layout and Spacing Skill`**
- 任务**集中在栅格/卡片类组件** → **`Grid Layout`**
- 在**现有项目中安全地改进布局** → **`frontend-design-director-plus`**

你之前了解过的 **`better-layout`** 依然是布局审查与修复领域的标杆，它同样不依赖 MCP，专注于对现有布局进行压力测试（拉伸、翻译、RTL 镜像）并给出修复建议。你可以将它作为“审查者”，与上述任何一款“构建者” Skill 搭配使用，形成从生成到校验的闭环。

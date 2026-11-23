# Skill 使用路线图（按产品阶段）

本文只推荐**当前仓库中已有**的 Skill。每个条目都给出仓库路径，可直接在 `skills/` 下找到。上游来源、版本和旧名称映射见 [imported-playbook-skills.md](./imported-playbook-skills.md)。

推荐顺序按**需求 → 产品定义 → 设计 → 开发 → 架构 → 日常内容生产**组织。同一阶段内的 Skill 不必严格串行，按“首选 → 补充 → 按需”的定位取用即可。

---

## 一、需求挖掘与澄清

目标是在动手之前把问题问清楚，避免“做出来的和想要的完全不是一回事”。

| 顺序 | Skill | 仓库路径 | 定位 | 在这个阶段的作用 |
|---|---|---|---|---|
| 1 | **`grill-me`** | `skills/mattpocock/grill-me` | 首选 | 对初步方案或设计进行“灵魂拷问”，逐个分支解决决策树上的未定项。适合需求模糊、团队对方向有分歧时先跑一轮，暴露假设漏洞 |
| 2 | **`grilling`** | `skills/agents/grilling` | 底层能力 | `grill-me` 实际调用的访谈引擎。也可以直接使用，按“设计树”逐个决策分支追问，直到形成共享理解 |
| 3 | **`grill-with-docs`** | `skills/agents/grill-with-docs` | 按需 | 在 grilling 的同时产出 ADR 和术语表。适合需要把关键决策沉淀成文档的团队；依赖 `grilling`（`skills/agents/grilling`）与 `domain-modeling`（`skills/mattpocock/domain-modeling`） |

**阶段使用逻辑**：先用 `grill-me` 快速暴露逻辑缺口；需要记录决策时再用 `grill-with-docs`。如果只是想把一个问题问透，直接用 `grilling` 即可。

---

## 二、市场调研与竞品分析

需求方向初步清晰后，进入“看别人怎么做、机会在哪里”的阶段。

| 顺序 | Skill | 仓库路径 | 定位 | 在这个阶段的作用 |
|---|---|---|---|---|
| 1 | **`insight`** | `skills/liangdabiao/insight` | 首选 | 用户需求洞察与产品机会分析。输出用户画像、痛点/痒点/爽点、P0/P1/P2 机会清单，适合先建立“用户视角”的基线 |
| 2 | **`competitive-analysis`** | `skills/1198560751/competitive-analysis` | 首选 | 产品经理竞品分析报告生成器，支持单品拆解、多品对比、快速分析和深度分析两种模式 |
| 3 | **`space-chart-html`** | `skills/SpaceZephyr/space-chart-html` | 补充 | 把竞品矩阵、SWOT、用户旅程、商业模式画布、产品路线图等结论直接生成 HTML 图表，适合放进汇报或文档 |
| 4 | **`space-chart-html-plus`** | `skills/SpaceZephyr/space-chart-html-plus` | 按需 | 需要 35+ 种图表类型（桑基图、甘特图、C4、BPMN、威胁建模等）时使用，覆盖面比 `space-chart-html` 更广 |
| 5 | **`space-text-logic-diagram`** | `skills/SpaceZephyr/space-text-logic-diagram` | 按需 | 把一段分析文本拆成递进、流程、循环、层次、对比或矩阵关系的 SVG 逻辑图，适合沉淀“为什么得出这个结论” |

**阶段使用逻辑**：`insight` 建立用户基线 → `competitive-analysis` 做结构化竞品对比 → 需要可视化时用 `space-chart-html`；图表类型更复杂时换 `space-chart-html-plus`，纯逻辑关系用 `space-text-logic-diagram`。

---

## 三、产品定义（PRD / 需求文档）

调研完成后，把结论收束成可执行的文档和任务。

| 顺序 | Skill | 仓库路径 | 定位 | 在这个阶段的作用 |
|---|---|---|---|---|
| 1 | **`prd-generator`** | `skills/agents/prd-generator` | 首选 | 通过问答收集背景、目标用户、功能与非功能需求，生成 PRD 大纲、完整 PRD 和 Mermaid 流程图。适合产品经理从零起草 PRD |
| 2 | **`prd`** | `skills/agents/prd` | 备选 | 面向软件系统和 AI 功能的高质量 PRD，包含执行摘要、用户故事、技术规格和风险分析。适合工程导向或 AI 产品规格 |
| 3 | **`to-spec`** | `skills/mattpocock/to-spec` | 首选（issue tracker 流程） | 把当前对话和代码库理解直接合成为 spec，并发布到项目 issue tracker。它不做访谈，只做归纳，适合已经充分讨论过的需求 |
| 4 | **`to-tickets`** | `skills/mattpocock/to-tickets` | 首选（issue tracker 流程） | 把 plan、spec 或对话拆成 tracer-bullet 垂直切片 ticket，并标注 blocking edges，适合多 agent 并行领取 |

**阶段使用逻辑**：中文产品文档优先用 `prd-generator`；工程/AI 规格用 `prd`。如果团队用 GitHub Issues、Linear 等工具管理需求，则在讨论充分后走 `to-spec` → `to-tickets`。

> `to-spec` 和 `to-tickets` 依赖仓库内的 `setup-matt-pocock-skills`（`skills/mattpocock/setup-matt-pocock-skills`）。先在目标仓库运行一次，配置 issue tracker、triage labels 和 domain doc 布局；未配置时先用 `prd-generator` 或 `prd` 产出文档。

---

## 四、UI / UX 设计

PRD 和实施计划就绪后，进入界面与体验设计。这个阶段的关键是**先定设计系统，再做组件和页面**。

| 顺序 | Skill | 仓库路径 | 定位 | 在这个阶段的作用 |
|---|---|---|---|---|
| 1 | **`ui-ux-pro-max`** | `skills/agents/ui-ux-pro-max` | 首选 | UI/UX 设计知识底座。内置 79 种风格（50 种活跃）、192 套产品配色与推理画像、74 组字体搭配、119 条 UX 指南、105 个图标、17 个 GSAP 预设、25 种图表类型和 22 个技术栈 |
| 2 | **`frontend-design`** | `skills/agents/frontend-design` | 首选 | 在写 CSS 之前先做真实的美学承诺，生成有辨识度、生产级的前端界面，避免通用的“AI 味”审美 |
| 3 | **`design-system`** | `skills/agents/design-system` | 首选 | 设计 token 架构、组件规格和演示文稿策略。覆盖 primitive → semantic → component 三层 token、CSS 变量、间距/字号比例 |
| 4 | **`theming-components`** | `skills/ancoleman/theming-components` | 补充 | 更细的 token 分类、主题切换、RTL/i18n、对比度和减少动效等无障碍实现，适合作为组件库的样式底座 |
| 5 | **`design-an-interface`** | `skills/mattpocock/design-an-interface` | 探索 | 用并行子 agent 生成多个截然不同的接口/界面方向，适合定稿前做“design it twice”对比。该 Skill 已从上游主分支移除，仓库保留 v1.0.0 版本 |
| 6 | **`space-brand-ui-design`** | `skills/SpaceZephyr/space-brand-ui-design` | 按需 | 从 getdesign.md 获取 62 个品牌风格（Apple、Notion、Claude、Stripe 等），生成“做成 XX 的感觉”的 UI 代码 |
| 7 | **`ui-styling`** | `skills/agents/ui-styling` | 实现 | 用 shadcn/ui、Radix UI 和 Tailwind CSS 落地界面，覆盖响应式布局、主题、暗色模式和无障碍组件 |
| 8 | **`shadcn`** | `skills/agents/shadcn` | 实现 | 管理 shadcn 组件与项目：添加、搜索、修复、调试、组合组件，处理 `components.json` 和 preset |
| 9 | **`building-forms`** | `skills/ancoleman/building-forms` | 按需 | 表单与数据采集组件：50+ 输入类型、校验策略、多步向导、WCAG 2.1 无障碍 |
| 10 | **`building-tables`** | `skills/ancoleman/building-tables` | 按需 | 表格与数据网格：排序、筛选、分页、大数据量、TanStack Table / AG Grid 选型 |
| 11 | **`creating-dashboards`** | `skills/ancoleman/creating-dashboards` | 按需 | 仪表盘与分析界面：KPI 卡片、实时更新、多图表协同布局 |
| 12 | **`designing-layouts`** | `skills/ancoleman/designing-layouts` | 按需 | 栅格、Flexbox、侧边栏、响应式断点等布局系统 |
| 13 | **`visualizing-data`** | `skills/ancoleman/visualizing-data` | 按需 | 按分析目的选择 24+ 种可视化类型，含色盲友好配色和 WCAG 2.1 AA 无障碍 |
| 14 | **`building-ai-chat`** | `skills/ancoleman/building-ai-chat` | 按需 | ChatGPT 风格对话界面：流式响应、上下文管理、多模态、工具调用可视化 |
| 15 | **`assembling-components`** | `skills/ancoleman/assembling-components` | 收尾 | 把 theming、layout、dashboard、data-viz 等组件产出组装成可运行的 React/Next.js、Python 或 Rust 组件系统 |

**阶段使用逻辑**：`ui-ux-pro-max` 定知识和风格方向 → `frontend-design` 定审美 → `design-system` / `theming-components` 定 token 和主题 → 早期方向对比用 `design-an-interface` → 品牌风格用 `space-brand-ui-design` → 落地用 `ui-styling` / `shadcn` → 具体组件从 `ancoleman` 集合按需取 → 最后用 `assembling-components` 组装。

---

## 五、前端开发

设计确定后进入编码。前端核心诉求是性能、可维护性和组件质量。

| 顺序 | Skill | 仓库路径 | 定位 | 在这个阶段的作用 |
|---|---|---|---|---|
| 1 | **`vercel-react-best-practices`** | `skills/agents/vercel-react-best-practices` | 首选 | React / Next.js 性能规则集，覆盖请求瀑布消除、包体积、服务端性能、重渲染等。适合写新代码或 review 时作为性能基线 |
| 2 | **`vercel-composition-patterns`** | `skills/agents/vercel-composition-patterns` | 首选 | React 组合模式与组件 API 设计，专治 boolean props 堆砌、过度依赖 render props 等反模式 |
| 3 | **`tdd`** | `skills/mattpocock/tdd` | 首选 | 红-绿-重构循环，按 vertical slice 逐个构建功能或修复 bug。适合作为编码节奏约束 |
| 4 | **`shadcn`** | `skills/agents/shadcn` | 首选 | 组件层落地与维护，处理 shadcn 组件、registry 和 preset |
| 5 | **`ui-styling`** | `skills/agents/ui-styling` | 首选 | Tailwind + shadcn/ui 的样式实现，含响应式、主题和暗色模式 |
| 6 | **`web-design-guidelines`** | `skills/agents/web-design-guidelines` | 检查 | 按 Web Interface Guidelines 审查 UI 代码，检查无障碍、交互和设计规范 |

**阶段使用逻辑**：`vercel-react-best-practices` 作为日常性能守则贯穿全程 → 设计组件 API 时主动调用 `vercel-composition-patterns` → 用 `tdd` 控制实现节奏 → 用 `shadcn` / `ui-styling` 落地 → 提交前用 `web-design-guidelines` 做 UI 审查。

---

## 六、架构设计与代码质量

前端组件和页面跑起来之后，需要从系统层面审视代码库健康度。这个阶段可以与前端开发并行，也可以作为迭代前或接手老项目时的前置体检。

| 顺序 | Skill | 仓库路径 | 定位 | 在这个阶段的作用 |
|---|---|---|---|---|
| 1 | **`improve-codebase-architecture`** | `skills/agents/improve-codebase-architecture` | 首选 | 扫描代码库中的 shallow module，识别可以“深化”的机会，输出可视化 HTML 报告，并进入 grilling 深化环节 |
| 2 | **`karpathy-guidelines`** | `skills/forrestchang/karpathy-guidelines` | 首选 | 行为护栏：Think Before Coding、Simplicity First、Surgical Changes、Goal-Driven Execution，防止 AI 过度设计和无关改动 |
| 3 | **`request-refactor-plan`** | `skills/mattpocock/request-refactor-plan` | 首选 | 通过访谈生成小步提交的重构计划，并归档为 GitHub issue，避免一次性大改。该 Skill 已从上游主分支移除，仓库保留 v1.0.0 版本 |
| 4 | **`code-review-excellence`** | `skills/agents/code-review-excellence` | 补充 | 代码评审实践：发现缺陷、提供建设性反馈、建立评审标准 |
| 5 | **`systematic-debugging`** | `skills/agents/systematic-debugging` | 补充 | 遇到 bug、测试失败或异常行为时，先系统定位根因再提修复方案 |
| 6 | **`designing-apis`** | `skills/ancoleman/designing-apis` | 按需 | REST、GraphQL、事件驱动 API 的设计原则、版本演进和团队标准 |
| 7 | **`testing-strategies`** | `skills/ancoleman/testing-strategies` | 按需 | 单元、集成、E2E、契约测试的组合策略，含属性测试和 CI/CD 集成 |
| 8 | **`performance-engineering`** | `skills/ancoleman/performance-engineering` | 按需 | 负载测试（k6、Locust）、CPU/内存/IO profiling、缓存、查询优化和 Core Web Vitals |
| 9 | **`generating-documentation`** | `skills/ancoleman/generating-documentation` | 按需 | 生成 OpenAPI/Swagger、TypeDoc/Sphinx、Docusaurus/MkDocs、ADR 和 Mermaid/PlantUML 图 |

**阶段使用逻辑**：`improve-codebase-architecture` 发现问题 → `karpathy-guidelines` 在重构和架构变更时约束行为 → `request-refactor-plan` 生成可执行的小步重构路径 → `code-review-excellence` 和 `systematic-debugging` 守住质量；需要更深的 API、测试、性能或文档能力时，再取 `ancoleman` 的对应 Skill。

---

## 七、日常内容生产

这部分贯穿产品从立项到推广的全程，可以独立成一条内容生产工作流。先定主力管线，再按平台叠加专用 Skill。

### 7.1 一站式主力管线（图片为主）

| 顺序 | Skill | 仓库路径 | 定位 | 在这个阶段的作用 |
|---|---|---|---|---|
| 1 | **`baoyu-slide-deck`** | `skills/JimLiu/baoyu-slide-deck` | 首选（幻灯片） | 从内容生成大纲和逐页幻灯片图片，适合 PPT、演示和课程材料 |
| 2 | **`baoyu-infographic`** | `skills/JimLiu/baoyu-infographic` | 首选（信息图） | 21 种版式 × 22 种视觉风格，分析内容后推荐组合并生成出版级信息图 |
| 3 | **`baoyu-article-illustrator`** | `skills/agents/baoyu-article-illustrator` | 首选（文章配图） | 分析文章结构，按 Type × Style × Palette 三维方法为文章生成配图 |
| 4 | **`baoyu-cover-image`** | `skills/agents/baoyu-cover-image` | 首选（封面） | 5 个维度（类型、配色、渲染、文字、情绪）× 11 套配色 × 7 种渲染风格，支持 2.35:1、16:9、1:1 |
| 5 | **`baoyu-post-to-wechat`** | `skills/JimLiu/baoyu-post-to-wechat` | 首选（公众号发布） | 通过 API 或 Chrome CDP 发布公众号文章或贴图，支持 Markdown/HTML/纯文本 |
| 6 | **`baoyu-image-gen`** | `skills/JimLiu/baoyu-image-gen` | 底层 | 多供应商 AI 生图后端（OpenAI、Azure、Google、OpenRouter、DashScope、GLM、MiniMax、Jimeng、Seedream、Replicate 等），支持文生图、参考图和批量生成 |
| 7 | **`baoyu-comic`** | `skills/agents/baoyu-comic` | 按需 | 知识漫画/教育漫画，支持多种画风和分镜布局 |
| 8 | **`baoyu-compress-image`** | `skills/agents/baoyu-compress-image` | 收尾 | 把成品压成 WebP 或 PNG，控制发布体积 |

### 7.2 平台专用与结构化视觉

| 顺序 | Skill | 仓库路径 | 定位 | 在这个阶段的作用 |
|---|---|---|---|---|
| 1 | **`guizang-social-card-skill`** | `skills/op7418/guizang-social-card-skill` | 首选（小红书/公众号头图） | 生成小红书 3:4 组图、公众号 21:9 头图 + 1:1 分享卡、Live Photo 动图卡片，内置电子杂志风和瑞士国际主义风格 |
| 2 | **`ian-xiaohei-illustrations`** | `skills/helloianneo/ian-xiaohei-illustrations` | 首选（中文长文正文配图） | 用固定 IP“小黑”生成 16:9 白底手绘解释图，适合方法论文章和公众号长文，风格辨识度高且不易漂移 |
| 3 | **`smart-illustrator`** | `skills/axtonliu/smart-illustrator` | 首选（多引擎/多平台） | 文章配图、PPT/Slides 批量信息图、Cover 三种模式，支持 Bento Grid 功能展示图和多平台封面 |
| 4 | **`space-image-studio`** | `skills/SpaceZephyr/space-image-studio` | 备选（小红书/PPT/图表/逻辑图） | 一个 Skill 覆盖小红书封面、PPT 配图、12+ 种图表和文章逻辑图，内置 12 种中文场景风格 |
| 5 | **`space-slide-deck`** | `skills/SpaceZephyr/space-slide-deck` | 备选（PPTX/PDF） | 生成幻灯片图片并导出 PPTX/PDF，支持 60+ 品牌风格和 5 个匹配风格推荐 |
| 6 | **`space-markdown-poster`** | `skills/SpaceZephyr/space-markdown-poster` | 按需 | 把 Markdown、播客摘要或文章转成 3:4 社交分享海报 |
| 7 | **`space-wechat-layout`** | `skills/SpaceZephyr/space-wechat-layout` | 按需 | 把文章或 Markdown 排成公众号 HTML，支持本地预览和一键复制富文本 |
| 8 | **`space-logo-generator`** | `skills/SpaceZephyr/space-logo-generator` | 按需 | 批量生成 10 个 Logo 变体，支持 7 种风格和参考图分析 |
| 9 | **`space-storyboard-generator`** | `skills/SpaceZephyr/space-storyboard-generator` | 按需 | 把故事拆成分镜脚本，批量生成风格一致的故事板插图 |
| 10 | **`space-canvas-art`** | `skills/SpaceZephyr/space-canvas-art` | 按需 | 用设计哲学生成海报、艺术图和静态视觉作品 |
| 11 | **`space-generative-art`** | `skills/SpaceZephyr/space-generative-art` | 按需 | 用 p5.js 和带种子的随机性生成算法艺术、流场和粒子系统 |

### 7.3 图表、演示与视频

| 顺序 | Skill | 仓库路径 | 定位 | 在这个阶段的作用 |
|---|---|---|---|---|
| 1 | **`space-chart-html`** | `skills/SpaceZephyr/space-chart-html` | 首选（HTML 图表） | 10 种常用图表：流程图、架构图、ER 图、商业模式画布、用户旅程、思维导图、竞品分析、SWOT、路线图、组织架构 |
| 2 | **`space-chart-html-plus`** | `skills/SpaceZephyr/space-chart-html-plus` | 补充 | 35+ 种图表，覆盖技术架构、流程逻辑、业务战略、数据可视化和信息展示 |
| 3 | **`space-chart-image`** | `skills/SpaceZephyr/space-chart-image` | 按需 | 用 AI 图片模型直接生成图表图片，不输出 HTML；适合需要图片而非网页的场景 |
| 4 | **`space-architecture-diagram`** | `skills/SpaceZephyr/space-architecture-diagram` | 按需 | 系统架构图、基础设施拓扑、云架构、安全架构、网络拓扑，输出带暗色/浅色切换的 HTML/SVG |
| 5 | **`space-mermaid-diagram`** | `skills/SpaceZephyr/space-mermaid-diagram` | 按需 | 把文本、工作流或逻辑转成 Mermaid 流程图、时序图、类图 |
| 6 | **`space-text-logic-diagram`** | `skills/SpaceZephyr/space-text-logic-diagram` | 按需 | 把文本拆成递进、流程、循环、层次、对比、矩阵六种关系的 SVG 逻辑图 |
| 7 | **`slides`** | `skills/agents/slides` | 备选（HTML 演示） | 用 Chart.js、设计 token、响应式布局和文案公式生成 HTML 演示文稿 |
| 8 | **`banner-design`** | `skills/agents/banner-design` | 按需 | 社交平台、广告、网站 Hero 和印刷 Banner，支持多种艺术方向和 AI 视觉 |
| 9 | **`faceless-explainer`** | `skills/agents/faceless-explainer` | 按需 | 把文章、笔记或主题转成无真人出镜的解释视频，按场景发明排版、抽象图形、图表和数据可视化 |

**阶段使用逻辑**：追求“一个管线覆盖大部分图片生产 + 公众号发布”选 `baoyu-*`；追求信息结构和多平台输出选 `space-*`。平台专用叠加：小红书/公众号头图用 `guizang-social-card-skill`，中文长文正文用 `ian-xiaohei-illustrations`，多引擎/多平台封面用 `smart-illustrator`。幻灯片在 `baoyu-slide-deck`（图片）、`space-slide-deck`（PPTX/PDF）和 `slides`（HTML/Chart.js）之间按交付格式选择。

---

## 八、贯穿全程：生态入口

| 顺序 | Skill | 仓库路径 | 定位 | 作用 |
|---|---|---|---|---|
| 1 | **`find-skills`** | `skills/agents/find-skills` | 首选 | 元 Skill：用自然语言让 AI 搜索和安装其他 Skill，适合按需发现细分方向的新工具 |
| 2 | **`sync-skills`** | `skills/agents/sync-skills` | 首选 | 在本机多个 AI 编程工具之间同步 Skill，支持 dry run 和安装位置查询 |
| 3 | **`space-image-skill-builder`** | `skills/SpaceZephyr/space-image-skill-builder` | 按需 | 通过交互式问答生成自定义批量生图 Skill，不需要写代码 |

---

## 整体使用顺序速览

从零走完一个完整产品周期，推荐顺序大致是：

**`find-skills`（装生态入口）→ `grill-me` / `grilling`（拷问需求）→ `insight`（用户基线）→ `competitive-analysis`（竞品）→ `prd-generator` / `prd`（PRD）→ `to-spec` → `to-tickets`（issue tracker 流程）→ `ui-ux-pro-max` + `frontend-design` + `design-system`（设计系统 + 审美）→ `vercel-react-best-practices` + `vercel-composition-patterns` + `tdd`（前端编码）→ `improve-codebase-architecture` + `karpathy-guidelines` + `request-refactor-plan`（架构体检、约束与重构）→ 内容生产按平台选用 `baoyu-*` / `space-*` / `guizang-social-card-skill` / `ian-xiaohei-illustrations` / `smart-illustrator`。**

实际使用时不需要严格串行：`grill-me` 可以在 PRD 定稿前反复跑，`improve-codebase-architecture` 可以在任何迭代开始前单独使用，内容生产 Skill 完全可以根据发布节奏独立调用。核心是把每个阶段的 Skill 放在它最能**减少返工**的位置。

---

## 维护说明

- 本文只列仓库内已有的 Skill；新增或替换 Skill 时同步更新对应路径。
- 旧版中在上游找不到的条目，已替换为仓库内的等价方案。来源、版本和名称映射见 [imported-playbook-skills.md](./imported-playbook-skills.md)。
- `design-an-interface` 和 `request-refactor-plan` 来自上游 `v1.0.0`，已从主分支移除；仓库保留它们是为了保留可用的历史方案。

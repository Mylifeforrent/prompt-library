# UI 设计 Token / 设计系统资源

以下是五个资源的访问链接，其中 “Design Systems Index” 已确认是一个可在 Claude Code 等 Agent 中调用的 Skill。

## 📚 资源链接汇总

### `brands-design-md`

一个包含 69 个品牌 DESIGN.md 文件的开源库，每个品牌目录下通常包含 `DESIGN.md`、`preview.html`、`tokens.json`、`variables.css` 等完整结构。

- **GitHub**：<https://github.com/ricocc/brands-design-md>

### `Awesome DESIGN.md`

这是该类项目中最主流、更新最活跃的版本（由 VoltAgent 维护），收录了大量从真实开发者网站提取的 DESIGN.md 文件，可以直接放入项目供 AI 编码工具使用。

- **GitHub（VoltAgent 主版本）**：<https://github.com/VoltAgent/awesome-design-md>

此外还有由社区维护的衍生版本，收录范围略有不同，可作为补充参考：

- **everpay 版本**：<https://github.com/everpay/awesome-design-md>
- **rahulholkar16 版本**：<https://github.com/rahulholkar16/awesome-design-md>

### `awesome-design-md-cn`

这是 `Awesome DESIGN.md` 的中文策展版，存在两个侧重不同的仓库：

- **bayshier 版本**：将 VoltAgent 仓库的 README 和说明汉化，DESIGN.md 文件本身保留英文。
  - **GitHub**：<https://github.com/bayshier/awesome-design-md-cn>
- **xueuncia-product 版本**：做了更深的策展，按 **9 种美学风格** 对 74 个品牌进行分类，并提供了 **200 张在线渲染的 Demo** 页面，更方便按风格反向查找。
  - **GitHub**：<https://github.com/xueuncia-product/awesome-design-md-cn>
  - **在线 Demo 速查**：<https://xueuncia-product.github.io/awesome-design-md-cn/>

### `FreeDesign`

面向开发者的设计资源导航库，按场景分类收录了 120+ 个 UI 组件库、设计系统、Figma 插件、配色字体、Landing Page 模板等，适合作为上游资源池持续挖掘。

- **GitHub**：<https://github.com/AIPMAndy/FreeDesign>

### `Design Systems Index`（Skill）

这正是之前关注的那个被封装为 **Claude Code Agent Skill** 的项目。它本质上是一个**导航索引**，帮助 AI Agent 定位各大公司的设计系统（如 Material、Fluent、Carbon、Polaris）、Design Tokens 工具/规范，以及可用的 React/React Native 组件库。它不提供具体的设计文件，而是充当“调度层”，引导 Agent 找到正确的参考来源。

- **Skill 页面（Awesome Skills）**：<https://www.awesomeskills.dev/skills/design-systems-index>
- **备用来源（SkillsMP）**：<https://skillsmp.com/skills/ezra-y-design-systems-index>

# Prompt Library

A starter asset repository for [Prompt Keeper](https://github.com/Mylifeforrent/prompt-keeper). It uses the canonical layout the app scans when you connect a repository, and it ships nine demo assets that cover every supported file shape.

Use it as a local bind target while developing, or push it to your own Git host and connect it from the Sync workspace.

## Repository layout

```text
prompts/<folder>/<slug>.prompt.md
instructions/<folder>/<slug>.contract.md
skills/<folder>/<skill-name>/SKILL.md
mcp/<folder>/<server-name>.json
```

The demo content is arranged like this:

```text
.
├── prompts/
│   ├── engineering/
│   │   ├── code-review/review-pull-request.prompt.md
│   │   └── operations/incident-postmortem.prompt.md
│   └── meeting-summary.prompt.md
├── instructions/
│   ├── global/collaboration-baseline.contract.md
│   └── engineering/typescript/typescript-strictness.contract.md
├── skills/
│   └── engineering/
│       ├── git/commit-helper/
│       │   ├── SKILL.md
│       │   ├── references/conventional-commits.md
│       │   └── scripts/validate-subject.sh
│       └── testing/test-plan-writer/SKILL.md
└── mcp/
    └── development/
        ├── local/filesystem.json
        └── docs/docs-search.json
```

Rules that apply to every asset type:

- Folder paths are repository directories and may nest to any depth.
- The last level is fixed: one `.prompt.md` per Prompt, one `.contract.md` per contract, one directory per Skill with `SKILL.md` at its root, one `.json` per MCP server.
- Each asset carries a stable `id`. Keep it when you rename or move an asset so Prompt Keeper preserves history and sync state instead of treating the move as a delete plus an add.
- Files and directories outside the four roots are ignored by the asset scanner. Root files such as `README.md` and `LICENSE` are safe.

## Prompts

A Prompt is one Markdown file with YAML frontmatter and a body split into `## System Prompt` and `## User Prompt`.

```markdown
---
id: ast_roxnxlwh2nmyn2
title: Review Pull Request
description: Produce a prioritized code review for a pull request diff.
folder: engineering/code-review
tags:
  - code-review
syncPolicy: inherit
variables:
  - name: diff
    type: textarea
    label: Pull request diff
    required: true
---
## System Prompt

You are a senior software engineer reviewing a pull request.

## User Prompt

Review this diff:

{{diff}}
```

- `title` is required.
- `folder` is the directory between `prompts/` and the file. Keep it equal to the actual path.
- `syncPolicy` is `inherit`, `sync`, or `local`.
- Variable types are `text`, `textarea`, `number`, and `select`. A `select` variable needs a non-empty `options` list.
- Variables are referenced as `{{name}}`. Prompt Keeper discovers variables in the body and merges them with the frontmatter definitions; a definition that is never referenced is dropped.
- The body must contain `## System Prompt`, `## User Prompt`, or both.

## Agent Instructions

A contract is one Markdown file with frontmatter that describes when the rule applies. The body is the instruction text.

```markdown
---
id: ast_edcz247bgz9ayn
title: TypeScript Strictness
description: Type and error-handling rules for TypeScript sources under src/.
folder: engineering/typescript
scope: path
pathPrefix: src/
activation:
  mode: glob
  globs:
    - "src/**/*.ts"
priority: 60
imports: []
targetIds:
  - copilot-path
  - cursor
  - windsurf
tags:
  - typescript
syncPolicy: inherit
---
# TypeScript Strictness

Rules go here.
```

- `scope` is `user`, `project`, or `path`. A `path` scope requires a non-empty `pathPrefix`.
- `activation.mode` is `always`, `glob`, `model`, or `manual`. A `glob` activation requires at least one pattern; quote patterns that start with `*`.
- `priority` is a number; higher values win when targets merge rules.
- `targetIds` is optional. Known project target IDs are `agents-md`, `claude`, `copilot`, `copilot-path`, `cursor`, and `windsurf`. Targets that cannot represent the activation mode are skipped with a warning rather than silently downgraded.
- The body must not be empty.

## Skills

A Skill is a directory whose root contains `SKILL.md`. Every other file in that directory ships with the Skill.

```markdown
---
id: ast_x492jngv6x6ssg
title: Commit Helper
description: Draft and validate Conventional Commit messages.
folder: engineering/git
tags:
  - git
version: 1.1.0
author: Prompt Library
category: engineering
icon: GC
---
# Commit Helper

Instructions go here.
```

- `SKILL.md` must exist at the root of the Skill directory.
- `title` is the display name; `name` is accepted as a fallback.
- `folder` is the directory between `skills/` and the Skill directory.
- `version`, `author`, `category`, and `icon` are free-form metadata used by the UI.
- Skills may contain scripts and references. Prompt Keeper never executes them; the connect preflight only flags their presence as a risk.

## MCP servers

An MCP file is one JSON object per server. Credential-like `env` and `headers` values must be `${VAR}` placeholders; real values never belong in this repository.

```json
{
  "id": "ast_yhiqxihjnep694",
  "title": "Docs Search",
  "description": "Query an internal documentation index over HTTP.",
  "folder": "development/docs",
  "tags": ["docs", "http"],
  "transport": "http",
  "url": "https://docs.example.com/mcp",
  "headers": {
    "X-API-Key": "${DOCS_API_KEY}"
  },
  "enabled": true,
  "notes": "Set the real key locally before dispatch."
}
```

- `transport` is `stdio` or `http`.
- A `stdio` server needs `command` and may use `args`; an `http` server needs `url`.
- `requiredEnv` lists environment variable names that must have a local value before dispatch.
- Prompt Keeper detects credential-like keys (`KEY`, `TOKEN`, `SECRET`, `PASSWORD`, `CREDENTIAL`, `AUTH`) and placeholder values. It stores real values with `safeStorage`, substitutes them outside the repository, and redacts them from logs, audit events, and renderer payloads.

## Connect it to Prompt Keeper

1. Open **Sync** and choose **Connect repository**.
2. Enter the repository address:
   - For this local folder, use its absolute path, for example `/Users/you/vscode-workspace/prompt-library`, as the repository URL.
   - After pushing to a Git host, use the HTTPS or SSH URL instead.
3. Choose **Bind existing clone** and select this directory when using the local path. Choose **App-managed clone** when using a remote URL.
4. Keep the auto-detected layout: `prompts`, `instructions`, `skills`, and `mcp`.
5. Review the preflight. It should report three Prompts, two instructions, two Skills, and two MCP servers, and it should flag one script under `skills/engineering/git/commit-helper/scripts/`.

Prompt Keeper accepts absolute local paths and `file:` URLs for offline repositories, so you can test the full sync flow before creating a remote.

## Adding an asset

1. Create the directory under the correct root. For a Skill, create the Skill directory and add `SKILL.md` first.
2. Generate a new stable ID and add it to the frontmatter or JSON.
3. Follow the format rules above, and keep `folder` aligned with the path.
4. Commit the change, then run the connect or fetch preflight in Prompt Keeper to catch malformed files, duplicate IDs, and credential findings.

## License

MIT. See [LICENSE](./LICENSE).

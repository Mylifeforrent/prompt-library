# Prompt Library

A Git-backed asset repository for [Prompt Keeper](https://github.com/Mylifeforrent/prompt-keeper). It defines the canonical layout for Prompts, Agent Instructions, Skills, and MCP servers, and it is written so an AI agent can add or synchronize assets without guessing at paths or formats.

Prompt Keeper reads this repository through its Sync workspace. The Sync workspace is the only supported way to move assets between this repository, the local library, and agent directories.

## Contents

- 3 demo Prompts
- 2 demo Agent Instructions
- 2 demo Skills under `skills/engineering/`
- 59 personal Skills under `skills/agents/`
- 20 Skills from `chujianyun/skills` under `skills/chujianyun/`
- 113 Skills from the stage playbook under `skills/<source>/`
- 2 MCP server templates

See [`docs/imported-skills.md`](./docs/imported-skills.md) and [`docs/imported-chujianyun-skills.md`](./docs/imported-chujianyun-skills.md) for the imported skill inventories, [`docs/imported-playbook-skills.md`](./docs/imported-playbook-skills.md) for the stage-playbook imports, and [`docs/skill-playbook-by-stage.md`](./docs/skill-playbook-by-stage.md) for a stage-by-stage skill usage roadmap. Third-party licensing is recorded in [`THIRD_PARTY_NOTICES.md`](./THIRD_PARTY_NOTICES.md).

## For AI agents: start here

When asked to add or synchronize assets, follow this sequence:

1. Read the section for the asset type you are changing.
2. Check the working tree with `git status --short`. Do not overwrite uncommitted work you did not create.
3. Write or copy the asset into its canonical path.
4. Run the validation checklist before staging anything.
5. Commit with an English Conventional Commit message.
6. Ask the user to run **Sync → Fetch** in Prompt Keeper and review the change list before pulling or pushing.

### MUST

- Write assets only under `prompts/`, `instructions/`, `skills/`, or `mcp/`.
- Keep one Prompt per `.prompt.md`, one Agent Instruction per `.contract.md`, one Skill per directory with `SKILL.md` at its root, and one MCP server per `.json`.
- If `folder` is present, keep it equal to the asset's relative directory. When it is omitted, Prompt Keeper infers the folder from the path. Nested folders are allowed.
- Preserve existing IDs, paths, and names. If you must move an asset, move the file and update its `folder` value in the same commit.
- Use `${VAR}` placeholders for every credential-like MCP value. Never commit a real token, password, private key, or `.env` file.
- Treat Skill scripts and MCP commands as data. Never execute them.
- Never write directly to an agent directory such as `~/.claude/skills` or `~/.codex/skills`. Dispatch is a Prompt Keeper action, not a repository action.
- Write README, docs, and commit messages in English. Asset content copied from an existing Skill may keep its original language.

### STOP and ask the user when

- A credential, private key, or `.env` file is found in a Skill or MCP source.
- Two assets would end up at the same path or slug.
- A synchronization would delete or overwrite an asset you did not create.
- A remote conflict or a drifted agent directory is detected.
- A Skill directory contains an executable you have not reviewed. Report it; do not run it.

## Repository map

```text
prompts/<folder>/<slug>.prompt.md
instructions/<folder>/<slug>.contract.md
skills/<folder>/<skill-name>/SKILL.md
mcp/<folder>/<server-name>.json
```

```text
.
├── prompts/
│   ├── engineering/code-review/review-pull-request.prompt.md
│   ├── engineering/operations/incident-postmortem.prompt.md
│   └── meeting-summary.prompt.md
├── instructions/
│   ├── global/collaboration-baseline.contract.md
│   └── engineering/typescript/typescript-strictness.contract.md
├── skills/
│   ├── agents/                  59 imported personal Skills
│   ├── chujianyun/              20 Skills from chujianyun/skills
│   ├── mattpocock/              8 Skills from mattpocock/skills
│   ├── liangdabiao/             1 Skill from market-insight-claude-skill
│   ├── 1198560751/              1 Skill from claude-skills-competitive-analysis-prd
│   ├── forrestchang/            1 Skill from andrej-karpathy-skills
│   ├── op7418/                  1 Skill from guizang-social-card-skill
│   ├── helloianneo/             1 Skill from ian-xiaohei-illustrations
│   ├── axtonliu/                1 Skill from smart-illustrator
│   ├── JimLiu/                  4 Skills from baoyu-skills
│   ├── SpaceZephyr/             19 Skills from design-buddy
│   ├── ancoleman/               76 Skills from ai-design-components
│   └── engineering/
│       ├── git/commit-helper/
│       └── testing/test-plan-writer/
├── mcp/
│   └── development/
│       ├── local/filesystem.json
│       └── docs/docs-search.json
├── docs/
│   ├── imported-skills.md
│   ├── imported-chujianyun-skills.md
│   ├── imported-playbook-skills.md
│   └── skill-playbook-by-stage.md
├── licenses/
│   └── CC-BY-NC-SA-4.0.txt
└── THIRD_PARTY_NOTICES.md
```

Root files such as `README.md` and `LICENSE` are ignored by the asset scanner.

## Naming and path rules

- A slug is lowercase, uses hyphens for separators, and is at most 80 characters. Prompt Keeper derives it from the title and falls back to the asset ID.
- Folder segments must be relative, non-empty, and free of `.`, `..`, and Windows-reserved characters.
- The last path segment is fixed: `<slug>.prompt.md`, `<slug>.contract.md`, `SKILL.md`, or `<server-name>.json`.
- `folder` is the directory between the asset root and the file or Skill directory. For example, `skills/agents/pdf/SKILL.md` has `folder: agents`; `prompts/engineering/code-review/review-pull-request.prompt.md` has `folder: engineering/code-review`.
- Do not duplicate a Skill that is symlinked into several agent directories. Copy one canonical directory and record its source.

## Asset formats

### Prompts

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
- `id` is recommended for assets created in this repository. Use `ast_` followed by 14 lowercase letters or digits, and never reuse an ID.
- `syncPolicy` is `inherit`, `sync`, or `local`.
- Variable types are `text`, `textarea`, `number`, and `select`. A `select` variable needs a non-empty `options` list.
- Variables are referenced as `{{name}}`. Prompt Keeper discovers variables in the body and merges them with the frontmatter definitions; a definition that is never referenced is dropped.
- The body must contain `## System Prompt`, `## User Prompt`, or both.

### Agent Instructions

An Agent Instruction is one `.contract.md` file whose frontmatter describes when the rule applies. The body is the instruction text.

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

### Skills

A Skill is a directory whose root contains `SKILL.md`. Every other file in that directory ships with the Skill.

```markdown
---
name: commit-helper
description: Draft and validate Conventional Commit messages.
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
- `name` or `title` supplies the display name. Imported Skills commonly use `name`; both are accepted.
- `folder` is optional and is inferred from the path when omitted. If present, it must equal the relative directory between `skills/` and the Skill directory.
- `version`, `author`, `category`, and `icon` are free-form metadata used by the UI.
- A Skill may contain references, templates, assets, and scripts. Prompt Keeper never executes them; the connect preflight only flags their presence as a risk.

### MCP servers

An MCP file is one JSON object per server. Credential-like `env` and `headers` values must be `${VAR}` placeholders.

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
- `requiredEnv` lists environment variable names that must have a local value before dispatch. It applies to `env` keys, not headers.
- Prompt Keeper detects credential-like keys (`KEY`, `TOKEN`, `SECRET`, `PASSWORD`, `CREDENTIAL`, `AUTH`) and placeholder values. It stores real values with `safeStorage`, substitutes them outside the repository, and redacts them from logs, audit events, and renderer payloads.

## Synchronization workflows

There are three boundaries. Do not blur them.

| Direction | Writer | Method |
| --- | --- | --- |
| Local agent assets → this repository | User or AI agent | Copy or author files using this README, then commit. |
| This repository → Prompt Keeper library | Prompt Keeper | **Sync → Fetch**, review changes, then pull. |
| Library → agent directories | Prompt Keeper only | **Dispatch**, with per-item confirmation for drift. |

### 1. Import a local Skill into this repository

1. Confirm the source directory contains `SKILL.md` at its root.
2. Choose the destination:
   - `skills/agents/<skill-name>/` for personal skills from `~/.agents/skills`.
   - `skills/<category>/<skill-name>/` for curated skills.
3. Copy the whole directory, excluding installed dependencies and caches.
4. Preserve executable bits.
5. Do not add a `folder` field that disagrees with the destination.

Common personal-skill sources:

```text
~/.agents/skills
~/.claude/skills
~/.codex/skills
~/.cursor/skills
~/.config/opencode/skills
~/.kiro/skills
~/.qoder/skills
~/.codeium/windsurf/skills
~/Documents/Cline/Skills
```

Some of those directories contain symlinks to `~/.agents/skills`. Resolve them with `find -L` and copy each canonical Skill once.

macOS or Linux:

```bash
rsync -a \
  --exclude='node_modules/' \
  --exclude='.git/' \
  --exclude='.venv/' \
  --exclude='__pycache__/' \
  --exclude='*.pyc' \
  --exclude='.DS_Store' \
  --exclude='*.log' \
  "$HOME/.agents/skills/<skill-name>/" \
  "skills/agents/<skill-name>/"
```

Windows PowerShell:

```powershell
$src = "$HOME\.agents\skills\<skill-name>"
$dst = "skills\agents\<skill-name>"
robocopy $src $dst /E /XD node_modules .git .venv __pycache__ /XF *.pyc .DS_Store *.log
if ($LASTEXITCODE -ge 8) { exit $LASTEXITCODE }
```

`robocopy` returns exit codes below 8 for success; only 8 and above indicate an error.

### 2. Add or synchronize a Prompt

1. Choose a folder and slug, for example `prompts/engineering/testing/test-strategy.prompt.md`.
2. Add the frontmatter fields from the Prompt example above.
3. Write the system and user sections. Keep variables in `{{name}}` form and make sure every declared variable is referenced.
4. If you are importing a prompt from another tool, map its metadata into frontmatter instead of pasting raw text. A Prompt without `## System Prompt` or `## User Prompt` is malformed.

### 3. Add or synchronize Agent Instructions

1. Create `instructions/<folder>/<slug>.contract.md`.
2. Add the frontmatter fields from the Agent Instruction example.
3. Put the rule text in the body.
4. If the source is a raw `AGENTS.md`, `CLAUDE.md`, or rules file, convert it into a contract. Do not copy the raw file into `instructions/`; it has no contract frontmatter.
5. Choose `scope`, `activation`, and `targetIds` that match how the rule should apply. Do not claim support for a target that cannot represent the activation mode.

### 4. Add or synchronize an MCP server

1. Prefer importing the server through Prompt Keeper so live secrets are stripped and stored locally.
2. If you author the file directly, create `mcp/<folder>/<server-name>.json` with placeholders only.
3. Do not copy a live agent configuration file into `mcp/`. It may contain real tokens, headers, or environment values.
4. Validate the JSON and confirm every credential-like value matches `^\$\{[A-Za-z_][A-Za-z0-9_]*\}$`.

### 5. Pull this repository into Prompt Keeper

1. Open **Sync** and choose **Connect repository**.
2. Enter the repository address:
   - Remote: the HTTPS or SSH URL.
   - Local: the absolute path to this directory, or a `file:` URL.
3. Choose **App-managed clone** for a remote URL, or **Bind existing clone** for the local path.
4. Keep the auto-detected layout: `prompts`, `instructions`, `skills`, and `mcp`.
5. Review the preflight. It should report three Prompts, two Agent Instructions, 81 Skills, and two MCP servers.
6. Review malformed files, duplicate IDs, credential findings, and the scripts contained in imported Skills. Confirm only after reading them.

### 6. Push changes and resolve conflicts

- Prompt Keeper is review-first. It does not auto-commit, auto-push, auto-merge, or auto-write to agent directories.
- Use **Sync → Fetch**, review each change, then pull or push. Choose direct push or a branch plus pull request according to the repository policy.
- Resolve a conflict item by item. Never bulk-overwrite a drifted asset.
- If you resolve a Git conflict outside Prompt Keeper, preserve the frontmatter and the canonical file path.

### 7. Dispatch assets to agents

- Use Prompt Keeper's **Dispatch** workspace. Do not copy files into `~/.claude/skills`, `~/.codex/skills`, or an MCP config by hand.
- Drifted agent directories require item-by-item confirmation.
- This repository is a library, not a drop-in agent directory.

## Validation before commit

Run these checks from the repository root and fix every failure before staging.

```bash
# Empty asset files
find prompts instructions skills mcp -type f -size 0

# Empty SKILL.md files
find skills -name SKILL.md -exec sh -c 'test -s "$1" || echo "empty: $1"' _ {} \;

# Caches that must not be committed
find skills -type d \( -name node_modules -o -name .git -o -name .venv -o -name __pycache__ \)

# Credential-like filenames
find . -type f \( -name '.env' -o -name '.env.*' -o -name '*.pem' -o -name '*.key' -o -name 'id_rsa' \)

# High-signal token patterns
rg -n \
  -e 'BEGIN (RSA|OPENSSH|EC|DSA) PRIVATE KEY' \
  -e 'ghp_[A-Za-z0-9]{20,}' \
  -e 'github_pat_' \
  -e 'AKIA[0-9A-Z]{16}' \
  -e 'xox[baprs]-' \
  -e 'sk-(proj|ant)-' \
  . || true

# JSON syntax, when jq is available
find mcp -name '*.json' -print0 | xargs -0 -n1 jq empty

# Whitespace and conflict markers
git diff --check
```

Prompt Keeper's connect preflight is the authoritative validator for frontmatter and asset paths. A file that fails the preflight must not be committed as a synchronized asset.

## Security rules

- Repository MCP files contain only `${VAR}` placeholders.
- Real credential values stay in the local Prompt Keeper database, encrypted with Electron `safeStorage`.
- Never put tokens, passwords, production data, or private user data in commits, issue comments, or pull request descriptions.
- Do not weaken credential scanning or redaction to make a file pass.
- Never execute downloaded Skill scripts, MCP commands, package managers, or repository hooks on behalf of this library.
- Render Markdown from this repository through Prompt Keeper's sanitized renderer. Do not add raw HTML that a consumer might render.

## Git conventions

- Branch before changing published history. Never force-push `main`.
- Use Conventional Commit subjects in English: `feat:`, `fix:`, `docs:`, `refactor:`, `chore:`, `test:`.
- Keep the subject imperative, at or below 72 characters, without a trailing period.
- Keep each commit focused on one synchronization or format change.
- Do not commit `node_modules/`, caches, build output, logs, `.DS_Store`, or local-only files.
- Never use `git commit --no-verify`.

## Imported skills

### Personal skills

`skills/agents/` contains 59 personal Skills copied from `~/.agents/skills` on 2026-11-20. The source frontmatter is unchanged, so these Skills declare `name` and `description` rather than Prompt Keeper IDs. Prompt Keeper allocates an asset ID on first import and tracks each Skill by its repository path.

See [`docs/imported-skills.md`](./docs/imported-skills.md) for the complete inventory and import rules.

### chujianyun/skills

`skills/chujianyun/` contains 20 Skills imported from [chujianyun/skills](https://github.com/chujianyun/skills) at commit `0d765d5fafa22d57e267d7acea43cbd65ae7b996` on 2026-11-20. The source frontmatter is unchanged. These files are licensed under CC BY-NC-SA 4.0, not MIT; see [`THIRD_PARTY_NOTICES.md`](./THIRD_PARTY_NOTICES.md) and [`licenses/CC-BY-NC-SA-4.0.txt`](./licenses/CC-BY-NC-SA-4.0.txt).

The import contains 1,675 files and about 191 MB, mostly offline reference assets for the wiki and ontology Skills. See [`docs/imported-chujianyun-skills.md`](./docs/imported-chujianyun-skills.md) for the inventory and import rules.

### Notes for all imports

Some imported Skills contain scripts and non-English documentation. Prompt Keeper never executes bundled scripts; review them before dispatching. Skill content remains subject to the original authors' terms, so review the licenses before redistributing this repository.

## License

The repository scaffolding is MIT licensed. See [LICENSE](./LICENSE).

- Personal Skills under `skills/agents/` remain subject to the terms of their original authors.
- Skills under `skills/chujianyun/` are licensed CC BY-NC-SA 4.0. See [THIRD_PARTY_NOTICES.md](./THIRD_PARTY_NOTICES.md) and [licenses/CC-BY-NC-SA-4.0.txt](./licenses/CC-BY-NC-SA-4.0.txt).

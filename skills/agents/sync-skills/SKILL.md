---
name: sync-skills
description: Synchronize local Agent Skills between AI coding tools. Use when the user asks to sync, copy, mirror, propagate, or reconcile skills from the current AI programming tool into ~/.agents/skills and then into existing tool-specific skills directories such as Claude Code, Cursor, OpenCode, GitHub Copilot, Gemini CLI, Cline, Warp, Trae, Qoder, Kimi CLI, or Codex. Also use when the user asks where skills are installed or wants a dry run before syncing.
---

# Sync Skills

## Overview

Use the bundled script to synchronize skill folders safely across local AI coding tools.
The canonical hub is `~/.agents/skills`; the current tool's skills directory is copied into that hub first, then the hub is copied into any known tool-specific skills directories that already exist.

## Quick Start

Preview what would change:

```bash
python3 ~/.codex/skills/sync-skills/scripts/sync_skills.py
```

Apply non-destructive sync:

```bash
python3 ~/.codex/skills/sync-skills/scripts/sync_skills.py --apply
```

Apply and replace conflicting existing skill folders:

```bash
python3 ~/.codex/skills/sync-skills/scripts/sync_skills.py --apply --overwrite
```

## Workflow

1. Run a dry run first unless the user explicitly asked to apply changes immediately.
2. Review `copy`, `unchanged`, `conflict`, and `skip` lines.
3. If the user approves, rerun with `--apply`.
4. Use `--overwrite` only when the user wants the source/hub version to replace differing target copies.

## Defaults

- Source defaults to `$CODEX_HOME/skills` when set, otherwise `~/.codex/skills`.
- Hub defaults to `~/.agents/skills`.
- Targets are only used if their parent tool skills directory already exists.
- System skills and hidden folders are skipped by default.
- Existing target skills are never changed unless `--overwrite` is provided.

## Useful Options

```bash
python3 ~/.codex/skills/sync-skills/scripts/sync_skills.py --source ~/.claude/skills --apply
python3 ~/.codex/skills/sync-skills/scripts/sync_skills.py --include-system --apply
python3 ~/.codex/skills/sync-skills/scripts/sync_skills.py --targets ~/.claude/skills ~/.cursor/skills --apply
```

## Notes

This skill synchronizes Agent Skills only. MCP servers are configured per application and should not be copied into `~/.agents`.

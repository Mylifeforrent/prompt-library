---
id: ast_x492jngv6x6ssg
title: Commit Helper
description: Draft and validate Conventional Commit messages from a diff or change summary.
folder: engineering/git
tags:
  - git
  - commits
  - workflow
version: 1.1.0
author: Prompt Library
category: engineering
icon: GC
---
# Commit Helper

Use this skill when a change is ready to commit and you need a Conventional Commit message that a reviewer can scan quickly.

## Inputs

- The staged diff or an accurate description of the change.
- An optional scope such as `sync`, `prompts`, or `settings`.
- A note when the change breaks compatibility.

## Workflow

1. Read the diff and identify the primary intent. Do not describe every file.
2. Choose the type from `references/conventional-commits.md`.
3. Draft a subject in the imperative mood, at or below 72 characters, without a trailing period.
4. Add a body when the change needs context: what changed, why, and any migration step.
5. Mark a breaking change with `!` after the type or scope and describe the break in a `BREAKING CHANGE:` footer.
6. Validate the subject with `scripts/validate-subject.sh` before returning it.

## Output

Return the final message in a fenced text block, followed by one sentence that names the main risk a reviewer should check.

## References

- `references/conventional-commits.md` lists the supported types and rules.
- `scripts/validate-subject.sh` checks the subject shape. Prompt Keeper never executes bundled scripts; run it yourself when you copy this skill elsewhere.

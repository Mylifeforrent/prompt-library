---
id: ast_jh8o94vyi8r3fg
title: Collaboration Baseline
description: Default working agreement for every project that adopts these instructions.
folder: global
scope: project
pathPrefix: ''
activation:
  mode: always
  globs: []
priority: 40
imports: []
targetIds:
  - agents-md
  - claude
  - copilot
  - cursor
  - windsurf
tags:
  - collaboration
  - baseline
syncPolicy: inherit
---
# Collaboration Baseline

## Before changing code

- State the intended change and the files it will touch.
- Read the surrounding code and follow its existing conventions.
- Prefer the smallest change that solves the stated problem.

## While working

- Keep unrelated refactors out of the same change.
- Do not weaken validation, security checks, or error handling to make a test pass.
- Add or update tests whenever behavior changes.
- Never print secrets, tokens, or private user data in logs or responses.

## Before finishing

- Run the repository's documented build and test commands.
- Report what was verified and what was not.
- Call out assumptions, follow-ups, and known risks explicitly.

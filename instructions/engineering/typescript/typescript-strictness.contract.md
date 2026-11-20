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
    - "src/**/*.tsx"
priority: 60
imports: []
targetIds:
  - copilot-path
  - cursor
  - windsurf
tags:
  - typescript
  - quality
syncPolicy: inherit
---
# TypeScript Strictness

These rules apply to TypeScript sources under `src/`.

## Types

- Do not introduce `any` to silence a type error. Model the value or narrow it with `unknown`.
- Give exported functions and public types explicit return and parameter types.
- Parse external data at the boundary and convert it into a typed value before it reaches business logic.

## Modules

- Use `import type` for type-only imports.
- Keep shared types in the module that owns the concept instead of a catch-all types file.
- Avoid circular imports; move shared primitives downward in the dependency graph.

## Errors

- Throw typed errors with a stable code and a message that states the user-visible consequence.
- Never swallow an error without logging enough context to diagnose it.
- Do not leak stack traces or internal paths into user-facing output.

## Tests

- Every new branch in business logic needs a unit test.
- Integration tests must exercise the real persistence layer when the change touches storage.

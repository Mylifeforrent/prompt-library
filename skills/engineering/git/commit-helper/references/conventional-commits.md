# Conventional Commit Reference

## Types

| Type | Use for |
| --- | --- |
| `feat` | A new user-visible capability. |
| `fix` | A correction to broken behavior. |
| `docs` | Documentation, comments, or examples only. |
| `refactor` | A behavior-preserving code change. |
| `test` | Test coverage or test infrastructure only. |
| `perf` | A measurable performance improvement. |
| `build` | Build scripts, packaging, or dependencies. |
| `ci` | Continuous integration configuration. |
| `chore` | Repository maintenance that fits no other type. |

## Subject rules

- Use the imperative mood: `add`, `fix`, `remove`, not `added` or `fixes`.
- Keep the subject at or below 72 characters.
- Do not end the subject with a period.
- Use lowercase after the colon unless the word is a proper noun.

## Body rules

- Wrap the body at 72 characters.
- Explain why the change is needed, not what the diff already shows.
- Reference the issue or incident when one exists.

## Breaking changes

Add `!` after the type or scope, for example `feat(api)!: drop the legacy export`, and include a `BREAKING CHANGE:` footer that names the migration step.

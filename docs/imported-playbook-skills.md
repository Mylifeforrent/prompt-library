# Imported Skills from the Stage Playbook

- **Selection doc:** [skill-playbook-by-stage.md](./skill-playbook-by-stage.md)
- **Imported:** 2026-11-21
- **Destination:** `skills/<source>/<skill-name>/`
- **Count:** 113 skills, 1,920 files, about 44 MB
- **Method:** GitHub repository archives downloaded from `codeload.github.com` at the commits listed below. No Git metadata was copied.

## Sources

| Source | Ref | Skills | Files | Size | License |
| --- | --- | ---: | ---: | ---: | --- |
| [mattpocock/skills](https://github.com/mattpocock/skills) | `abeeaf9`, plus `v1.0.0` | 8 | 23 | 104 KB | MIT |
| [liangdabiao/market-insight-claude-skill](https://github.com/liangdabiao/market-insight-claude-skill) | `c996d2c` | 1 | 5 | 68 KB | No license file found |
| [1198560751/claude-skills-competitive-analysis-prd](https://github.com/1198560751/claude-skills-competitive-analysis-prd) | `9d753b2` | 1 | 4 | 64 KB | No license file found |
| [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | `2c60614` | 1 | 1 | 4 KB | MIT, declared in `SKILL.md` and `README.md` |
| [op7418/guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill) | `64d02d4` | 1 | 50 | 2.4 MB | AGPL-3.0 |
| [helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations) | `8961915` | 1 | 21 | 13 MB | MIT |
| [axtonliu/smart-illustrator](https://github.com/axtonliu/smart-illustrator) | `5140888` | 1 | 29 | 5.4 MB | MIT |
| [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | `bf1ff07` | 4 | 163 | 1.2 MB | MIT |
| [SpaceZephyr/design-buddy](https://github.com/SpaceZephyr/design-buddy) | `f1d835f` | 19 | 199 | 6.4 MB | MIT, declared in `README.md` |
| [ancoleman/ai-design-components](https://github.com/ancoleman/ai-design-components) | `76551b7` | 76 | 1,425 | 15 MB | MIT |

The `mattpocock/skills` commit is `abeeaf95660ba9e8b7c753eb38f441ca707a8823`. Two skills were removed from `main` after that repository's `v1.0.0` tag, so they were imported from `v1.0.0` (`bddb833cbaa322ff89d07e490530860aa73a4293`).

## Name mapping and upstream changes

Several names in the selection doc no longer match the upstream repositories. The table records what was actually imported.

| Selection doc name | Imported as | Note |
| --- | --- | --- |
| `write-a-prd` | `skills/mattpocock/to-spec` | Upstream renamed `to-prd` to `to-spec`. The current skill synthesizes an existing conversation into a spec; it does not run an interview. |
| `prd-to-plan` | `skills/mattpocock/to-tickets` | Upstream merged `to-plan` and `to-issues` into `to-tickets`. |
| `prd-to-issues` | `skills/mattpocock/to-tickets` | Same merge as above; `to-tickets` emits tracer-bullet tickets with blocking edges. |
| `design-an-interface` | `skills/mattpocock/design-an-interface` | Removed from `main`; imported from tag `v1.0.0` under `skills/deprecated/`. |
| `request-refactor-plan` | `skills/mattpocock/request-refactor-plan` | Removed from `main`; imported from tag `v1.0.0` under `skills/deprecated/`. |
| `market-insight-claude-skill` | `skills/liangdabiao/insight` | The repository contains a single skill named `insight`. |
| `andrej-karpathy-skills` | `skills/forrestchang/karpathy-guidelines` | The repository contains a single skill named `karpathy-guidelines`. |
| `design-buddy` | 19 `skills/SpaceZephyr/space-*` skills | The repository is a collection, not a single skill directory. |
| `ai-design-components` | 76 `skills/ancoleman/*` skills | The repository is a collection under `skills/`; all 76 were imported. |
| `baoyu-skills` | 4 `skills/JimLiu/*` skills | Imported `baoyu-slide-deck`, `baoyu-infographic`, `baoyu-post-to-wechat`, and the image backend dependency `baoyu-image-gen`. |

## Not imported

| Item | Reason |
| --- | --- |
| 「需求捕手」 | No public repository was provided or found. |
| `interview-conducting` | No skill exists at the named path. The repository contains a plugin-internal skill at `plugins/planning/skills/interview`, which depends on plugin-level `context/` and `reference/` files. Copying only the skill directory would leave those references broken, so it was not imported. |
| `pm-compete` | Not present in `Fokkyp/claude-skills` at the recorded commit. That repository contains only `competitive-analysis` and `prd-generator`. |
| `awesome-skills-zh`, `agent-skills-zh` | Indexes and localization libraries, not individual Skills. |
| `improve-codebase-architecture` | Already present at `skills/agents/improve-codebase-architecture`; the local copy differs from the current upstream and was left unchanged. |
| `prd-generator` | Already present at `skills/agents/prd-generator`; the local copy has extra `references/` and `scripts/` and was left unchanged. |
| `ui-ux-pro-max`, `frontend-design`, `vercel-react-best-practices`, `vercel-composition-patterns`, `find-skills` | Already present under `skills/agents/`; left unchanged to avoid duplicating or overwriting local variants. |
| `baoyu-article-illustrator`, `baoyu-cover-image` | Already present under `skills/agents/`; the upstream copies differ and were not overwritten. |

## Import rules

- Each Skill directory was copied in full from the upstream tree.
- `.git`, `node_modules`, `.venv`, `__pycache__`, tool caches, logs, and `.DS_Store` were excluded.
- Source files and frontmatter were preserved. No Prompt Keeper `id` or `folder` field was injected.
- No source files were modified.
- No symlinks were present in the imported trees.
- 66 files carry an executable bit. Prompt Keeper never executes bundled scripts; review a Skill before dispatching it to an agent directory.
- `skills/op7418/guizang-social-card-skill` and `skills/axtonliu/smart-illustrator` keep their repository-level files because the Skill lives at the repository root. This includes license, README, assets, and package metadata.
- `grill-me` calls the `grilling` Skill, which is already present at `skills/agents/grilling`.
- `grill-with-docs` calls `grilling` and `domain-modeling`; both are present.
- `to-spec` and `to-tickets` expect the imported `/setup-matt-pocock-skills` configuration. Run it once in the target repository before first use.
- `baoyu-slide-deck` and `baoyu-infographic` can use runtime-native image generation or the imported `baoyu-image-gen` backend.

## Inventory

### mattpocock/skills

| Skill | Files | Size |
| --- | ---: | ---: |
| grill-me | 2 | 8 KB |
| tdd | 4 | 16 KB |
| to-spec | 2 | 8 KB |
| to-tickets | 2 | 12 KB |
| design-an-interface | 1 | 4 KB |
| request-refactor-plan | 1 | 4 KB |
| domain-modeling | 4 | 16 KB |
| setup-matt-pocock-skills | 7 | 36 KB |

### liangdabiao/market-insight-claude-skill

| Skill | Files | Size |
| --- | ---: | ---: |
| insight | 5 | 68 KB |

### 1198560751/claude-skills-competitive-analysis-prd

| Skill | Files | Size |
| --- | ---: | ---: |
| competitive-analysis | 4 | 64 KB |

### forrestchang/andrej-karpathy-skills

| Skill | Files | Size |
| --- | ---: | ---: |
| karpathy-guidelines | 1 | 4 KB |

### op7418/guizang-social-card-skill

| Skill | Files | Size |
| --- | ---: | ---: |
| guizang-social-card-skill | 50 | 2.4 MB |

### helloianneo/ian-xiaohei-illustrations

| Skill | Files | Size |
| --- | ---: | ---: |
| ian-xiaohei-illustrations | 21 | 13 MB |

### axtonliu/smart-illustrator

| Skill | Files | Size |
| --- | ---: | ---: |
| smart-illustrator | 29 | 5.4 MB |

### JimLiu/baoyu-skills

| Skill | Files | Size |
| --- | ---: | ---: |
| baoyu-slide-deck | 35 | 176 KB |
| baoyu-infographic | 50 | 216 KB |
| baoyu-post-to-wechat | 29 | 360 KB |
| baoyu-image-gen | 49 | 460 KB |

### SpaceZephyr/design-buddy

| Skill | Files | Size |
| --- | ---: | ---: |
| space-ai-article-illustration | 5 | 36 KB |
| space-architecture-diagram | 3 | 60 KB |
| space-brand-ui-design | 2 | 16 KB |
| space-canvas-art | 83 | 5.6 MB |
| space-chart-html-plus | 7 | 56 KB |
| space-chart-html | 4 | 36 KB |
| space-chart-image | 5 | 48 KB |
| space-gemini-article-illustration | 4 | 28 KB |
| space-gemini-image | 1 | 4 KB |
| space-generative-art | 4 | 64 KB |
| space-image-skill-builder | 5 | 48 KB |
| space-image-studio | 20 | 100 KB |
| space-logo-generator | 4 | 28 KB |
| space-markdown-poster | 3 | 52 KB |
| space-mermaid-diagram | 2 | 12 KB |
| space-slide-deck | 37 | 216 KB |
| space-storyboard-generator | 4 | 28 KB |
| space-text-logic-diagram | 2 | 32 KB |
| space-wechat-layout | 4 | 20 KB |

### ancoleman/ai-design-components

| Skill | Files | Size |
| --- | ---: | ---: |
| administering-linux | 13 | 148 KB |
| ai-data-engineering | 27 | 284 KB |
| architecting-data | 14 | 124 KB |
| architecting-networks | 15 | 148 KB |
| architecting-security | 22 | 412 KB |
| assembling-components | 20 | 204 KB |
| building-ai-chat | 27 | 468 KB |
| building-ci-pipelines | 12 | 128 KB |
| building-clis | 20 | 156 KB |
| building-forms | 43 | 568 KB |
| building-tables | 32 | 336 KB |
| configuring-firewalls | 20 | 244 KB |
| configuring-nginx | 20 | 140 KB |
| creating-dashboards | 24 | 312 KB |
| debugging-techniques | 10 | 116 KB |
| deploying-applications | 19 | 216 KB |
| deploying-on-aws | 11 | 188 KB |
| deploying-on-azure | 14 | 152 KB |
| deploying-on-gcp | 11 | 160 KB |
| designing-apis | 13 | 124 KB |
| designing-distributed-systems | 22 | 228 KB |
| designing-layouts | 18 | 208 KB |
| designing-sdks | 18 | 144 KB |
| displaying-timelines | 33 | 164 KB |
| embedding-optimization | 11 | 168 KB |
| evaluating-llms | 18 | 292 KB |
| generating-documentation | 12 | 136 KB |
| guiding-users | 28 | 144 KB |
| implementing-api-patterns | 25 | 240 KB |
| implementing-compliance | 20 | 180 KB |
| implementing-drag-drop | 19 | 264 KB |
| implementing-gitops | 27 | 164 KB |
| implementing-mlops | 19 | 392 KB |
| implementing-navigation | 21 | 336 KB |
| implementing-observability | 17 | 228 KB |
| implementing-realtime-sync | 13 | 156 KB |
| implementing-search-filter | 21 | 348 KB |
| implementing-service-mesh | 14 | 172 KB |
| implementing-tls | 16 | 148 KB |
| ingesting-data | 11 | 84 KB |
| load-balancing-patterns | 21 | 200 KB |
| managing-configuration | 15 | 168 KB |
| managing-dns | 15 | 156 KB |
| managing-git-workflows | 12 | 140 KB |
| managing-incidents | 18 | 276 KB |
| managing-media | 41 | 204 KB |
| managing-vulnerabilities | 15 | 152 KB |
| model-serving | 21 | 196 KB |
| operating-kubernetes | 24 | 216 KB |
| optimizing-costs | 14 | 176 KB |
| optimizing-sql | 14 | 184 KB |
| performance-engineering | 14 | 148 KB |
| planning-disaster-recovery | 20 | 196 KB |
| platform-engineering | 11 | 172 KB |
| prompt-engineering | 15 | 276 KB |
| providing-feedback | 19 | 280 KB |
| resource-tagging | 10 | 168 KB |
| secret-management | 16 | 172 KB |
| securing-authentication | 13 | 216 KB |
| security-hardening | 14 | 160 KB |
| shell-scripting | 16 | 188 KB |
| siem-logging | 18 | 148 KB |
| streaming-data | 16 | 176 KB |
| testing-strategies | 15 | 160 KB |
| theming-components | 37 | 256 KB |
| transforming-data | 19 | 152 KB |
| using-document-databases | 20 | 224 KB |
| using-graph-databases | 11 | 168 KB |
| using-message-queues | 20 | 240 KB |
| using-relational-databases | 17 | 200 KB |
| using-timeseries-databases | 15 | 192 KB |
| using-vector-databases | 22 | 244 KB |
| visualizing-data | 44 | 344 KB |
| writing-dockerfiles | 16 | 180 KB |
| writing-github-actions | 16 | 156 KB |
| writing-infrastructure-code | 11 | 140 KB |

---
id: ast_t311ur19q3mjv2
title: Test Plan Writer
description: Build a risk-based test plan from a feature description and acceptance criteria.
folder: engineering/testing
tags:
  - testing
  - planning
version: 1.0.0
author: Prompt Library
category: engineering
icon: TP
---
# Test Plan Writer

Use this skill when a feature or change needs a test plan before implementation starts, or when a reviewer asks whether the proposed tests cover the real risk.

## Inputs

- The feature description or change summary.
- Acceptance criteria, if they exist.
- Known integrations, data stores, and user roles.

## Workflow

1. List the behaviors a user or caller can observe.
2. Rank the risks by impact and likelihood.
3. Map each risk to at least one test at the lowest layer that can catch it.
4. Separate automated coverage from manual checks.
5. Name the test data and environment each check needs.
6. Call out what will not be covered and why.

## Output

Return a Markdown test plan with these sections:

- Scope and non-goals.
- Risk table with impact, likelihood, and planned coverage.
- Automated tests grouped by unit, integration, and end-to-end.
- Manual checks with prerequisites.
- Gaps and follow-ups.

Keep every check executable by someone who did not write the plan. Avoid vague steps such as "verify it works".

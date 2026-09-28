# LinkedIn Sales Navigator (`linkedin.sales-navigator`)

Turn ICP into executable Sales Navigator practice: filter plans, Boolean strings, lead/account list design, saved-search cadence, and hygiene (dedupe, refresh, handoff). Tool-agnostic — describes what to run, verifies what's available, never invents filter names.

## Install

Copy `skills/sales-navigator/` into your agent skills folder. No dependencies.

## Quickstart

1. Read `SKILL.md` (reasoning) + `schema.json` (validation).
2. Supply inputs: `icp`.
3. Wire tools if available (search); otherwise analysis-only mode.
4. Validate output envelope (`data` + `provenance` with confidence/gaps).

## Compose

Consumes ICP; produces Search plan + lists → prospect-research, lead-qualification. See `SKILL.md → Chaining`.

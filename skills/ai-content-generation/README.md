# LinkedIn AI Content Generation (`linkedin.ai-content-generation`)

Draft posts machines can defend: expand content-creation briefs into full drafts where every claim traces to supplied proof, unknowns are slotted (not invented), and 2 format variants are offered. Groundedness over fluency.

## Install

Copy `skills/ai-content-generation/` into your agent skills folder. No dependencies.

## Quickstart

1. Read `SKILL.md` (reasoning) + `schema.json` (validation).
2. Supply inputs: `brief`.
3. Wire tools if available (none required); otherwise analysis-only mode.
4. Validate output envelope (`data` + `provenance` with confidence/gaps).

## Compose

Consumes Brief + proof + voice; produces ContentPost drafts → copywriting (polish), content-scheduling. See `SKILL.md → Chaining`.

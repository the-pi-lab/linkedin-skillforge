# LinkedIn B2B Prospecting (`linkedin.b2b-prospecting`)

Turn ICP + research into an executable prospecting book: tiered accounts, buying-committee personas, prioritized plays per tier, and entry-point recommendations — so outreach starts where win probability is highest.

## Install

Copy `skills/b2b-prospecting/` into your agent skills folder. No dependencies.

## Quickstart

1. Read `SKILL.md` (reasoning) + `schema.json` (validation).
2. Supply inputs: `icp`, `accounts`.
3. Wire tools if available (get_company, search); otherwise analysis-only mode.
4. Validate output envelope (`data` + `provenance` with confidence/gaps).

## Compose

Consumes ICP + accounts + research; produces Prospect queue → lead-qualification, ai-personalization. See `SKILL.md → Chaining`.

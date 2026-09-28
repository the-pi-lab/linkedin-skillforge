# LinkedIn Lead Qualification (`linkedin.lead-qualification`)

Separate signal from noise: score every lead on fit (ICP match) and intent (triggers, engagement), combine into a 0-1 priority with bands (now/nurture/disqualify), and give disqualify reasons — so outreach spends touches where they convert.

## Install

Copy `skills/lead-qualification/` into your agent skills folder. No dependencies.

## Quickstart

1. Read `SKILL.md` (reasoning) + `schema.json` (validation).
2. Supply inputs: `leads`, `icp`.
3. Wire tools if available (none required); otherwise analysis-only mode.
4. Validate output envelope (`data` + `provenance` with confidence/gaps).

## Compose

Consumes Lead[] + ICP + signals; produces Prospect[] → ai-personalization, cold-messaging, appointment-setting. See `SKILL.md → Chaining`.

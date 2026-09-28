# LinkedIn AI-Powered Personalization (`linkedin.ai-personalization`)

Make 'personalized' mean 'evidenced': take message templates + ResearchResults and fill each slot only from cited evidence, scoring slot-confidence and leaving unknowns empty with research tasks. Kills fake familiarity at the source.

## Install

Copy `skills/ai-personalization/` into your agent skills folder. No dependencies.

## Quickstart

1. Read `SKILL.md` (reasoning) + `schema.json` (validation).
2. Supply inputs: `template`, `dossiers`.
3. Wire tools if available (enrich_contact); otherwise analysis-only mode.
4. Validate output envelope (`data` + `provenance` with confidence/gaps).

## Compose

Consumes Template + ResearchResults; produces Personalized Messages → cold-messaging, outreach-automation. See `SKILL.md → Chaining`.

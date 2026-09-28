# LinkedIn Prospect Research (`linkedin.prospect-research`)

Answer 'who is this person/company and why now' with receipts: collect claims from profiles, company pages, and public sources; score each finding's confidence; separate facts from inferences; output a ResearchResult dossier that downstream personalization and qualification can trust.

## Install

Copy `skills/prospect-research/` into your agent skills folder. No dependencies.

## Quickstart

1. Read `SKILL.md` (reasoning) + `schema.json` (validation).
2. Supply inputs: `subject`.
3. Wire tools if available (get_profile, get_company, search); otherwise analysis-only mode.
4. Validate output envelope (`data` + `provenance` with confidence/gaps).

## Compose

Consumes Lead + subject identifier; produces ResearchResult → lead-qualification, ai-personalization, b2b-prospecting. See `SKILL.md → Chaining`.

# LinkedIn Lead Generation (`linkedin.lead-generation`)

Produce qualified top-of-funnel supply: formalize ICP, define list-building rules (titles, geos, signals, exclusions), emit deduped Lead[] with source_refs and handoff contract for prospect-research/qualification. Quantity never outruns definitional clarity.

## Install

Copy `skills/lead-generation/` into your agent skills folder. No dependencies.

## Quickstart

1. Read `SKILL.md` (reasoning) + `schema.json` (validation).
2. Supply inputs: `offer`, `icp_hints`.
3. Wire tools if available (search, get_profile); otherwise analysis-only mode.
4. Validate output envelope (`data` + `provenance` with confidence/gaps).

## Compose

Consumes Offer + ICP hints; produces ICP + Lead[] → prospect-research, lead-qualification, sales-navigator. See `SKILL.md → Chaining`.

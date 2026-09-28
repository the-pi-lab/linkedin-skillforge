# LinkedIn Data Enrichment (`linkedin.data-enrichment`)

Complete partial records responsibly: for each missing field, find candidate values from allowed sources, score per-field confidence, and return filled + unfilled partitions with provenance — so downstream skills consume only what is evidenced.

## Install

Copy `skills/data-enrichment/` into your agent skills folder. No dependencies.

## Quickstart

1. Read `SKILL.md` (reasoning) + `schema.json` (validation).
2. Supply inputs: `records`, `fields_wanted`.
3. Wire tools if available (enrich_contact, get_profile, get_company); otherwise analysis-only mode.
4. Validate output envelope (`data` + `provenance` with confidence/gaps).

## Compose

Consumes Partial records; produces Enriched Person/Lead → lead-qualification, crm-integration. See `SKILL.md → Chaining`.

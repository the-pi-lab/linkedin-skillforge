# LinkedIn Sales Funnel Building (`linkedin.sales-funnel`)

Architect the journey from first touch to closed/won for LinkedIn-sourced deals: stages, entry/exit criteria, required artifacts, SLAs, and CRM handoffs — so volume, velocity, and leakage are all measurable.

## Install

Copy `skills/sales-funnel/` into your agent skills folder. No dependencies.

## Quickstart

1. Read `SKILL.md` (reasoning) + `schema.json` (validation).
2. Supply inputs: `motion`.
3. Wire tools if available (create_crm_record); otherwise analysis-only mode.
4. Validate output envelope (`data` + `provenance` with confidence/gaps).

## Compose

Consumes Motion + capacity; produces Funnel + metrics → crm-integration, analytics-reporting. See `SKILL.md → Chaining`.

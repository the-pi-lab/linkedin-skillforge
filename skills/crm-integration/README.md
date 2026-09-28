# LinkedIn CRM Integration (`linkedin.crm-integration`)

Keep CRM truthful: field-map LinkedIn entities (leads, prospects, conversations, appointments) to CRM objects with dedupe keys, conflict rules, sync direction, and receipted writes — so sales and reporting trust the data.

## Install

Copy `skills/crm-integration/` into your agent skills folder. No dependencies.

## Quickstart

1. Read `SKILL.md` (reasoning) + `schema.json` (validation).
2. Supply inputs: `entities`, `crm`.
3. Wire tools if available (create_crm_record); otherwise analysis-only mode.
4. Validate output envelope (`data` + `provenance` with confidence/gaps).

## Compose

Consumes LinkedIn entities (Lead/Prospect/Conversation/Appointment); produces CRMRecord maps → analytics-reporting, workflow-automation. See `SKILL.md → Chaining`.

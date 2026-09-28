# LinkedIn Workflow Automation (`linkedin.workflow-automation`)

Make automation reliable: formalize any LinkedIn workflow as trigger → steps → guards with retries, idempotency keys, dedupe, SLAs, and audit logging — executable by engineers and reviewable by automation-compliance.

## Install

Copy `skills/workflow-automation/` into your agent skills folder. No dependencies.

## Quickstart

1. Read `SKILL.md` (reasoning) + `schema.json` (validation).
2. Supply inputs: `process`, `systems`, `constraints`.
3. Wire tools if available (create_crm_record, schedule_post); otherwise analysis-only mode.
4. Validate output envelope (`data` + `provenance` with confidence/gaps).

## Compose

Consumes Process + systems; produces AutomationWorkflow → ai-agent-development, automation-compliance, api-integration. See `SKILL.md → Chaining`.

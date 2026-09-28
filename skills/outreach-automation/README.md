# LinkedIn Outreach Automation (`linkedin.outreach-automation`)

Design outreach that scales without spamming: multi-step sequences (connection → value → ask) with per-step guards (confidence thresholds, caps, opt-out, human approval), exit rules, and audit logging. Prefers approved paths; anything risky routes to automation-compliance.

## Install

Copy `skills/outreach-automation/` into your agent skills folder. No dependencies.

## Quickstart

1. Read `SKILL.md` (reasoning) + `schema.json` (validation).
2. Supply inputs: `audience`, `offer`, `constraints`.
3. Wire tools if available (send_message); otherwise analysis-only mode.
4. Validate output envelope (`data` + `provenance` with confidence/gaps).

## Compose

Consumes Prospect tiers + offer; produces Campaign sequence → cold-messaging (executes copy), automation-compliance (scores). See `SKILL.md → Chaining`.

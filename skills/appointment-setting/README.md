# LinkedIn Appointment Setting (`linkedin.appointment-setting`)

Turn interest into calendar: qualify lightly, offer constrained slots, confirm with agenda, remind, handle reschedules, and log outcomes — maximizing hold-rate while respecting the prospect's time and consent.

## Install

Copy `skills/appointment-setting/` into your agent skills folder. No dependencies.

## Quickstart

1. Read `SKILL.md` (reasoning) + `schema.json` (validation).
2. Supply inputs: `conversation`, `calendar`.
3. Wire tools if available (create_appointment, send_message); otherwise analysis-only mode.
4. Validate output envelope (`data` + `provenance` with confidence/gaps).

## Compose

Consumes Conversation + calendar; produces Appointment → crm-integration, email-outreach-integration. See `SKILL.md → Chaining`.

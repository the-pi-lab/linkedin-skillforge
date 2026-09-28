# LinkedIn Email Outreach Integration (`linkedin.email-outreach-integration`)

Orchestrate the two channels as one conversation: decide which steps live where, keep identity/message consistent, protect deliverability (volume, warmup, list quality), and dedupe/suppress across channels with unified opt-out.

## Install

Copy `skills/email-outreach-integration/` into your agent skills folder. No dependencies.

## Quickstart

1. Read `SKILL.md` (reasoning) + `schema.json` (validation).
2. Supply inputs: `audience`, `assets`.
3. Wire tools if available (send_message); otherwise analysis-only mode.
4. Validate output envelope (`data` + `provenance` with confidence/gaps).

## Compose

Consumes Prospects + per-channel messages; produces Unified sequence → outreach-automation, appointment-setting. See `SKILL.md → Chaining`.

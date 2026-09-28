# LinkedIn Cold Messaging (`linkedin.cold-messaging`)

Write cold messages that earn replies: one idea per message, prospect-specific opener from dossier evidence, value in recipient terms, singular low-friction CTA, graceful follow-ups. Every claim traceable; confidence gates sending.

## Install

Copy `skills/cold-messaging/` into your agent skills folder. No dependencies.

## Quickstart

1. Read `SKILL.md` (reasoning) + `schema.json` (validation).
2. Supply inputs: `prospect`, `offer`.
3. Wire tools if available (send_message); otherwise analysis-only mode.
4. Validate output envelope (`data` + `provenance` with confidence/gaps).

## Compose

Consumes Prospect dossier + offer; produces Message variants → outreach-automation, appointment-setting. See `SKILL.md → Chaining`.

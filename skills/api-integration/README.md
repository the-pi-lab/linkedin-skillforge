# LinkedIn API Integration (`linkedin.api-integration`)

Connect systems correctly: map desired LinkedIn operations to official API surfaces (or approved partners), design auth, error handling, retries, rate-limit behavior, and data mapping — and say plainly when no official path exists instead of inventing one.

## Install

Copy `skills/api-integration/` into your agent skills folder. No dependencies.

## Quickstart

1. Read `SKILL.md` (reasoning) + `schema.json` (validation).
2. Supply inputs: `workflow`, `stack`.
3. Wire tools if available (none required); otherwise analysis-only mode.
4. Validate output envelope (`data` + `provenance` with confidence/gaps).

## Compose

Consumes Desired operations; produces Integration map → workflow-automation, ai-agent-development. See `SKILL.md → Chaining`.

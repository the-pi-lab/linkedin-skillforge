# LinkedIn Social Selling (`linkedin.social-selling`)

Sell through usefulness: monitor buyer triggers (posts, job changes, hiring), engage with substantive comments, then transition warm conversations to discovery — with clear rules for when NOT to pitch.

## Install

Copy `skills/social-selling/` into your agent skills folder. No dependencies.

## Quickstart

1. Read `SKILL.md` (reasoning) + `schema.json` (validation).
2. Supply inputs: `accounts`, `offer`.
3. Wire tools if available (get_profile, search); otherwise analysis-only mode.
4. Validate output envelope (`data` + `provenance` with confidence/gaps).

## Compose

Consumes Accounts + triggers; produces Warm conversations → cold-messaging (transition), appointment-setting. See `SKILL.md → Chaining`.

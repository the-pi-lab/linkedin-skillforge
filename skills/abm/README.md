# LinkedIn Account-Based Marketing (`linkedin.abm`)

Focus go-to-market on accounts that matter: tier named accounts (strategic/scale/programmatic), map committees, assign plays per tier (1:1, 1:few, 1:many), and define account-level metrics — so marketing + sales row in the same direction.

## Install

Copy `skills/abm/` into your agent skills folder. No dependencies.

## Quickstart

1. Read `SKILL.md` (reasoning) + `schema.json` (validation).
2. Supply inputs: `accounts`, `icp`.
3. Wire tools if available (get_company, search); otherwise analysis-only mode.
4. Validate output envelope (`data` + `provenance` with confidence/gaps).

## Compose

Consumes Accounts + ICP; produces ABM plan → ads-management, outreach-automation, market-research. See `SKILL.md → Chaining`.

# LinkedIn Ads Management (`linkedin.ads-management`)

Launch ads worth their spend: translate offer + ICP into campaign objective, audience, creative variants, bidding/budget, and measurement — with human approval gates and policy compliance before any dollar moves.

## Install

Copy `skills/ads-management/` into your agent skills folder. No dependencies.

## Quickstart

1. Read `SKILL.md` (reasoning) + `schema.json` (validation).
2. Supply inputs: `offer`, `audience`, `budget`.
3. Wire tools if available (manage_ads); otherwise analysis-only mode.
4. Validate output envelope (`data` + `provenance` with confidence/gaps).

## Compose

Consumes Offer + ICP + budget; produces Campaign → campaign-optimization, conversion-tracking. See `SKILL.md → Chaining`.

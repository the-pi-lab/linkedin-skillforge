# LinkedIn Campaign Optimization (`linkedin.campaign-optimization`)

Fix paid performance methodically: decompose funnel (delivery→CTR→CVR→CPL→pipeline), isolate the binding constraint, prescribe one-variable tests in sequence — stopping losers fast and scaling winners with guardrails.

## Install

Copy `skills/campaign-optimization/` into your agent skills folder. No dependencies.

## Quickstart

1. Read `SKILL.md` (reasoning) + `schema.json` (validation).
2. Supply inputs: `metrics`, `goals`.
3. Wire tools if available (get_analytics, manage_ads); otherwise analysis-only mode.
4. Validate output envelope (`data` + `provenance` with confidence/gaps).

## Compose

Consumes Campaign metrics; produces Tuned Campaign → ads-management, analytics-reporting. See `SKILL.md → Chaining`.

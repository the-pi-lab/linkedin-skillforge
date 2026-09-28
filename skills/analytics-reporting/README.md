# LinkedIn Analytics and Reporting (`linkedin.analytics-reporting`)

Close the loop: ingest metrics (content, outreach, funnel, ads), attribute honestly within data limits, surface 3-5 insights with evidence, and recommend next actions with expected effects — reported at stakeholder-appropriate depth.

## Install

Copy `skills/analytics-reporting/` into your agent skills folder. No dependencies.

## Quickstart

1. Read `SKILL.md` (reasoning) + `schema.json` (validation).
2. Supply inputs: `metrics`.
3. Wire tools if available (get_analytics, track_conversion); otherwise analysis-only mode.
4. Validate output envelope (`data` + `provenance` with confidence/gaps).

## Compose

Consumes Metrics + goals; produces AnalyticsReport → growth-strategy, campaign-optimization, content-scheduling. See `SKILL.md → Chaining`.

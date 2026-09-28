# LinkedIn Job Search Optimization (`linkedin.job-search-optimization`)

Run job search like a campaign: define target roles/companies, audit fit gaps, optimize profile for recruiters, plan networking + application sequencing, and track funnel (applied → screen → offer) — honest positioning, no credential inflation.

## Install

Copy `skills/job-search-optimization/` into your agent skills folder. No dependencies.

## Quickstart

1. Read `SKILL.md` (reasoning) + `schema.json` (validation).
2. Supply inputs: `background`, `targets`.
3. Wire tools if available (search, get_profile); otherwise analysis-only mode.
4. Validate output envelope (`data` + `provenance` with confidence/gaps).

## Compose

Consumes Background + targets; produces Job campaign → profile-optimization, networking. See `SKILL.md → Chaining`.

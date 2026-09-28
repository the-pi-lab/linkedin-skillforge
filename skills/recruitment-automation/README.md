# LinkedIn Recruitment Automation (`linkedin.recruitment-automation`)

Hire faster without hiring worse: convert JD into sourcing plan, structured screens, scorecards, and stage automation with human decision gates and bias guards — efficiency on logistics, rigor on judgment.

## Install

Copy `skills/recruitment-automation/` into your agent skills folder. No dependencies.

## Quickstart

1. Read `SKILL.md` (reasoning) + `schema.json` (validation).
2. Supply inputs: `role`, `constraints`.
3. Wire tools if available (search, get_profile); otherwise analysis-only mode.
4. Validate output envelope (`data` + `provenance` with confidence/gaps).

## Compose

Consumes Role + constraints; produces Pipeline → job-search-optimization (mirror), employer-branding. See `SKILL.md → Chaining`.

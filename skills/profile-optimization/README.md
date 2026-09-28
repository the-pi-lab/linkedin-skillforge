# LinkedIn Profile Optimization (`linkedin.profile-optimization`)

Turn a LinkedIn profile into a credible, searchable, conversion-ready asset. Audits headline, about, experience, skills, featured, and custom sections against a 100-point rubric, then produces prioritized rewrites with before/after diffs and evidence-based rationale — never generic advice.

## Install

Copy `skills/profile-optimization/` into your agent skills folder. No dependencies.

## Quickstart

1. Read `SKILL.md` (reasoning) + `schema.json` (validation).
2. Supply inputs: `profile_text`, `target_audience`, `target_outcome`.
3. Wire tools if available (get_profile); otherwise analysis-only mode.
4. Validate output envelope (`data` + `provenance` with confidence/gaps).

## Compose

Consumes LinkedInProfile text/handle + audience definition; produces LinkedInProfile audit + rewrites → personal-branding, linkedin-seo, social-selling. See `SKILL.md → Chaining`.

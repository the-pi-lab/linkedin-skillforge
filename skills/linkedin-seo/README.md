# LinkedIn SEO (`linkedin.linkedin-seo`)

Make the right people find the profile: build a keyword map from audience search language, assign each term to exactly one profile section (headline, about, experience, skills), and verify placement without stuffing. Covers LinkedIn search + public Google indexing.

## Install

Copy `skills/linkedin-seo/` into your agent skills folder. No dependencies.

## Quickstart

1. Read `SKILL.md` (reasoning) + `schema.json` (validation).
2. Supply inputs: `audience`, `profile`.
3. Wire tools if available (search, get_profile); otherwise analysis-only mode.
4. Validate output envelope (`data` + `provenance` with confidence/gaps).

## Compose

Consumes Audience queries + profile; produces Keyword map → profile-optimization (applies edits). See `SKILL.md → Chaining`.

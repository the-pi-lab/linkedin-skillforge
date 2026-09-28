# LinkedIn Content Scheduling (`linkedin.content-scheduling`)

Ship consistently: turn approved ContentPosts into a calendar with slot selection (audience hours x pillar mix x format variety), pre-flight QA, scheduling receipts, and fallback rules for gaps.

## Install

Copy `skills/content-scheduling/` into your agent skills folder. No dependencies.

## Quickstart

1. Read `SKILL.md` (reasoning) + `schema.json` (validation).
2. Supply inputs: `posts`, `windows`.
3. Wire tools if available (schedule_post, post_content); otherwise analysis-only mode.
4. Validate output envelope (`data` + `provenance` with confidence/gaps).

## Compose

Consumes ContentPost[] + windows; produces Calendar → analytics-reporting (measures), engagement-strategy. See `SKILL.md → Chaining`.

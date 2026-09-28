# LinkedIn Content Creation (`linkedin.content-creation`)

Bridge brand strategy and publishable posts: generate ContentIdeas from pillars, score them, expand winners into structured briefs (hook, beats, CTA, format) that copywriting/ai-content-generation execute. Separates ideation quality from prose quality.

## Install

Copy `skills/content-creation/` into your agent skills folder. No dependencies.

## Quickstart

1. Read `SKILL.md` (reasoning) + `schema.json` (validation).
2. Supply inputs: `pillars`, `audience`.
3. Wire tools if available (none required); otherwise analysis-only mode.
4. Validate output envelope (`data` + `provenance` with confidence/gaps).

## Compose

Consumes Brand pillars + audience + proof; produces ContentIdea[] + briefs → ai-content-generation, copywriting, content-scheduling. See `SKILL.md → Chaining`.

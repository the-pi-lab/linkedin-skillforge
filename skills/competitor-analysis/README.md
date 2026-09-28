# LinkedIn Competitor Analysis (`linkedin.competitor-analysis`)

Find winnable ground: profile top competitors' LinkedIn presence (positioning, content, engagement, proof), score their jobs-to-be-done coverage, and output gaps + countermoves with evidence — never scraping restricted data.

## Install

Copy `skills/competitor-analysis/` into your agent skills folder. No dependencies.

## Quickstart

1. Read `SKILL.md` (reasoning) + `schema.json` (validation).
2. Supply inputs: `competitors`.
3. Wire tools if available (get_company, get_profile, search); otherwise analysis-only mode.
4. Validate output envelope (`data` + `provenance` with confidence/gaps).

## Compose

Consumes Competitor list; produces ResearchResult → market-research, content-creation, abm. See `SKILL.md → Chaining`.

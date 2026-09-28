# LinkedIn Market Research (`linkedin.market-research`)

Ground strategy in evidence: define segments, collect pain/signal evidence from LinkedIn + public sources, estimate opportunity (size x pain x reachability), and rank bets — with every claim cited and limits stated.

## Install

Copy `skills/market-research/` into your agent skills folder. No dependencies.

## Quickstart

1. Read `SKILL.md` (reasoning) + `schema.json` (validation).
2. Supply inputs: `domain`, `questions`.
3. Wire tools if available (search, get_company); otherwise analysis-only mode.
4. Validate output envelope (`data` + `provenance` with confidence/gaps).

## Compose

Consumes Domain + questions; produces ResearchResult → abm, content-creation, growth-strategy. See `SKILL.md → Chaining`.

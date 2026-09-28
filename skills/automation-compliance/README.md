# LinkedIn Automation Compliance (`linkedin.automation-compliance`)

Keep automation legitimate: evaluate any proposed LinkedIn workflow (sequence, agent, integration, scraping plan) against platform rules and risk factors, score severity, and return a verdict — approved with guards, needs-review, or blocked — plus fix list. The repo's safety gate.

## Install

Copy `skills/automation-compliance/` into your agent skills folder. No dependencies.

## Quickstart

1. Read `SKILL.md` (reasoning) + `schema.json` (validation).
2. Supply inputs: `workflow`.
3. Wire tools if available (none required); otherwise analysis-only mode.
4. Validate output envelope (`data` + `provenance` with confidence/gaps).

## Compose

Consumes Any proposed workflow; produces Verdict + fixes → all automation skills (gate). See `SKILL.md → Chaining`.

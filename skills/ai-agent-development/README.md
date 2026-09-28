# LinkedIn AI Agent Development (`linkedin.ai-agent-development`)

Turn an automation wish into a buildable agent spec: bounded scope, tool bindings (abstract interfaces), guard rails, eval suite, rollout stages — so engineers can implement without discovering safety requirements mid-build.

## Install

Copy `skills/ai-agent-development/` into your agent skills folder. No dependencies.

## Quickstart

1. Read `SKILL.md` (reasoning) + `schema.json` (validation).
2. Supply inputs: `job`, `tools_available`, `constraints`.
3. Wire tools if available (none required); otherwise analysis-only mode.
4. Validate output envelope (`data` + `provenance` with confidence/gaps).

## Compose

Consumes Job + tool inventory; produces Agent spec → workflow-automation, api-integration, automation-compliance. See `SKILL.md → Chaining`.

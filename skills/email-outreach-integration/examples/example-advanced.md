# LinkedIn Email Outreach Integration — Advanced / composition example

## Scenario

Weak consent + new domain: LinkedIn-first with email held to opt-ins.

## Input

```json
{"audience": "purchased list?", "infra": "new domain"}
```

## Output (abridged)

```json
{"data": {"sequence": "LI-only pilot + warmup"}, "provenance": {"confidence": 0.55, "gaps": ["consent", "warmup"]}}
```

Notes: demonstrates Unified sequence → outreach-automation, appointment-setting consumed downstream, degraded confidence on gaps, no fabricated facts.

# LinkedIn Outreach Automation — Advanced / composition example

## Scenario

User demands autonomous 500/day: refused, replaced with gated 50-pilot + compliance checkpoint.

## Input

```json
{"audience": "broad list", "constraints": "500/day autonomous"}
```

## Output (abridged)

```json
{"data": {"sequence": "pilot-50 gated", "refusal_note": "uncapped autonomous refused"}, "provenance": {"confidence": 0.5, "gaps": ["ICP precision"]}}
```

Notes: demonstrates Campaign sequence → cold-messaging (executes copy), automation-compliance (scores) consumed downstream, degraded confidence on gaps, no fabricated facts.

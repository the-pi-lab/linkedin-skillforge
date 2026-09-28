# LinkedIn Appointment Setting — Advanced / composition example

## Scenario

No-show: blameless rescue with 2 re-offers + async fallback, outcome logged.

## Input

```json
{"conversation": "no-show first slot"}
```

## Output (abridged)

```json
{"data": {"followup": ["rescue-1", "async option"]}}, "provenance": {"confidence": 0.7, "gaps": []}}
```

Notes: demonstrates Appointment → crm-integration, email-outreach-integration consumed downstream, degraded confidence on gaps, no fabricated facts.

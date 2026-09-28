# LinkedIn Sales Funnel Building — Advanced / composition example

## Scenario

Leaky discovery stage: entry tightened with required artifacts instead of new stages.

## Input

```json
{"motion": "outbound", "stages_current": "7 vague stages"}
```

## Output (abridged)

```json
{"data": {"funnel": ["4 gated stages"], "fix": "entry criteria"}, "provenance": {"confidence": 0.7, "gaps": ["baseline conversion"]}}
```

Notes: demonstrates Funnel + metrics → crm-integration, analytics-reporting consumed downstream, degraded confidence on gaps, no fabricated facts.

# LinkedIn Campaign Optimization — Advanced / composition example

## Scenario

Thin spend: no verdict, extended test with kill thresholds instead.

## Input

```json
{"metrics": {"spend": "$40", "clicks": 12}}
```

## Output (abridged)

```json
{"data": {"diagnosis": "insufficient n", "test_plan": "extend to $300"}}, "provenance": {"confidence": 0.5, "gaps": ["sample"]}}
```

Notes: demonstrates Tuned Campaign → ads-management, analytics-reporting consumed downstream, degraded confidence on gaps, no fabricated facts.

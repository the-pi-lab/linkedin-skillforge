# LinkedIn Content Scheduling — Advanced / composition example

## Scenario

No scheduler tool: manual SOP with pre-flight checklist and tentative holds.

## Input

```json
{"posts": ["2 approved"], "windows": "unknown"}
```

## Output (abridged)

```json
{"data": {"calendar": "manual SOP", "receipts": []}, "provenance": {"confidence": 0.6, "gaps": ["scheduler", "audience hours"]}}
```

Notes: demonstrates Calendar → analytics-reporting (measures), engagement-strategy consumed downstream, degraded confidence on gaps, no fabricated facts.

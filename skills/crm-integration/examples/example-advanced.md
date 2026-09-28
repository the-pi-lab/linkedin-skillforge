# LinkedIn CRM Integration — Advanced / composition example

## Scenario

Key collision on email: review-queue + source-priority merge instead of auto-overwrite.

## Input

```json
{"entities": ["Prospect"], "crm": "Salesforce", "rules": "strict dedupe"}
```

## Output (abridged)

```json
{"data": {"mapping": {}, "conflicts": "review-queue"}, "provenance": {"confidence": 0.7, "gaps": ["match sample"]}}
```

Notes: demonstrates CRMRecord maps → analytics-reporting, workflow-automation consumed downstream, degraded confidence on gaps, no fabricated facts.

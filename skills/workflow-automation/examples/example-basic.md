# LinkedIn Workflow Automation — Basic example

## Input

```json
{"process": "new connect → CRM → follow-up", "systems": ["CRM"], "constraints": "human-gate sends"}
```

## Output (abridged)

```json
{"data": {"workflow": {"trigger": "new-connection", "steps": ["dedupe", "crm-create", "gated-followup"]}}, "provenance": {"producer_skill": "linkedin.workflow-automation", "confidence": 0.8, "gaps": []}}
```

Notes: fictitious data. Confidence reflects evidence present; gaps list what was missing.

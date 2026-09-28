# LinkedIn Workflow Automation — Advanced / composition example

## Scenario

Duplicate-send risk: dedupe + idempotency added before any send node.

## Input

```json
{"process": "auto-follow-up sequence"}
```

## Output (abridged)

```json
{"data": {"workflow": {"guards": ["opt-out", "dedupe"], "idempotency": "thread+step key"}}, "provenance": {"confidence": 0.7, "gaps": ["volume"]}}
```

Notes: demonstrates AutomationWorkflow → ai-agent-development, automation-compliance, api-integration consumed downstream, degraded confidence on gaps, no fabricated facts.

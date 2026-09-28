# LinkedIn API Integration — Advanced / composition example

## Scenario

Requested op with no official path: declined with compliant alternative.

## Input

```json
{"workflow": "bulk auto-DM endpoint"}
```

## Output (abridged)

```json
{"data": {"integration": "no official path; gated manual alternative"}}, "provenance": {"confidence": 0.6, "gaps": ["partner approval"]}}
```

Notes: demonstrates Integration map → workflow-automation, ai-agent-development consumed downstream, degraded confidence on gaps, no fabricated facts.

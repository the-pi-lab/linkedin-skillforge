# LinkedIn AI Agent Development — Advanced / composition example

## Scenario

Autonomous outreach request: downgraded to gated pilot with eval gates.

## Input

```json
{"job": "autonomous outreach", "tools_available": ["send_message"]}
```

## Output (abridged)

```json
{"data": {"agent_spec": {"mode": "human-gated pilot"}, "rollout": ["read-only", "gated-50"]}, "provenance": {"confidence": 0.6, "gaps": ["approval policy"]}}
```

Notes: demonstrates Agent spec → workflow-automation, api-integration, automation-compliance consumed downstream, degraded confidence on gaps, no fabricated facts.

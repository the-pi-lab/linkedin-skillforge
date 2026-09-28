# LinkedIn AI Agent Development — Basic example

## Input

```json
{"job": "draft comments for review", "tools_available": ["get_profile"], "constraints": "no auto-post"}
```

## Output (abridged)

```json
{"data": {"agent_spec": {"scope": "draft-only", "gates": ["human approves all posts"]}}, "provenance": {"producer_skill": "linkedin.ai-agent-development", "confidence": 0.82, "gaps": []}}
```

Notes: fictitious data. Confidence reflects evidence present; gaps list what was missing.

# LinkedIn Cold Messaging — Advanced / composition example

## Scenario

Thin dossier: honest short opener with slots + research task instead of fake hook.

## Input

```json
{"prospect": "name + title only", "offer": "audit tool"}
```

## Output (abridged)

```json
{"data": {"messages": [{"body": "Quick question on {{stack:verify}}..."}]}, "provenance": {"confidence": 0.55, "gaps": ["trigger evidence"]}}
```

Notes: demonstrates Message variants → outreach-automation, appointment-setting consumed downstream, degraded confidence on gaps, no fabricated facts.

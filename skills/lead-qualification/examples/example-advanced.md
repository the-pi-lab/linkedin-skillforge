# LinkedIn Lead Qualification — Advanced / composition example

## Scenario

High fit, zero intent: nurture band with trigger-watch tasks.

## Input

```json
{"leads": ["perfect-fit, silent account"]}
```

## Output (abridged)

```json
{"data": {"prospects": [{"band": "nurture", "watch": ["hiring", "posts"]}]}, "provenance": {"confidence": 0.65, "gaps": ["intent"]}}
```

Notes: demonstrates Prospect[] → ai-personalization, cold-messaging, appointment-setting consumed downstream, degraded confidence on gaps, no fabricated facts.

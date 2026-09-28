# LinkedIn AI-Powered Personalization — Advanced / composition example

## Scenario

No evidence for key slot: held with research task, honest fallback used.

## Input

```json
{"template": "Loved your {{keynote}}...", "dossiers": ["no keynote found"]}
```

## Output (abridged)

```json
{"data": {"personalized": [{"body": "Quick question on {{stack}}...", "held": ["keynote"]}]}, "provenance": {"confidence": 0.55, "gaps": ["keynote evidence"]}}
```

Notes: demonstrates Personalized Messages → cold-messaging, outreach-automation consumed downstream, degraded confidence on gaps, no fabricated facts.

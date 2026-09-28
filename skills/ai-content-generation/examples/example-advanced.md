# LinkedIn AI Content Generation — Advanced / composition example

## Scenario

Bold claim without proof: draft reframes as question + slot for data.

## Input

```json
{"brief": "10x claim", "proof": "none"}
```

## Output (abridged)

```json
{"data": {"drafts": [{"body": "Are multi-touch bumps worth it? Our early reads... {{pilot_n}}"}]}, "provenance": {"confidence": 0.55, "gaps": ["supporting data"]}}
```

Notes: demonstrates ContentPost drafts → copywriting (polish), content-scheduling consumed downstream, degraded confidence on gaps, no fabricated facts.

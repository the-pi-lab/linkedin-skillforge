# LinkedIn B2B Prospecting — Advanced / composition example

## Scenario

No intent signals anywhere: all accounts capped at B with research tasks to unlock A-tier.

## Input

```json
{"icp": {}, "accounts": ["X","Y","Z"]}
```

## Output (abridged)

```json
{"data": {"tiers": {"B": ["X","Y","Z"], "A": []}}, "provenance": {"confidence": 0.55, "gaps": ["triggers"]}}
```

Notes: demonstrates Prospect queue → lead-qualification, ai-personalization consumed downstream, degraded confidence on gaps, no fabricated facts.

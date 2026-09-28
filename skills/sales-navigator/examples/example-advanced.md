# LinkedIn Sales Navigator — Advanced / composition example

## Scenario

Unknown tier + oversized results; plan splits lists and marks tier assumptions for confirmation.

## Input

```json
{"icp": {"titles": ["Revenue leaders"]}, "navigator_access": "unknown"}
```

## Output (abridged)

```json
{"data": {"search_plan": {}, "assumptions": ["Core tier assumed"]}, "provenance": {"confidence": 0.6, "gaps": ["tier", "capacity"]}}
```

Notes: demonstrates Search plan + lists → prospect-research, lead-qualification consumed downstream, degraded confidence on gaps, no fabricated facts.

# LinkedIn Sales Navigator — Basic example

## Input

```json
{"icp": {"titles": ["VP Sales"], "geos": ["US"]}, "capacity": "100/week"}
```

## Output (abridged)

```json
{"data": {"search_plan": {"title_boolean": "(VP OR Vice President) AND Sales NOT...", "lists": ["newbiz-us"]}}, "provenance": {"producer_skill": "linkedin.sales-navigator", "confidence": 0.78, "gaps": ["tier unconfirmed"]}}
```

Notes: fictitious data. Confidence reflects evidence present; gaps list what was missing.

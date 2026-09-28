# LinkedIn Account-Based Marketing — Basic example

## Input

```json
{"accounts": ["Acme ($100k)", "Beta ($20k)"], "icp": {}}
```

## Output (abridged)

```json
{"data": {"tiers": {"strategic": ["Acme"], "programmatic": ["Beta"]}}}, "provenance": {"producer_skill": "linkedin.abm", "confidence": 0.78, "gaps": []}}
```

Notes: fictitious data. Confidence reflects evidence present; gaps list what was missing.

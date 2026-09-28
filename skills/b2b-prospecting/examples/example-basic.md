# LinkedIn B2B Prospecting — Basic example

## Input

```json
{"icp": {"titles": ["VP Sales"]}, "accounts": ["Acme", "Beta"], "capacity": "50/week"}
```

## Output (abridged)

```json
{"data": {"tiers": {"A": ["Acme (hiring trigger)"]}, "queue": ["Acme/VP Sales"]}, "provenance": {"producer_skill": "linkedin.b2b-prospecting", "confidence": 0.76, "gaps": []}}
```

Notes: fictitious data. Confidence reflects evidence present; gaps list what was missing.

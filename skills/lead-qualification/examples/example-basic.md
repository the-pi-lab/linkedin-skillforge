# LinkedIn Lead Qualification — Basic example

## Input

```json
{"leads": ["VP Sales SaaS hiring"], "icp": {"titles": ["VP Sales"]}}
```

## Output (abridged)

```json
{"data": {"prospects": [{"fit": 0.9, "intent": 0.7, "band": "now"}]}, "provenance": {"producer_skill": "linkedin.lead-qualification", "confidence": 0.8, "gaps": []}}
```

Notes: fictitious data. Confidence reflects evidence present; gaps list what was missing.

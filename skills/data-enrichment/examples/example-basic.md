# LinkedIn Data Enrichment — Basic example

## Input

```json
{"records": [{"name": "A. Example"}], "fields_wanted": ["title", "company"]}
```

## Output (abridged)

```json
{"data": {"enriched": [{"title": "VP Sales (0.85)"}]}, "provenance": {"producer_skill": "linkedin.data-enrichment", "confidence": 0.8, "gaps": ["email"]}}
```

Notes: fictitious data. Confidence reflects evidence present; gaps list what was missing.

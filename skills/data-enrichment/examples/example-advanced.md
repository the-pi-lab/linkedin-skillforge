# LinkedIn Data Enrichment — Advanced / composition example

## Scenario

Conflicting titles across sources: held with both candidates flagged.

## Input

```json
{"records": [{"name": "B. Example"}], "fields_wanted": ["title"]}
```

## Output (abridged)

```json
{"data": {"unfilled": [{"field": "title", "candidates": ["VP", "Head"], "reason": "conflict"}]}, "provenance": {"confidence": 0.5, "gaps": ["corroboration"]}}
```

Notes: demonstrates Enriched Person/Lead → lead-qualification, crm-integration consumed downstream, degraded confidence on gaps, no fabricated facts.

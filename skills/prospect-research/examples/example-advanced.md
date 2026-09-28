# LinkedIn Prospect Research — Advanced / composition example

## Scenario

Same-name collision: two profiles match; skill stops with candidate list instead of guessing.

## Input

```json
{"subject": "John Smith, Acme", "depth": "standard"}
```

## Output (abridged)

```json
{"data": {"candidates": [".../john-smith-1", ".../john-smith-2"], "dossier": null}, "provenance": {"confidence": 0.3, "gaps": ["identity disambiguation"]}}
```

Notes: demonstrates ResearchResult → lead-qualification, ai-personalization, b2b-prospecting consumed downstream, degraded confidence on gaps, no fabricated facts.

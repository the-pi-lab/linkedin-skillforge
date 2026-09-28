# LinkedIn SEO — Advanced / composition example

## Scenario

Private profile blocking Google indexing; plan includes settings fix as P0 plus section edits.

## Input

```json
{"audience": "recruiters: data engineer", "profile": "...private..."}
```

## Output (abridged)

```json
{"data": {"blocker": "public visibility off", "keyword_map": {}}, "provenance": {"confidence": 0.6, "gaps": ["peer benchmarks"]}}
```

Notes: demonstrates Keyword map → profile-optimization (applies edits) consumed downstream, degraded confidence on gaps, no fabricated facts.

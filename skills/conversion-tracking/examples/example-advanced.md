# LinkedIn Conversion Tracking — Advanced / composition example

## Scenario

No tracking at all: minimal 5-event starter + QA backlog with owners.

## Input

```json
{"motions": ["ads"], "systems": ["new site"]}
```

## Output (abridged)

```json
{"data": {"wiring": "starter + backlog"}}, "provenance": {"confidence": 0.6, "gaps": ["pixel access"]}}
```

Notes: demonstrates Taxonomy + clean events → analytics-reporting consumed downstream, degraded confidence on gaps, no fabricated facts.

# LinkedIn Analytics and Reporting — Advanced / composition example

## Scenario

Sparse data: ranges + instrumentation backlog instead of false precision.

## Input

```json
{"metrics": {"posts": 2}}
```

## Output (abridged)

```json
{"data": {"insights": ["insufficient n"], "backlog": ["UTM discipline", "weekly pull"]}, "provenance": {"confidence": 0.5, "gaps": ["sample size"]}}
```

Notes: demonstrates AnalyticsReport → growth-strategy, campaign-optimization, content-scheduling consumed downstream, degraded confidence on gaps, no fabricated facts.

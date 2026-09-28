# LinkedIn Copywriting — Advanced / composition example

## Scenario

Technical draft with unverified benchmark; copy softens claim, flags verification, keeps punch.

## Input

```json
{"draft": "Our tool is 10x faster...", "voice": "plain-technical"}
```

## Output (abridged)

```json
{"data": {"copy": {"body": "In our staging runs, p95 fell from... [verify prod]"}}, "provenance": {"confidence": 0.66, "gaps": ["benchmark source"]}}
```

Notes: demonstrates ContentPost → content-scheduling, engagement-strategy consumed downstream, degraded confidence on gaps, no fabricated facts.

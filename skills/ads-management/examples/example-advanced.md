# LinkedIn Ads Management — Advanced / composition example

## Scenario

Policy-risky earnings claim: rewritten to compliant proof-led creative + review flag.

## Input

```json
{"offer": "10x revenue claims"}
```

## Output (abridged)

```json
{"data": {"campaign": "draft-held", "flag": "claim review"}}, "provenance": {"confidence": 0.55, "gaps": ["compliant proof"]}}
```

Notes: demonstrates Campaign → campaign-optimization, conversion-tracking consumed downstream, degraded confidence on gaps, no fabricated facts.

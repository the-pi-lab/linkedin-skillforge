# LinkedIn Automation Compliance — Advanced / composition example

## Scenario

CAPTCHA-bypass scraper: blocked with citations + compliant official-API alternative.

## Input

```json
{"workflow": "scraper with CAPTCHA bypass, 5k/day"}
```

## Output (abridged)

```json
{"data": {"verdict": "blocked", "findings": ["auth-integrity critical", "rate-abuse critical"]}}, "provenance": {"confidence": 0.9, "gaps": []}}
```

Notes: demonstrates Verdict + fixes → all automation skills (gate) consumed downstream, degraded confidence on gaps, no fabricated facts.

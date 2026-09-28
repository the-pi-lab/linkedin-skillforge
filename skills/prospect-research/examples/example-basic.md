# LinkedIn Prospect Research — Basic example

## Input

```json
{"subject": "linkedin.com/in/example-vp-sales", "depth": "standard", "questions": ["role scope", "triggers"]}
```

## Output (abridged)

```json
{"data": {"findings": [{"claim": "VP Sales, 200-person SaaS", "confidence": 0.85}], "triggers": ["hiring 3 SDRs (2w ago)"]}, "provenance": {"producer_skill": "linkedin.prospect-research", "confidence": 0.8, "gaps": ["tech stack"]}}
```

Notes: fictitious data. Confidence reflects evidence present; gaps list what was missing.

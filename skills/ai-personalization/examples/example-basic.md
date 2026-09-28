# LinkedIn AI-Powered Personalization — Basic example

## Input

```json
{"template": "Saw {{trigger}} at {{company}}...", "dossiers": ["hiring 3 SDRs"]}
```

## Output (abridged)

```json
{"data": {"personalized": [{"body": "Saw the 3 SDR reqs at Acme...", "cites": ["finding-2"]}]}, "provenance": {"producer_skill": "linkedin.ai-personalization", "confidence": 0.82, "gaps": []}}
```

Notes: fictitious data. Confidence reflects evidence present; gaps list what was missing.

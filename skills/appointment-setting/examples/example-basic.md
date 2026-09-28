# LinkedIn Appointment Setting — Basic example

## Input

```json
{"conversation": "VP agreed to chat", "calendar": "Tue/Thu afternoons ET"}
```

## Output (abridged)

```json
{"data": {"booking": {"slots": ["Tue 2pm", "Thu 11am"], "agenda": "SDR follow-up teardown"}}}, "provenance": {"producer_skill": "linkedin.appointment-setting", "confidence": 0.82, "gaps": []}}
```

Notes: fictitious data. Confidence reflects evidence present; gaps list what was missing.

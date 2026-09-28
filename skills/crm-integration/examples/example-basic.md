# LinkedIn CRM Integration — Basic example

## Input

```json
{"entities": ["Lead", "Conversation"], "crm": "HubSpot"}
```

## Output (abridged)

```json
{"data": {"mapping": {"Lead": "Contact", "key": "linkedin_handle"}}, "provenance": {"producer_skill": "linkedin.crm-integration", "confidence": 0.8, "gaps": []}}
```

Notes: fictitious data. Confidence reflects evidence present; gaps list what was missing.

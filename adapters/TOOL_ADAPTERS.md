# Tool Adapter Architecture (v1.0.0)

Skills depend on **interfaces**, never providers.

```text
skill (SKILL.md + schema.json)
  → tool interface (this doc, stable name + signature)
    → provider adapter (your code, e.g. adapters/linkedin-api.py)
      → actual provider (LinkedIn API, CRM, browser, DB)
```

## Standard interfaces

| Interface | Signature (illustrative) | Used by |
|---|---|---|
| `search(query, filters)` | `(str, dict) → ResearchResult[]` | prospect-research, market-research, competitor-analysis |
| `get_profile(handle_or_urn)` | `(str) → LinkedInProfile` | profile-optimization, prospect-research, social-selling |
| `get_company(slug_or_urn)` | `(str) → Company` | abm, competitor-analysis, employer-branding |
| `enrich_contact(identifier)` | `(str) → Person + confidence` | data-enrichment, lead-qualification |
| `send_message(recipient, message)` | gated, human-approved | cold-messaging, appointment-setting |
| `create_crm_record(record)` | `(CRMRecord) → receipt` | crm-integration, sales-funnel |
| `schedule_post(post, slot)` | `(ContentPost, datetime) → receipt` | content-scheduling |
| `post_content(post)` | gated | content-creation, ai-content-generation |
| `get_analytics(scope, window)` | `(dict, str) → metrics` | analytics-reporting, conversion-tracking |
| `manage_ads(op)` | gated | ads-management, campaign-optimization |
| `track_conversion(event)` | `(dict) → receipt` | conversion-tracking |
| `create_appointment(slot, attendees)` | gated | appointment-setting |

Full typed signatures: see `adapters/interfaces.json`.

## Adapter contract

1. Expose `capabilities() → string[]` so skills can check availability FIRST.
2. Return typed receipts (`{ok, provider, id, at}`), never bare booleans.
3. Enforce rate limits + daily caps; surface `429 / quota` as typed errors.
4. Redact PII in logs. Append `source_ref = "tool:<interface>:<id>"` for provenance.
5. Writes (`send_message`, `post_content`, `manage_ads`, CRM writes) REQUIRE host
   confirmation unless host policy explicitly opts into autonomous mode with audit log.

## Availability / degradation

```python
if "get_profile" not in adapter.capabilities():
    return analysis_only_output(gaps=["live profile fetch unavailable"])
```

Skills MUST include this branch. Tests in every `tests/eval.json` cover it.

## Writing your own adapter

See `adapters/example-adapter.py` (stdlib only, in-memory stub implementing
`capabilities()`, `get_profile()`, `search()`, `create_crm_record()`).
Copy it, replace stubs with real SDK calls, keep interface names unchanged.

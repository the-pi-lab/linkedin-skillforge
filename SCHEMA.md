# Shared Data Models (v1.0.0)

All skills share these entities. **Do not redefine them per skill** — import by name.
Canonical JSON Schemas live in `schemas/*.json`. This doc is the human-readable summary.

## Entity map

| Entity | File | Purpose | Produced by | Consumed by |
|---|---|---|---|---|
| Person | `schemas/person.json` | Base human identity | prospect-research, data-enrichment | lead-qualification, personalization |
| LinkedInProfile | `schemas/linkedin-profile.json` | Profile snapshot + audit | profile-optimization, prospect-research | personal-branding, linkedin-seo, social-selling |
| Company | `schemas/company.json` | Employer / target account | prospect-research, competitor-analysis | abm, market-research, employer-branding |
| JobRole | `schemas/job-role.json` | Role context for messaging / hiring | prospect-research, recruitment-automation | job-search-optimization, b2b-prospecting |
| Lead | `schemas/lead.json` | Unqualified contact + source | lead-generation, sales-navigator | lead-qualification, crm-integration |
| Prospect | `schemas/prospect.json` | Qualified contact + fit + intent | lead-qualification, b2b-prospecting | ai-personalization, cold-messaging, appointment-setting |
| ICP | `schemas/icp.json` | Ideal Customer Profile definition | lead-generation, abm | prospect-research, sales-navigator, market-research |
| Campaign | `schemas/campaign.json` | Outreach / ads / content campaign | outreach-automation, ads-management | campaign-optimization, conversion-tracking, analytics-reporting |
| Message | `schemas/message.json` | Single message variant + personalization slots | cold-messaging, ai-personalization | outreach-automation, email-outreach-integration, appointment-setting |
| ContentPost | `schemas/content-post.json` | Ready-to-publish post | content-creation, ai-content-generation, copywriting | content-scheduling, engagement-strategy, algorithm-optimization |
| ContentIdea | `schemas/content-idea.json` | Pre-draft angle + hook | content-creation, market-research | ai-content-generation, copywriting |
| Engagement | `schemas/engagement.json` | Like / comment / reply action plan | engagement-strategy, networking | social-selling, algorithm-optimization |
| Conversation | `schemas/conversation.json` | Thread state + next action | cold-messaging, networking | appointment-setting, crm-integration |
| Opportunity | `schemas/opportunity.json` | Pipeline stage + value | social-selling, sales-funnel | crm-integration, analytics-reporting |
| Appointment | `schemas/appointment.json` | Booked meeting + context | appointment-setting | crm-integration, email-outreach-integration |
| CRMRecord | `schemas/crm-record.json` | CRM write payload + dedupe keys | crm-integration | analytics-reporting, workflow-automation |
| ResearchResult | `schemas/research-result.json` | Evidence-scored findings | prospect-research, market-research, competitor-analysis | lead-qualification, abm, content-creation |
| AnalyticsReport | `schemas/analytics-report.json` | Metrics + insights + recommendations | analytics-reporting, conversion-tracking | growth-strategy, campaign-optimization, content-scheduling |
| AutomationWorkflow | `schemas/automation-workflow.json` | Trigger → steps → guards | workflow-automation, ai-agent-development | automation-compliance, api-integration |
| Provenance | embedded in all outputs | producer, confidence, gaps, refs | every skill | every downstream skill |

## Envelope (required on every skill output)

```json
{
  "data": { "<entity>": {} },
  "provenance": {
    "producer_skill": "linkedin.<slug>",
    "producer_version": "1.0.0",
    "produced_at": "2026-01-01T00:00:00Z",
    "source_refs": ["user-provided", "tool:get_profile:urn:..."],
    "confidence": 0.82,
    "gaps": ["current headline not provided"],
    "assumptions": ["company size inferred from headline"]
  }
}
```

- `confidence`: 0.0–1.0, calibrated. <0.5 MUST block automated sends.
- `gaps`: missing critical facts preventing higher confidence.
- `source_refs`: `user-provided` | `tool:<interface>:<id>` | `inferred:<basis>`.
- Never emit a fact without a source_ref.

## Design rules

1. Additive evolution only — new optional fields MINOR, required fields MAJOR.
2. All IDs are strings; timestamps RFC3339 UTC; URLs validated.
3. PII fields flagged `"pii": true` in schemas; adapters MUST redact on logging.
4. Confidence propagation: downstream confidence ≤ min(upstream confidences) unless new evidence added (then document it).

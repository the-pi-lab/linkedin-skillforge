# Composition Chain A — Prospecting → Meeting

`lead-generation` (ICP + Lead[]) → `prospect-research` (ResearchResult) →
`lead-qualification` (Prospect + fit_score) → `ai-personalization` (Message variants) →
`cold-messaging` (send-ready Message) → `appointment-setting` (Appointment) →
`crm-integration` (CRMRecord receipt).

Pass `{data, provenance}` forward; downstream confidence <= min(upstream).
Gate automated sends on confidence >= 0.7 + human approval + opt-out check.

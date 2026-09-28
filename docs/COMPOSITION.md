# Composition Guide

## Envelope

Every output: `{data, provenance:{producer_skill, producer_version, produced_at, source_refs[], confidence, gaps[], assumptions[]}}`.

## Rules

1. Pass envelopes, not bare entities.
2. Downstream confidence <= min(upstream) unless new evidence cited.
3. Propagate `gaps[]`; never silently fill missing facts.
4. On upstream failure: abort, degrade, or substitute — per skill's Failure Recovery.
5. Declare `consumes` / `produces` per skill Chaining section.

## Example chains

- `examples/composition/chain-prospecting.md`: lead-generation → prospect-research → lead-qualification → ai-personalization → cold-messaging → appointment-setting → crm-integration.
- `examples/composition/chain-content.md`: profile-optimization → content-creation → ai-content-generation → content-scheduling → engagement-strategy → analytics-reporting.
- `examples/composition/chain-paid.md`: market-research → abm → ads-management → campaign-optimization → conversion-tracking → analytics-reporting → growth-strategy.

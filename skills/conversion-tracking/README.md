# LinkedIn Conversion Tracking (`linkedin.conversion-tracking`)

Prove what worked: define conversion events (content→profile→DM→meeting→pipeline), wire tracking (UTM, CRM stages, ad conversions), set attribution rules with honest limits, and QA data quality — so analytics-reporting reasons from trustworthy inputs.

## Install

Copy `skills/conversion-tracking/` into your agent skills folder. No dependencies.

## Quickstart

1. Read `SKILL.md` (reasoning) + `schema.json` (validation).
2. Supply inputs: `motions`, `systems`, `goals`.
3. Wire tools if available (track_conversion, get_analytics); otherwise analysis-only mode.
4. Validate output envelope (`data` + `provenance` with confidence/gaps).

## Compose

Consumes Motions + systems; produces Taxonomy + clean events → analytics-reporting. See `SKILL.md → Chaining`.

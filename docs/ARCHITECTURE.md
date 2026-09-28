# Architecture

Skill library, not monolith. Each skill: `SKILL.md` (reasoning) + `schema.json`
(validation) + examples + evals. Shared entities in `schemas/`. Tool access via
abstract interfaces in `adapters/`. Composition via typed envelopes with provenance.

See `SKILL_SPEC.md` (normative), `SCHEMA.md`, `adapters/TOOL_ADAPTERS.md`,
`docs/COMPOSITION.md`, `docs/TESTING.md`, `docs/COMPLIANCE.md`.

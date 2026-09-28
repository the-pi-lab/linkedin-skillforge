# Changelog

All notable changes to the library (spec, schemas, adapters, cross-skill contracts).

Per-skill changes live in each `SKILL.md` → `Versioning` → `changelog[]`.

## [1.1.0] - 2026-09-28

- Added `ide/` universal adapter layer: `install.py` (any skill → any IDE,
  dry-run by default) + `IDE_REGISTRY.md` with honest confidence labels.
- Added `evolution/` self-improvement layer: `EVOLUTION.md` loop design,
  `evolve.py` gated CLI (record/propose/validate/apply), run-record + proposal
  schemas, audit log, scorecard. Human approval mandatory for all releases.
- `SKILL_SPEC.md` Annex A documents both layers as additive; all 40 skills
  remain v1.0.0-conformant (no contract changes).

## [1.0.0] - 2026-09-28

- Initial release: 40 skills conforming to `SKILL_SPEC.md v1.0.0`.
- 19 shared entities in `schemas/`.
- Tool adapter architecture (`adapters/TOOL_ADAPTERS.md`).
- Contract test harness (`tests/test_skill_contract.py`).
- 3 composition examples (`examples/composition/`).

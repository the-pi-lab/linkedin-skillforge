# Contributing

## Scope

Contributions are skills, schemas, adapters, IDE mappings, evolution proposals, tests, docs. No provider-locked code.

## Adding an IDE mapping

1. Add one row to `ide/IDE_REGISTRY.md` + one entry in `ide/install.py` `REGISTRY`.
2. Confidence MUST be `fallback` unless you personally tested the install.
3. Run `python tests/test_new_layers.py` — registry and installer checks must pass.

## Adding / changing a skill

1. Copy an existing `skills/<slug>/` as template. Keep the 27-section order from `SKILL_SPEC.md`.
2. Bump `version` per semver: breaking I/O → MAJOR, new optional field → MINOR, fix → PATCH. Update `changelog[]` in SKILL.md + root `CHANGELOG.md` if cross-cutting.
3. Update `schema.json` (draft 2020-12). Inputs/outputs in SKILL.md MUST match it byte-for-byte semantically.
4. Add `examples/example-basic.md` + `example-advanced.md`, `tests/eval.json` (≥6 cases: normal + adversarial).
5. Run `python -m unittest discover -s tests -p 'test_*.py' -v` — all checks must pass.

## Schema changes

- Additive only. New required field = MAJOR + migration note in `CHANGELOG.md`.
- Never duplicate an entity — extend `schemas/*.json` and reference by name.

## Style

- Precise, executable, no marketing fluff. Measurable quality bars.
- Tool interfaces abstract only (`search()`, `get_profile()`, …). No SDK imports inside `SKILL.md`.
- No forbidden automation content (see `SECURITY.md` + `skills/automation-compliance/`).

## PR checklist

- [ ] Spec §12 conformance passes
- [ ] No PII / secrets in examples or tests (use fictitious data)
- [ ] Provenance + confidence + gaps in all output examples

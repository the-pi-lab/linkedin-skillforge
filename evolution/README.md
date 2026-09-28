# Self-Evolution Layer

Skills that get better with use — **without going rogue**.

Your Hinglish summary, formalized: *"ye approach se ye aaya, toh ab iss wale
approach ko aur better banate hain"* (this approach produced this result, so now
we improve that approach) — as a gated loop where every improvement is measured,
validated, human-approved, versioned, and reversible.

## The loop

```text
1. OBSERVE   every skill run appends a run record (inputs hash, output confidence,
             human rating, downstream reuse)        → evolution/runs.jsonl
2. SCORE     aggregate per skill: eval pass-rate, mean confidence calibration,
             human approval rate, reuse rate        → evolution/SCORECARD.md
3. PROPOSE   agent drafts a bounded improvement citing run-record IDs
                                                    → evolution/proposals/<id>.json
4. VALIDATE  evolve.py checks gates (contract, evals, compliance, semver)
             dry-run first, always
5. APPROVE   human signs with --approve "name"; only then may files change
6. RELEASE   version bump + changelog + audit entry; old version tagged for rollback
7. MONITOR   next N runs watched; regression → auto-flag → rollback proposal
```

**Nothing reaches step 6 without a human.** The tool enforces this; see `EVOLUTION.md`.

## What may evolve (allowlist)

- Decision thresholds and weights (with re-calibration evidence)
- Workflow step wording / ordering (no step may drop a guard)
- Validation checklist items (only additive)
- Examples and anti-examples (fictitious data only)
- `tests/eval.json` cases (only additive, never deleting a failing case to pass)

## What may NEVER auto-evolve (blocklist)

- Input/output schema breaking changes without MAJOR bump + review
- Removing or weakening: human gates, opt-out handling, caps, audit logging
- Widening tool permissions
- Anything the `automation-compliance` skill would score as higher risk
- Deleting eval cases that currently fail (fix the skill, not the test)

## Quickstart

```bash
# After a real skill run, record the outcome (agent does this, honestly)
python evolution/evolve.py record --skill cold-messaging --outcome succeeded \
  --confidence 0.82 --human-rating 4 --notes "trigger-led variant won"

# Draft an improvement grounded in run records
python evolution/evolve.py propose --skill cold-messaging \
  --from-runs run-001,run-002 --change-type threshold \
  --summary "Raise auto-send gate 0.7 -> 0.75 after 2 low-confidence sends" \
  --version-bump minor

# Validate gates (dry-run, changes nothing)
python evolution/evolve.py validate --proposal evolution/proposals/prop-001.json

# Human approves and releases (only command that writes to skills/)
python evolution/evolve.py apply --proposal evolution/proposals/prop-001.json \
  --approve "Maintainer Name" --apply
```

Full design, metrics, and anti-gaming rules: `EVOLUTION.md`.
Schemas: `schemas/run-record.json`, `schemas/proposal.json`.
Audit trail: `AUDIT_LOG.md` (append-only).

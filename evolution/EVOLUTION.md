# EVOLUTION.md — Self-Improvement Design (v1.0.0)

## 1. Philosophy

A skill is a hypothesis about good reasoning. Each real run is evidence.
Evolution turns evidence into better hypotheses — slowly, measurably, reversibly.
**Learning without gates is drift. This layer is all gates.**

## 2. Data model

- **Run record** (`schemas/run-record.json`): one skill execution. Fields: `run_id`,
  `skill_id`, `skill_version`, `input_hash` (never raw PII), `outcome`
  (`succeeded|partial|failed|refused`), `output_confidence`, `human_rating`
  (1–5, optional but weighted highest), `downstream_reused` (bool),
  `eval_passed` (bool, from harness where runnable), `notes`.
- **Proposal** (`schemas/proposal.json`): one bounded change. Fields: `proposal_id`,
  `skill_id`, `base_version`, `change_type` (allowlist §4), `summary`,
  `cites_runs[]` (≥1 run-record ID — proposals without evidence are rejected),
  `files_touched[]`, `version_bump` (`patch|minor|major`), `changelog_entry`,
  `approval` (empty until human signs), `rollback_plan`.
- **Audit log** (`AUDIT_LOG.md`): every record/propose/validate/apply/rollback event,
  timestamped, append-only.

## 3. Metrics (scoreboard per skill, `SCORECARD.md`)

| Metric | Source | Healthy |
|---|---|---|
| Eval pass-rate | `tests/eval.json` via harness | 100% (blocking) |
| Confidence calibration | \|mean confidence − success rate\| | ≤ 0.15 gap |
| Human approval rate | run records rating ≥ 4 | ≥ 80% |
| Reuse rate | downstream_reused | tracked, no threshold |
| Regression count | post-release failures | 0 → else rollback |

A skill becomes an evolution **candidate** when: human approval < 80% over ≥10
rated runs, calibration gap > 0.15, or 2+ post-release regressions. Candidates
are prioritized, never auto-patched.

## 4. Change allowlist (enforced by `evolve.py validate`)

`threshold`, `wording`, `checklist-add`, `example`, `eval-add`, `order-steps`.
Anything else → `validate` fails with `change-type not evolvable`.

## 5. Blocklist (enforced, fail-closed)

`validate` REJECTS proposals whose summary/files suggest:

- removing/weakening human gates, approvals, opt-out, caps, audit logging
- deleting or editing an eval case to hide a failure (eval-add only)
- breaking `schema.json` Input/Output compatibility without `major` bump
- widening `tools_required` / `permissions_required`
- keywords: `bypass`, `remove approval`, `remove opt-out`, `uncapped`,
  `delete eval`, `weaken`, `skip validation`

Uncertain cases fail closed → human legal/maintainer review.

## 6. The agent's evolution routine (every K runs, e.g. K=10)

1. Read run records + scorecard for the skill.
2. Name the single biggest failure pattern **with run IDs as evidence**.
3. Draft the smallest allowlisted change that addresses it.
4. Run `validate` (dry-run). If it fails, shrink the proposal, don't fight the gate.
5. Present proposal + evidence + expected effect to the human. **Stop here.**
6. Only after `--approve`: `apply --apply`, then monitor next K runs.
7. Regression → file a rollback proposal (same loop, `change_type: wording`,
   summary starts with `ROLLBACK:`).

The reference implementation also exposes `evolve.py score --skill <slug>`.
It reads privacy-safe JSONL records, reports success/eval/human-approval/reuse
rates, and marks a skill as a candidate only when the minimum evidence window is
met. Malformed records fail closed rather than being included in a score.

## 7. Anti-gaming rules

- Self-scores don't count: a proposal citing only agent-written notes with no
  human rating and no eval result is rejected (`insufficient evidence`).
- Metric targets are floors, not games: raising thresholds to inflate
  approval-rate without the cited failure pattern is rejected.
- Version bumps follow semver (§SPEC §11); evolution never sneaks a MAJOR
  through `validate` without `rollback_plan` + human approval string ≥ 3 chars.
- `automation-compliance` re-scores any proposal touching outreach/automation
  skills; higher risk → blocked.

## 8. Rollback

Every `apply` records `base_version` + touched files. Rollback = new proposal
restoring prior content with `ROLLBACK:` prefix, same gates, same approval.
History is never rewritten; the audit log shows the full lineage.

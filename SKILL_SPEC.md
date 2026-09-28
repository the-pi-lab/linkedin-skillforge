# LinkedIn Skills SDK — Universal Skill Specification (v1.0.0)

> This document is the **normative contract** for all 40 skills in this repository.
> Every skill MUST conform to it. If a skill conflicts with this spec, the spec wins.

## 1. Design Intent

This repo is a **skill library**, not a monolithic agent.

- `SKILL` = reasoning + methodology + workflow + rules.
- `TOOL` = mechanism that performs an action (API, scraper, CRM, browser).
- Skills describe WHAT to do and HOW to reason. Tools do the doing.
- Skills are **tool-agnostic, framework-agnostic, vendor-neutral, IDE-agnostic**.

A user MUST be able to copy a single `skills/<slug>/` directory into any
compatible agent (Claude Code, Cursor, Windsurf, Copilot, Cline, Roo, generic
MCP host, custom Python/TS agent) and get value without the rest of the repo.

## 2. Required Skill Directory Layout

```text
skills/<slug>/
├── SKILL.md      # REQUIRED — primary AI-readable spec (follows §4)
├── schema.json   # REQUIRED — JSON Schema for inputs/outputs (draft 2020-12)
├── README.md     # REQUIRED — human-facing usage (install, quickstart)
├── examples/
│   ├── example-basic.md    # REQUIRED — happy-path input → output
│   └── example-advanced.md # REQUIRED — composition / edge case
└── tests/
    └── eval.json           # REQUIRED — ≥6 cases: normal + adversarial
```

No other files are required. Do not add lockfiles, node_modules, or binaries
inside a skill directory.

## 3. Universal Frontmatter Contract

Every `SKILL.md` MUST start with YAML frontmatter containing exactly:

```yaml
---
skill_id: linkedin.<slug-with-dashes>        # e.g. linkedin.prospect-research
skill_name: Human Readable Name
version: 1.0.0                                # semver
description: One-sentence capability summary (<140 chars)
category: foundation | content | prospecting | outreach | automation | data | engagement | analytics | talent | paid | platform | strategy
tags: [linkedin, <slug>, ...]
author: linkedin-skills-community
license: MIT
spec_version: 1.0.0
maturity: stable | experimental
requires_tools: false | true                  # true only if skill is useless without a tool
requires_network: false | true
---
```

Plus a `contract` code block in the Identity section exposing the 24-field
machine-readable contract (see §5).

## 4. Required SKILL.md Sections (in order)

1. Identity
2. Purpose
3. When To Use
4. When NOT To Use
5. Capabilities
6. Inputs
7. Input Schema (reference to schema.json)
8. Outputs
9. Output Schema (reference to schema.json)
10. Preconditions
11. Required Context
12. Optional Context
13. Reasoning Process (INPUT → ANALYSIS → DECISION → EXECUTION → VALIDATION → OUTPUT)
14. Execution Workflow (numbered, deterministic steps)
15. Decision Rules (if/then, thresholds, conflict resolution)
16. Validation (pre-output checklist)
17. Error Handling (named failure modes)
18. Failure Recovery
19. Tool Interfaces (abstract interface names only, §6)
20. Security
21. Compliance
22. Quality Standards (measurable)
23. Examples (pointer to examples/)
24. Anti-Examples (≥2)
25. Evaluation Criteria
26. Chaining (consumes / produces)
27. Versioning

Omit none. Keep each section precise and executable. No marketing fluff.

## 5. 24-Field Machine Contract

Every skill MUST declare (in Identity as a `json` block):

`skill_id, skill_name, version, description, purpose, category, capabilities[],
triggers[], inputs{}, input_schema, outputs{}, output_schema, prerequisites[],
dependencies[], optional_dependencies[], tools_required[], permissions_required[],
workflow[], reasoning_guidelines[], execution_rules[], validation_rules[],
failure_modes[], recovery_strategy, safety_rules[], compliance_rules[],
examples[], anti_examples[], quality_criteria[], evaluation_tests[], changelog[]`

`schema.json` MUST implement `input_schema` / `output_schema` as JSON Schema.
`tests/eval.json` MUST implement `evaluation_tests`.

## 6. Tool Adapter Architecture (normative)

Skills NEVER call providers directly. They declare an abstract interface:

```text
skill → tool interface → provider adapter → actual provider
```

Standard interface names (see `adapters/TOOL_ADAPTERS.md`):

`search(), get_profile(), get_company(), enrich_contact(), send_message(),
create_crm_record(), schedule_post(), get_analytics(), post_content(),
manage_ads(), track_conversion(), create_appointment()`

Rules:

1. Verify tool availability BEFORE attempting execution.
2. If tool unavailable → degrade to analysis-only mode, NEVER hallucinate the action.
3. NEVER claim a tool action happened when it did not.
4. NEVER invent LinkedIn API capabilities. If unsure, say so.
5. Prefer official APIs, approved integrations, user-authorized workflows,
   human approval gates, rate limiting, audit logs, opt-out handling.

## 7. Composition System (normative)

- Skills communicate via **structured outputs** defined in `schemas/`.
- Each skill lists `consumes` and `produces` entity types in Chaining.
- Shared entities: Person, LinkedInProfile, Company, JobRole, Lead, Prospect,
  ICP, Campaign, Message, ContentPost, ContentIdea, Engagement, Conversation,
  Opportunity, Appointment, CRMRecord, ResearchResult, AnalyticsReport,
  AutomationWorkflow (see `SCHEMA.md` + `schemas/*.json`).
- Error propagation: downstream skill MUST receive `provenance`, `confidence`
  (0.0–1.0), and `gaps[]`. Never silently drop uncertainty.
- Provenance object (required on all outputs): `{producer_skill, producer_version, produced_at, source_refs[], confidence, gaps[]}`.

Canonical chain (illustrative, NOT mandatory):

```text
profile-optimization → personal-branding → content-creation → engagement-strategy
→ lead-generation → prospect-research → lead-qualification → ai-personalization
→ outreach (cold-messaging) → appointment-setting → crm-integration → analytics-reporting
```

Any subset / order is valid if input contracts are satisfied.

## 8. AI Behaviour Rules (normative, all skills)

1. Never fabricate information. Distinguish facts vs assumptions vs inferences.
2. Explicitly identify uncertainty with confidence scores.
3. Ask for missing CRITICAL information; avoid unnecessary questions (≤3 per turn).
4. Validate outputs against schema before returning.
5. Prefer evidence over assumptions.
6. Never claim LinkedIn access you don't have.
7. Never invent API fields, endpoints, or limits.
8. Output MUST include `confidence`, `gaps[]`, `assumptions[]`.

## 9. LinkedIn Compliance (normative, all skills)

FORBIDDEN to instruct or facilitate:

- credential theft, session hijacking, auth bypass, CAPTCHA bypass,
  security-control bypass, enforcement evasion, rate-limit abuse,
  unauthorized access, deceptive impersonation, spam at scale.

Automation skills MUST require:

- official/approved path preferred, human-in-loop for sends,
- daily caps disclosed, opt-out honoured, audit log emitted,
- `automation-compliance` skill referenced for risk scoring.

See `skills/automation-compliance/SKILL.md` for the risk evaluator.

## 10. Quality Bar

Each skill MUST define measurable Quality Standards (e.g. "all outputs validate
against schema.json; confidence calibrated; ≥2 alternatives where choice exists;
no banned claims"). Tests MUST cover: correctness, completeness, hallucination
resistance, input validation, schema compliance, edge cases, failure handling,
tool-unavailability, ambiguity, compliance, composability — with normal AND
adversarial cases. No "sounds good" grading.

## 11. Versioning

- Semver per skill (`version` in frontmatter + changelog in SKILL.md).
- `spec_version` tracks which SKILL_SPEC the skill conforms to.
- Breaking input/output change → MAJOR. New optional field → MINOR. Fix → PATCH.
- Root `CHANGELOG.md` tracks cross-skill / schema changes.

## 12. Conformance Checklist (for reviewers / CI)

- [ ] Exactly the 27 sections in order
- [ ] Frontmatter complete, skill_id matches directory
- [ ] schema.json valid JSON Schema, inputs/outputs match SKILL.md
- [ ] examples/ has basic + advanced
- [ ] tests/eval.json has ≥6 cases with expected_behaviour
- [ ] Tool interfaces abstract only, availability check present
- [ ] Compliance section present, no forbidden content
- [ ] Chaining declares consumes/produces with shared entity names
- [ ] Provenance + confidence + gaps in output schema

---

# Annex A — Repo-level layers (v1.1.0, ADDITIVE, informative)

This annex adds repository capabilities WITHOUT changing the normative skill
contract above. All 40 skills remain `spec_version: 1.0.0` conformant; nothing
here adds required `SKILL.md` sections or invalidates existing skills.

## A.1 Universal IDE adaptation (`ide/`)

- Skills are host-agnostic by construction (markdown + JSON Schema).
- `ide/install.py` maps any skill into any IDE's expected folder + manifest
  (see `ide/IDE_REGISTRY.md`). Copy-based; dry-run by default.
- Registry entries carry honest confidence (`verified` / `community` /
  `fallback`). Unverified paths MUST be labelled `fallback`, never asserted.
- New IDEs are onboarded via `generic` mode + one registry row — no skill changes.

## A.2 Self-evolution loop (`evolution/`)

- Observe → Score → Propose → Validate → Human-approve → Release → Monitor.
  Full design: `evolution/EVOLUTION.md`.
- Evolvable: thresholds, wording, step order, added checklist items, examples,
  added eval cases. All else is rejected by `evolve.py validate` (fail-closed).
- `evolve.py apply` is the ONLY evolution command that writes to `skills/`,
  and it requires `--approve "<human>"`. No autonomous self-modification, ever.
- Proposals MUST cite ≥1 run-record ID; self-scores alone are rejected
  (anti-gaming). Breaking schema changes require MAJOR + review.
- Every event is appended to `evolution/AUDIT_LOG.md`; rollback is a new
  gated proposal, never history rewrite.

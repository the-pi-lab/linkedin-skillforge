<div align="center">

<br />

<sub>THE PI LAB / OPEN SOURCE INTELLIGENCE</sub>

# PI SKILLFORGE

### The skill layer between intent and execution.

<p align="center">
  Portable reasoning for LinkedIn workflows.<br />
  Composable across agents. Native to every IDE. Built to evolve.
</p>

<br />

<a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-0b0d12?style=flat-square" alt="MIT License" /></a>
<img src="https://img.shields.io/badge/skills-40-0b0d12?style=flat-square" alt="40 skills" />
<img src="https://img.shields.io/badge/IDE--ready-10%2B-0b0d12?style=flat-square" alt="10 plus IDEs" />
<img src="https://img.shields.io/badge/dependencies-zero-0b0d12?style=flat-square" alt="Zero dependencies" />

<br /><br />

**Reason better. Compose freely. Evolve responsibly.**

<br />
</div>

<div align="center">

```text
       INTENT                 INTELLIGENCE                 EXECUTION
  ┌─────────────┐        ┌─────────────────┐        ┌─────────────────┐
  │  “Find the  │───────▶│   PI SKILLFORGE │───────▶│  IDE · API · CRM │
  │  right lead”│        │  skills + rules │        │  browser · agent │
  └─────────────┘        └─────────────────┘        └─────────────────┘
                                  │
                          evidence → evolution
```

</div>

> AI agents are good at generating answers. Great agents know **how to reason**,
> **what not to claim**, and **how to get better without drifting**.

PI SkillForge is The PI Lab’s open-source library of structured LinkedIn skills:
methodology, decision rules, contracts, evaluation and compliance—in a format
that any compatible agent can read.

## The premise

Prompts are temporary. A skill is infrastructure.

PI SkillForge separates the part that should remain stable from the part that
will always change:

```text
┌────────────────────────────────────────────────────────────────────┐
│                         STABLE INTELLIGENCE                        │
│  reasoning · methodology · workflow · decision rules · quality bar  │
└────────────────────────────────────────────────────────────────────┘
                                  │ contract
┌────────────────────────────────────────────────────────────────────┐
│                          SWAPPABLE TOOLS                           │
│  LinkedIn API · CRM · browser · scheduler · model · IDE · database  │
└────────────────────────────────────────────────────────────────────┘
```

No provider lock-in. No giant monolithic agent. No black-box prompt pack.

## Why it feels different

| | What it means in practice |
| --- | --- |
| **Portable** | Markdown + JSON Schema. Install one skill in the agent you already use. |
| **Composable** | Skills exchange typed entities, provenance, confidence and gaps. |
| **Tool-agnostic** | Abstract interfaces keep APIs, CRMs and browsers replaceable. |
| **Auditable** | Every meaningful evolution is evidenced, versioned and logged. |
| **Safe by default** | Missing tools mean analysis-only mode—not fabricated actions. |
| **Built for change** | Governed self-evolution improves skills without uncontrolled drift. |

## The library

<table>
<tr><th align="left">Layer</th><th align="left">Capabilities</th></tr>
<tr><td><b>Foundation</b></td><td>Profile optimization · Personal branding · LinkedIn SEO</td></tr>
<tr><td><b>Content</b></td><td>Content creation · Copywriting · AI generation · Algorithm optimization · Scheduling</td></tr>
<tr><td><b>Prospecting</b></td><td>Lead generation · Sales Navigator · Prospect research · B2B prospecting · Lead qualification</td></tr>
<tr><td><b>Outreach</b></td><td>Outreach automation · Cold messaging · Connection strategy · Social selling · AI personalization · Appointment setting · Email outreach</td></tr>
<tr><td><b>Strategy</b></td><td>Sales funnel · Account-based marketing · Growth strategy · Engagement strategy</td></tr>
<tr><td><b>Automation</b></td><td>AI agent development · Workflow automation · Automation compliance</td></tr>
<tr><td><b>Data & CRM</b></td><td>CRM integration · Data enrichment</td></tr>
<tr><td><b>Analytics</b></td><td>Analytics & reporting · Competitor analysis · Market research · Conversion tracking</td></tr>
<tr><td><b>Talent</b></td><td>Recruitment automation · Job search optimization · Employer branding</td></tr>
<tr><td><b>Paid & Platform</b></td><td>Ads management · Campaign optimization · API integration</td></tr>
</table>

**40 skills. One contract. Infinite workflows.** Browse [`skills/`](skills/).

## One skill. Any IDE.

Preview it first. Apply it when it looks right.

```bash
python ide/install.py install \
  --skill prospect-research \
  --ide auto \
  --target /path/to/project

python ide/install.py install \
  --skill prospect-research \
  --ide auto \
  --target /path/to/project \
  --apply
```

The universal installer supports Claude Code, Cursor, Windsurf, VS Code, Cline,
Roo, Zed, JetBrains, Neovim and a generic mode for everything else.

Every skill is self-contained:

```text
skills/prospect-research/
├── SKILL.md                 methodology + rules
├── schema.json              input/output contract
├── README.md                quickstart
├── examples/                basic + advanced usage
└── tests/eval.json          normal + adversarial evaluations
```

## Compose intelligence

Skills are small enough to understand and strong enough to chain:

```text
PROFILE → CONTENT → ENGAGEMENT → PROSPECT → QUALIFY
                                                 │
                 ANALYZE ← PERSONALIZE ←────────┘
                    │
                    ▼
       MESSAGE → APPOINTMENT → CRM → ANALYTICS
```

An output never loses its context:

```json
{
  "data": {},
  "provenance": {
    "producer_skill": "linkedin.prospect-research",
    "producer_version": "1.0.0",
    "produced_at": "2026-01-01T00:00:00Z",
    "source_refs": [],
    "confidence": 0.87,
    "gaps": []
  }
}
```

The downstream skill knows what happened, who produced it, how certain it is and
what is still missing.

See the [composition examples](examples/composition/) and
[`docs/COMPOSITION.md`](docs/COMPOSITION.md).

## The evolution engine

Self-evolving should not mean self-modifying without oversight.

PI SkillForge learns through a controlled loop:

```text
   OBSERVE ──▶ SCORE ──▶ PROPOSE ──▶ VALIDATE ──▶ APPROVE ──▶ RELEASE
      ▲                                                        │
      └──────────────────── MONITOR ◀─────────────────────────┘
```

Run evidence becomes a scorecard. A scorecard becomes a bounded proposal. A
proposal must pass evidence, semver, compliance and rollback gates. A maintainer
approves the release. The audit trail remembers everything.

```bash
python evolution/evolve.py record \
  --skill cold-messaging \
  --outcome succeeded \
  --confidence 0.86 \
  --eval-passed \
  --notes "Reviewer accepted the follow-up sequence"

python evolution/evolve.py score --skill cold-messaging
```

The engine fails closed on unsafe paths, weak evidence, schema drift, permission
widening and compliance bypasses. Learning without gates is drift; gates are the
feature.

Read the [evolution design](evolution/EVOLUTION.md).

## The adapter boundary

```text
┌──────────┐     ┌──────────────────┐     ┌─────────────────────┐
│  SKILL   │────▶│ ABSTRACT TOOL    │────▶│ PROVIDER ADAPTER    │
│ reasoning│     │ INTERFACE        │     │ API / CRM / browser │
└──────────┘     └──────────────────┘     └─────────────────────┘
```

Supported interface families include:

`search()` · `get_profile()` · `get_company()` · `enrich_contact()` ·
`send_message()` · `create_crm_record()` · `schedule_post()` · `post_content()` ·
`get_analytics()` · `manage_ads()` · `track_conversion()` · `create_appointment()`

Tools are optional. When a tool is missing, the skill says so and returns an
analysis-only result. It never claims an action happened when it did not.

See [`adapters/TOOL_ADAPTERS.md`](adapters/TOOL_ADAPTERS.md).

## Quality is not a promise. It is a contract.

Every skill includes:

- 27 required reasoning and execution sections
- Draft 2020-12 JSON Schema
- Normal and adversarial evaluation cases
- Explicit validation, errors and recovery
- Provenance, confidence, gaps and assumptions
- Security and LinkedIn compliance rules
- Semver versioning and changelog history

The project explicitly rejects credential theft, session hijacking, CAPTCHA
bypass, enforcement evasion, rate-limit abuse and spam-at-scale patterns.

## Verify it

No third-party test framework is required.

```bash
python -m unittest discover -s tests -p 'test_*.py' -v
python -m compileall -q adapters evolution ide tests
```

CI runs the same checks on Python 3.10, 3.11 and 3.12.

## Repository map

```text
├── skills/                 40 portable skill packages
├── schemas/                shared entities for composition
├── adapters/               abstract tool contracts
├── ide/                    universal installer + IDE registry
├── evolution/              scoring + proposals + audit trail
├── examples/composition/   end-to-end workflow chains
├── tests/                  contract + integration checks
└── docs/                   architecture + compliance + testing
```

## Start here

1. Choose a skill from [`skills/`](skills/).
2. Read its `SKILL.md` and `schema.json`.
3. Install it into your IDE or agent.
4. Connect only the tools you trust.
5. Record evidence. Improve with gates.

New skill, adapter or IDE mapping? Start with [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Explore the system

[`SKILL_SPEC.md`](SKILL_SPEC.md) · [`SCHEMA.md`](SCHEMA.md) ·
[`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) ·
[`docs/COMPOSITION.md`](docs/COMPOSITION.md) ·
[`docs/COMPLIANCE.md`](docs/COMPLIANCE.md) · [`SECURITY.md`](SECURITY.md) ·
[`CHANGELOG.md`](CHANGELOG.md)

## License

MIT. Use it. Fork it. Improve it. Ship it.

<div align="center">

<br />

### Built for agents that need more than prompts.

**PI SKILLFORGE**

<sub>The PI Lab · Open source · Made for the next generation of AI workflows</sub>

<br /><br />

</div>

<div align="center">

# ✦ LinkedIn Skills SDK

### The open-source intelligence layer for LinkedIn workflows.

**40 portable skills · 10+ IDEs · governed self-evolution · zero vendor lock-in**

<br />

<a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-111827?style=for-the-badge" alt="MIT License" /></a>
<img src="https://img.shields.io/badge/skills-40-0f766e?style=for-the-badge" alt="40 skills" />
<img src="https://img.shields.io/badge/runtime-stdlib--only-7c3aed?style=for-the-badge" alt="Standard library only" />
<img src="https://img.shields.io/badge/status-production--ready-16a34a?style=for-the-badge" alt="Production ready" />

<br /><br />

**Built by [The PI Lab](.) · Open source · Fork it, ship it, make it yours.**

</div>

<br />

> **Your agent should know how to think about LinkedIn — not just how to call an API.**
>
> LinkedIn Skills SDK turns complex workflows into portable, composable and testable
> reasoning modules that work across agents, IDEs and tool stacks.

<div align="center">

```text
┌──────────────────────────────────────────────────────────────────────┐
│                         YOUR AI AGENT                                │
└───────────────────────────────┬──────────────────────────────────────┘
                                │ reads
┌───────────────────────────────▼──────────────────────────────────────┐
│                    LINKEDIN SKILLS SDK                               │
│     methodology · reasoning · contracts · validation · guardrails     │
└───────────────┬───────────────────────────────┬──────────────────────┘
                │ structured entities           │ abstract interfaces
┌───────────────▼──────────────┐    ┌───────────▼──────────────────────┐
│  JSON Schemas + provenance   │    │  API · CRM · browser · scheduler │
└──────────────────────────────┘    └──────────────────────────────────┘
```

</div>

## Why this exists

Most AI integrations are glued together from prompts, provider-specific rules and
hope. That breaks the moment you change model, IDE, CRM or API.

This project separates the durable part from the replaceable part:

| Durable intelligence | Replaceable machinery |
| --- | --- |
| Reasoning methodology | LinkedIn / CRM provider |
| Decision rules | Browser or API adapter |
| Input/output contracts | IDE or agent framework |
| Validation and compliance | Scheduler and deployment stack |

```text
SKILL = reasoning + methodology + workflow + rules
TOOL  = the mechanism that performs an action
```

Skills stay useful when tools change. Tools stay interchangeable when skills are
well-defined.

## What you get

<table>
<tr>
<td width="50%" valign="top">

### ◈ Portable by design

Plain Markdown, JSON Schema and Python standard library. Copy one skill into a
compatible host and start using it—no account, runtime or telemetry required.

</td>
<td width="50%" valign="top">

### ◈ Composable by contract

Skills exchange structured entities with provenance, confidence and gaps. Build
small workflows or chain the entire revenue and content engine.

</td>
</tr>
<tr>
<td width="50%" valign="top">

### ◈ Tool-agnostic

Skills declare abstract interfaces such as `search()` and `get_profile()` rather
than locking you to a provider or SDK.

</td>
<td width="50%" valign="top">

### ◈ Self-improving, safely

Real run evidence becomes scorecards and bounded evolution proposals. Changes are
validated, auditable, reversible and human-approved before release.

</td>
</tr>
</table>

## 40 skills. One system.

| Domain | Capabilities |
| --- | --- |
| **Foundation** | Profile optimization · Personal branding · LinkedIn SEO |
| **Content** | Content creation · Copywriting · AI content generation · Algorithm optimization · Content scheduling |
| **Prospecting** | Lead generation · Sales Navigator · Prospect research · B2B prospecting · Lead qualification |
| **Outreach** | Outreach automation · Cold messaging · Connection strategy · Social selling · AI personalization · Appointment setting · Email outreach integration |
| **Engagement** | Networking · Engagement strategy |
| **Strategy** | Sales funnel · Account-based marketing · Growth strategy |
| **Automation** | AI agent development · Workflow automation |
| **Data & CRM** | CRM integration · Data enrichment |
| **Analytics** | Analytics & reporting · Competitor analysis · Market research · Conversion tracking |
| **Talent** | Recruitment automation · Job search optimization · Employer branding |
| **Paid** | Ads management · Campaign optimization |
| **Platform** | API integration · Automation compliance |

Browse the complete catalog in [`skills/`](skills/).

## Install a skill in seconds

### Use one skill anywhere

```bash
# Preview first — installer is dry-run by default
python ide/install.py install \
  --skill prospect-research \
  --ide auto \
  --target /path/to/your-project

# Apply when ready
python ide/install.py install \
  --skill prospect-research \
  --ide auto \
  --target /path/to/your-project \
  --apply
```

Supported mappings include Claude Code, Cursor, Windsurf, VS Code, Cline, Roo,
Zed, JetBrains, Neovim and a generic mode for everything else.

Or simply copy a single directory:

```text
skills/prospect-research/
├── SKILL.md                 # the agent-readable methodology
├── schema.json              # input/output contract
├── README.md                # human quickstart
├── examples/                # basic + advanced examples
└── tests/eval.json          # normal + adversarial evaluations
```

## Compose a workflow

Skills are atomic alone and powerful together:

```text
Profile
  ↓
Content → Engagement → Lead generation → Prospect research
                                      ↓
                           Qualification → Personalization
                                      ↓
                 Cold messaging → Appointment → CRM → Analytics
```

Example:

```text
profile-optimization
  → content-creation
  → engagement-strategy
  → lead-generation
  → prospect-research
  → lead-qualification
  → ai-personalization
  → cold-messaging
  → appointment-setting
  → crm-integration
  → analytics-reporting
```

Every handoff preserves:

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

Downstream skills never receive silent uncertainty.

## The self-evolution loop

This is not uncontrolled prompt mutation. It is governed learning:

```text
OBSERVE → SCORE → PROPOSE → VALIDATE → HUMAN APPROVE → RELEASE → MONITOR
   ▲                                                        │
   └────────────────────── evidence ───────────────────────┘
```

Record privacy-safe evidence:

```bash
python evolution/evolve.py record \
  --skill cold-messaging \
  --outcome succeeded \
  --confidence 0.86 \
  --eval-passed \
  --notes "Follow-up timing was accepted by the reviewer"
```

Inspect quality signals:

```bash
python evolution/evolve.py score --skill cold-messaging
```

Draft, validate and release a bounded improvement:

```bash
python evolution/evolve.py propose \
  --skill cold-messaging \
  --from-runs run-example \
  --change-type wording \
  --summary "Clarify follow-up timing using reviewed run evidence" \
  --changelog "Clarified follow-up timing" \
  --rollback "Restore the previous wording verbatim"

python evolution/evolve.py validate \
  --proposal evolution/proposals/PROP.json

python evolution/evolve.py apply \
  --proposal evolution/proposals/PROP.json \
  --approve "Maintainer Name" \
  --apply
```

The system fails closed on unsafe paths, weak evidence, schema drift, permission
widening and compliance bypasses. Every release is versioned, audited and
rollbackable.

## Tool adapters without lock-in

Skills ask for abstract capabilities, never provider-specific implementation:

```text
skill → abstract interface → provider adapter → actual system
```

Available interface families include:

`search()` · `get_profile()` · `get_company()` · `enrich_contact()` ·
`send_message()` · `create_crm_record()` · `schedule_post()` · `post_content()` ·
`get_analytics()` · `manage_ads()` · `track_conversion()` · `create_appointment()`

If a tool is unavailable, the skill degrades to analysis-only mode. It never
pretends an action happened.

See [`adapters/TOOL_ADAPTERS.md`](adapters/TOOL_ADAPTERS.md) and the
[example adapter](adapters/example-adapter.py).

## Quality and compliance are built in

Every skill is held to the same contract:

- 27 required sections in `SKILL.md`
- Draft 2020-12 JSON Schema for inputs and outputs
- Normal and adversarial evaluation cases
- Provenance, confidence, gaps and assumptions
- Explicit validation, error handling and recovery
- No fabricated facts, tool actions or API capabilities
- No credential theft, session hijacking, CAPTCHA bypass or enforcement evasion
- Human approval, caps, opt-out handling and audit trails for automation

## Verify the repository

No third-party test framework is required:

```bash
python -m unittest discover -s tests -p 'test_*.py' -v
python -m compileall -q adapters evolution ide tests
```

The CI workflow runs the same checks on Python 3.10, 3.11 and 3.12.

## Repository map

```text
├── skills/                 40 portable LinkedIn skill packages
├── schemas/                shared entities for composition
├── adapters/               abstract tool contracts + reference adapter
├── ide/                    universal installer and IDE registry
├── evolution/              governed scoring, proposals and audit trail
├── examples/composition/   end-to-end workflow chains
├── tests/                  contract and integration checks
└── docs/                   architecture, compliance, testing and adapters
```

## Make it yours

1. Pick a skill from [`skills/`](skills/).
2. Read its `SKILL.md` and schema.
3. Install it into your agent or IDE.
4. Connect only the tools you trust.
5. Record evidence and evolve the workflow with gates.

New skill? New IDE? New adapter? Follow [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Links

[`SKILL_SPEC.md`](SKILL_SPEC.md) · [`SCHEMA.md`](SCHEMA.md) ·
[`ARCHITECTURE`](docs/ARCHITECTURE.md) · [`COMPOSITION`](docs/COMPOSITION.md) ·
[`COMPLIANCE`](docs/COMPLIANCE.md) · [`SECURITY.md`](SECURITY.md) ·
[`CHANGELOG.md`](CHANGELOG.md)

## License

MIT. Use it, fork it, improve it, ship it.

<div align="center">

### Built for agents that need more than prompts.

**Reason better. Compose freely. Evolve responsibly.**

</div>

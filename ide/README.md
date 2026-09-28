# Universal IDE Adapter Layer

Install **any skill** from this repo into **any IDE / agent host** with one command.
No lock-in: skills stay vendor-neutral; this layer only maps them into each host's
expected folder + manifest format.

## Quickstart

```bash
# 1. See supported hosts
python ide/install.py list

# 2. Dry-run (default: prints plan, changes nothing)
python ide/install.py install --skill prospect-research --ide cursor --target C:\my-project

# 3. Apply for real
python ide/install.py install --skill prospect-research --ide cursor --target C:\my-project --apply

# 4. No listed host? Generic mode copies the skill + prints wiring instructions
python ide/install.py install --skill prospect-research --ide generic --target C:\my-project --apply
```

`--ide auto` detects the host by scanning `--target` for marker files
(`.claude/`, `.cursor/`, `.vscode/`, `.windsurf/`, `.cline/`, `.roo/`,
`.zed/`, `.idea/`, `.nvim/` …). Detection is best-effort; confirm the plan
before `--apply`.

## How it works

```text
skills/<slug>/  (canonical, untouched — never edited by the installer)
      │  copy
      ▼
<target>/<host-skills-dir>/linkedin.<slug>/  (SKILL.md, schema.json, examples/, tests/)
      │  + generated manifest
      ▼
<target>/<host-skills-dir>/linkedin.<slug>.json  (skill_id, version, entry, host hints)
```

- The installer **copies**; it never rewrites skill content.
- Every install prints host-specific wiring notes (see `IDE_REGISTRY.md`).
- Unknown/future IDEs: use `--ide generic`. If your IDE reads a plain folder of
  markdown specs, generic mode is all you need.

## Contributing a host mapping

See `IDE_REGISTRY.md`. Each entry needs: `paths[]`, `manifest_format`,
`wiring_notes`, and an honest `confidence` (`verified` = tested by a maintainer,
`community` = reported by a user, `fallback` = reasonable default, unverified).
Never claim a path you have not tested — mark it `fallback`.

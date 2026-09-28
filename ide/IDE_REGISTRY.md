# IDE Registry (v1.0.0)

`confidence`: **verified** = tested by maintainer · **community** = user-reported,
believed correct · **fallback** = reasonable default, NOT verified — confirm in your IDE docs.

| IDE / host | Skills dir(s) under project root | Manifest / wiring | Confidence |
|---|---|---|---|
| Claude Code (`claude-code`) | `.claude/skills/` | Native `SKILL.md`; installer also writes `linkedin.<slug>.json` sidecar | verified |
| Cursor (`cursor`) | `.cursor/skills/` | `SKILL.md` + sidecar; add `Always apply` in Rules if you want it global | community |
| Windsurf (`windsurf`) | `.windsurf/skills/` | `SKILL.md` + sidecar; reference from `memories/` or rules as needed | community |
| VS Code + Copilot (`vscode`) | `.vscode/skills/` | `SKILL.md` + sidecar; point custom instructions at the folder | community |
| Cline (`cline`) | `.cline/skills/` | `SKILL.md` + sidecar | fallback |
| Roo Code (`roo`) | `.roo/skills/` | `SKILL.md` + sidecar | fallback |
| Zed (`zed`) | `.zed/skills/` | `SKILL.md` + sidecar; add to Assistant context | fallback |
| JetBrains AI (`jetbrains`) | `.idea/skills/` | `SKILL.md` + sidecar; attach in AI Assistant settings | fallback |
| Neovim agents (`neovim`) | `.nvim/skills/` | `SKILL.md` + sidecar; source from your plugin config | fallback |
| Generic / any other (`generic`) | `./linkedin-skills/<slug>/` | Copy only; wire the folder into your agent's system prompt or skill loader | fallback |

Auto-detect markers (scanned in `--target`): `.claude`, `.cursor`, `.windsurf`,
`.vscode`, `.cline`, `.roo`, `.zed`, `.idea`, `.nvim`.

> New IDE appears next year? You are covered: the canonical skill directory is
> plain markdown + JSON Schema. `generic` mode plus a one-row registry PR is the
> whole integration.

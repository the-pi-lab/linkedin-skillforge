"""Universal skill installer: copy any skill into any IDE/agent host. Stdlib only.

Usage:
    python ide/install.py list
    python ide/install.py install --skill prospect-research --ide cursor --target C:\\proj [--apply]
    python ide/install.py install --skill prospect-research --ide auto --target C:\\proj [--apply]
"""
from __future__ import annotations
import argparse, json, os, re, shutil, sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS_DIR = os.path.join(REPO_ROOT, "skills")

# host -> {dirs, wiring, confidence}. Keep honest: unverified entries are 'fallback'.
REGISTRY = {
    "claude-code": {"dirs": [".claude/skills"], "wiring": "Native SKILL.md support. Skill is picked up automatically.",
                    "confidence": "verified", "markers": [".claude"]},
    "cursor": {"dirs": [".cursor/skills"], "wiring": "Reference the folder from Cursor Rules / Composer context.",
               "confidence": "community", "markers": [".cursor"]},
    "windsurf": {"dirs": [".windsurf/skills"], "wiring": "Reference from Windsurf rules or memories as needed.",
                 "confidence": "community", "markers": [".windsurf"]},
    "vscode": {"dirs": [".vscode/skills"], "wiring": "Point Copilot custom instructions at the skill folder.",
               "confidence": "community", "markers": [".vscode"]},
    "cline": {"dirs": [".cline/skills"], "wiring": "Add the skill folder to Cline's context.",
              "confidence": "fallback", "markers": [".cline"]},
    "roo": {"dirs": [".roo/skills"], "wiring": "Add the skill folder to Roo Code context.",
            "confidence": "fallback", "markers": [".roo"]},
    "zed": {"dirs": [".zed/skills"], "wiring": "Include the folder in Zed Assistant context.",
            "confidence": "fallback", "markers": [".zed"]},
    "jetbrains": {"dirs": [".idea/skills"], "wiring": "Attach the folder in JetBrains AI Assistant settings.",
                  "confidence": "fallback", "markers": [".idea"]},
    "neovim": {"dirs": [".nvim/skills"], "wiring": "Source the folder from your agent plugin config.",
               "confidence": "fallback", "markers": [".nvim"]},
    "generic": {"dirs": ["linkedin-skills"], "wiring": "Wire the folder into your agent's system prompt or skill loader.",
                "confidence": "fallback", "markers": []},
}


def detect_ide(target):
    for host, info in REGISTRY.items():
        if host == "generic":
            continue
        for m in info["markers"]:
            if os.path.exists(os.path.join(target, m)):
                return host
    return "generic"


def skill_meta(slug):
    path = os.path.join(SKILLS_DIR, slug, "SKILL.md")
    if not os.path.isdir(os.path.join(SKILLS_DIR, slug)):
        raise SystemExit(f"Unknown skill '{slug}'. Available: {', '.join(sorted(os.listdir(SKILLS_DIR)))}")
    text = open(path, encoding="utf-8").read()
    fm = text.split("---")[1]
    out = {}
    for key in ("skill_id", "skill_name", "version", "category", "spec_version"):
        m = re.search(rf"^{key}:\s*(.+)$", fm, re.M)
        out[key] = m.group(1).strip() if m else "unknown"
    return out


def cmd_list():
    print(f"{'host':<12} {'skills dir':<22} {'confidence':<10} wiring")
    for host, info in REGISTRY.items():
        print(f"{host:<12} {info['dirs'][0]:<22} {info['confidence']:<10} {info['wiring']}")


def cmd_install(args):
    host = detect_ide(args.target) if args.ide == "auto" else args.ide
    if host not in REGISTRY:
        raise SystemExit(f"Unknown IDE '{args.ide}'. Run `install.py list`.")
    meta = skill_meta(args.skill)
    dest_dir = os.path.join(args.target, REGISTRY[host]["dirs"][0], f"linkedin.{args.skill}")
    manifest = {
        "skill_id": meta["skill_id"], "skill_name": meta["skill_name"],
        "version": meta["version"], "category": meta["category"],
        "spec_version": meta["spec_version"], "entry": "SKILL.md",
        "installed_for": host, "host_confidence": REGISTRY[host]["confidence"],
        "source": "linkedin-skills open-source repo (MIT)",
    }
    print(f"Skill : {meta['skill_id']} v{meta['version']}")
    print(f"Host  : {host} ({REGISTRY[host]['confidence']})")
    print(f"Copy  : skills/{args.skill}/ -> {dest_dir}/")
    print(f"Write : {dest_dir}.json manifest")
    print(f"Wiring: {REGISTRY[host]['wiring']}")
    if REGISTRY[host]["confidence"] == "fallback":
        print("NOTE  : host mapping is a fallback default — verify against your IDE docs.")
    if not args.apply:
        print("DRY-RUN: nothing changed. Re-run with --apply to execute.")
        return
    if not os.path.isdir(args.target):
        raise SystemExit(f"Target dir does not exist: {args.target}")
    src = os.path.join(SKILLS_DIR, args.skill)
    shutil.copytree(src, dest_dir, dirs_exist_ok=True)
    with open(dest_dir + ".json", "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)
    print(f"INSTALLED: {dest_dir} (+ manifest)")


def main(argv=None):
    ap = argparse.ArgumentParser(description="Install a LinkedIn skill into any IDE.")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("list", help="List supported IDE hosts")
    ins = sub.add_parser("install", help="Install a skill (dry-run unless --apply)")
    ins.add_argument("--skill", required=True, help="Skill slug, e.g. prospect-research")
    ins.add_argument("--ide", required=True, help="'auto', 'generic', or a host from list")
    ins.add_argument("--target", required=True, help="Project root to install into")
    ins.add_argument("--apply", action="store_true", help="Execute (default is dry-run)")
    args = ap.parse_args(argv)
    if args.cmd == "list":
        cmd_list()
    else:
        cmd_install(args)


if __name__ == "__main__":
    main()

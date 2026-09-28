"""Self-evolution gatekeeper: record runs, validate proposals, apply only with human approval. Stdlib only.

Commands (dry-run unless --apply on `apply`):
    evolve.py record --skill <slug> --outcome succeeded|partial|failed|refused [--confidence F] [--human-rating 1-5] [--reused] [--eval-passed/--eval-failed] --notes "..."
    evolve.py propose --skill <slug> --from-runs run-1,run-2 --change-type threshold|wording|checklist-add|example|eval-add|order-steps --summary "..." --files SKILL.md --version-bump patch|minor|major --changelog "..." --rollback "..."
    evolve.py validate --proposal evolution/proposals/<id>.json
    evolve.py apply --proposal evolution/proposals/<id>.json --approve "Human Name" [--apply]
"""
from __future__ import annotations
import argparse, datetime, json, os, re, sys, tempfile, uuid

EVO_ROOT = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(EVO_ROOT)
RUNS_LOG = os.path.join(EVO_ROOT, "runs.jsonl")
PROPOSALS = os.path.join(EVO_ROOT, "proposals")
AUDIT = os.path.join(EVO_ROOT, "AUDIT_LOG.md")

ALLOWLIST = {"threshold", "wording", "checklist-add", "example", "eval-add", "order-steps"}
BLOCK_PATTERNS = ["bypass", "remove approval", "remove opt-out", "uncapped", "delete eval",
                  "weaken", "skip validation", "no approval", "disable cap"]
RISKY_SKILLS = {"outreach-automation", "cold-messaging", "ai-agent-development",
                "workflow-automation", "ads-management", "api-integration"}


def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def atomic_write(path, content):
    """Write a file atomically so an interrupted release cannot truncate it."""
    directory = os.path.dirname(path) or "."
    os.makedirs(directory, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix=".evolve-", dir=directory, text=True)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as f:
            f.write(content)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, path)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)


def audit(event):
    with open(AUDIT, "a", encoding="utf-8") as f:
        f.write(f"- {now()} {event}\n")


def skill_exists(slug):
    return os.path.isdir(os.path.join(REPO_ROOT, "skills", slug))


def slug_of(skill_id_or_slug):
    return skill_id_or_slug.split(".", 1)[-1]


def validate_run_record(rec):
    """Validate the safety-critical parts of a run record without third-party deps."""
    errors = []
    if not re.fullmatch(r"run-[a-z0-9-]+", str(rec.get("run_id", ""))):
        errors.append("run_id must use the run-<id> format")
    if not re.fullmatch(r"linkedin\.[a-z0-9-]+", str(rec.get("skill_id", ""))):
        errors.append("skill_id must be linkedin.<slug>")
    if not skill_exists(slug_of(rec.get("skill_id", ""))):
        errors.append("unknown skill")
    if rec.get("outcome") not in {"succeeded", "partial", "failed", "refused"}:
        errors.append("invalid outcome")
    confidence = rec.get("output_confidence")
    if confidence is not None and (not isinstance(confidence, (int, float)) or not 0 <= confidence <= 1):
        errors.append("output_confidence must be between 0 and 1")
    rating = rec.get("human_rating")
    if rating is not None and (not isinstance(rating, int) or not 1 <= rating <= 5):
        errors.append("human_rating must be an integer from 1 to 5")
    if len(str(rec.get("notes", ""))) > 1000 or not str(rec.get("notes", "")).strip():
        errors.append("notes must be non-empty and <=1000 characters")
    return errors


def load_runs():
    if not os.path.exists(RUNS_LOG):
        return []
    records = []
    with open(RUNS_LOG, encoding="utf-8") as f:
        for line_no, line in enumerate(f, 1):
            if not line.strip():
                continue
            try:
                rec = json.loads(line)
            except json.JSONDecodeError as exc:
                raise SystemExit(f"Invalid JSON in runs.jsonl line {line_no}: {exc}")
            errors = validate_run_record(rec)
            if errors:
                raise SystemExit(f"Invalid run record line {line_no}: {'; '.join(errors)}")
            records.append(rec)
    return records


def cmd_record(a):
    slug = slug_of(a.skill)
    if not skill_exists(slug):
        raise SystemExit(f"Unknown skill '{a.skill}'")
    rec = {"run_id": f"run-{uuid.uuid4().hex}",
           "skill_id": f"linkedin.{slug}", "skill_version": a.skill_version,
           "input_hash": a.input_hash, "outcome": a.outcome,
           "output_confidence": a.confidence, "human_rating": a.human_rating,
           "downstream_reused": bool(a.reused), "eval_passed": a.eval,
           "notes": a.notes}
    errors = validate_run_record(rec)
    if errors:
        raise SystemExit("Invalid run record: " + "; ".join(errors))
    with open(RUNS_LOG, "a", encoding="utf-8") as f:
        f.write(json.dumps(rec) + "\n")
    audit(f"record {rec['run_id']} {rec['skill_id']} outcome={a.outcome}")
    print(f"Recorded {rec['run_id']} for linkedin.{slug}. Evidence for future proposals.")


def cmd_score(a):
    slug = slug_of(a.skill) if a.skill else None
    runs = [r for r in load_runs() if slug is None or slug_of(r["skill_id"]) == slug]
    if slug and not skill_exists(slug):
        raise SystemExit(f"Unknown skill '{a.skill}'")
    total = len(runs)
    succeeded = sum(r["outcome"] == "succeeded" for r in runs)
    rated = [r for r in runs if r.get("human_rating") is not None]
    evald = [r for r in runs if r.get("eval_passed") is not None]
    passed = sum(r.get("eval_passed") is True for r in evald)
    confidence_values = [r["output_confidence"] for r in runs if r.get("output_confidence") is not None]
    score = {
        "skill_id": f"linkedin.{slug}" if slug else None,
        "runs": total,
        "success_rate": round(succeeded / total, 4) if total else None,
        "eval_pass_rate": round(passed / len(evald), 4) if evald else None,
        "human_approval_rate": round(sum(r["human_rating"] >= 4 for r in rated) / len(rated), 4) if rated else None,
        "mean_confidence": round(sum(confidence_values) / len(confidence_values), 4) if confidence_values else None,
        "reused_rate": round(sum(r.get("downstream_reused", False) for r in runs) / total, 4) if total else None,
        "candidate": bool(rated and len(rated) >= 10 and sum(r["human_rating"] >= 4 for r in rated) / len(rated) < 0.8),
    }
    print(json.dumps(score, indent=2))


def cmd_propose(a):
    slug = slug_of(a.skill)
    if not skill_exists(slug):
        raise SystemExit(f"Unknown skill '{a.skill}'")
    if a.change_type not in ALLOWLIST:
        raise SystemExit(f"change-type '{a.change_type}' not evolvable. Allowlist: {sorted(ALLOWLIST)}")
    runs = [r.strip() for r in a.from_runs.split(",") if r.strip()]
    if not runs:
        raise SystemExit("Proposals without cited run records are rejected (anti-gaming). Use --from-runs run-1,run-2")
    os.makedirs(PROPOSALS, exist_ok=True)
    pid = f"prop-{int(datetime.datetime.now().timestamp())}"
    prop = {"proposal_id": pid, "skill_id": f"linkedin.{slug}", "base_version": a.base_version,
            "change_type": a.change_type, "summary": a.summary, "cites_runs": runs,
            "files_touched": [f.strip() for f in a.files.split(",")],
            "version_bump": a.version_bump, "changelog_entry": a.changelog,
            "rollback_plan": a.rollback, "approval": ""}
    path = os.path.join(PROPOSALS, pid + ".json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(prop, f, indent=2)
    audit(f"propose {pid} {prop['skill_id']} type={a.change_type}")
    print(f"Drafted {path}. Next: validate, then human approval. Nothing in skills/ changed.")


def validate_proposal(prop):
    errors = []
    slug = slug_of(prop.get("skill_id", ""))
    if not skill_exists(slug):
        errors.append(f"unknown skill {prop.get('skill_id')}")
    if prop.get("change_type") not in ALLOWLIST:
        errors.append(f"change-type '{prop.get('change_type')}' not evolvable")
    if not prop.get("cites_runs"):
        errors.append("insufficient evidence: cites_runs empty (anti-gaming)")
    if len(str(prop.get("summary", ""))) < 20:
        errors.append("summary too short to review")
    blob = json.dumps(prop).lower()
    if not re.fullmatch(r"\d+\.\d+\.\d+", str(prop.get("base_version", ""))):
        errors.append("base_version must be semver")
    if not re.fullmatch(r"\d+\.\d+\.\d+", str(prop.get("version_bump", ""))) and prop.get("version_bump") not in {"patch", "minor", "major"}:
        errors.append("version_bump must be patch, minor, or major")
    touched = prop.get("files_touched", [])
    if not isinstance(touched, list) or not touched:
        errors.append("files_touched must be a non-empty list")
    for filename in touched if isinstance(touched, list) else []:
        normalized = str(filename).replace("\\", "/")
        if normalized.startswith("/") or ".." in normalized.split("/"):
            errors.append("files_touched contains an unsafe path")
        if normalized not in {"SKILL.md", "README.md", "examples/example-basic.md", "examples/example-advanced.md", "tests/eval.json"}:
            errors.append(f"file is outside the evolution allowlist: {filename}")
    for pat in BLOCK_PATTERNS:
        if pat in blob:
            errors.append(f"blocklisted pattern '{pat}' — fail-closed, human review required")
    if re.search(r"schema\.json", blob) and prop.get("version_bump") != "major":
        errors.append("schema.json touched without major bump")
    tools_widen = "tools_required" in blob or "permissions_required" in blob
    if tools_widen:
        errors.append("tool/permission widening requires full review, not evolution loop")
    if slug in RISKY_SKILLS and prop.get("change_type") == "threshold":
        if not str(prop.get("rollback_plan", "")).strip():
            errors.append("risky-skill threshold change needs explicit rollback_plan")
    if not str(prop.get("rollback_plan", "")) or len(str(prop.get("rollback_plan"))) < 10:
        errors.append("rollback_plan missing or too short")
    return errors


def cmd_validate(a):
    prop = json.load(open(a.proposal, encoding="utf-8"))
    errors = validate_proposal(prop)
    if errors:
        print(f"INVALID {prop.get('proposal_id')}:")
        for e in errors:
            print(f"  - {e}")
        audit(f"validate {prop.get('proposal_id')} FAIL ({len(errors)})")
        sys.exit(1)
    print(f"VALID {prop.get('proposal_id')}: gates pass. Still needs human --approve to apply.")
    audit(f"validate {prop.get('proposal_id')} OK")


def bump_version(ver, kind):
    major, minor, patch = (list(map(int, ver.split("."))) + [0, 0, 0])[:3]
    if kind == "major":
        return f"{major + 1}.0.0"
    if kind == "minor":
        return f"{major}.{minor + 1}.0"
    return f"{major}.{minor}.{patch + 1}"


def cmd_apply(a):
    prop = json.load(open(a.proposal, encoding="utf-8"))
    errors = validate_proposal(prop)
    if errors:
        print("Cannot apply: proposal fails validation. Fix it, don't force it.");
        sys.exit(1)
    if not a.approve or len(a.approve.strip()) < 3:
        raise SystemExit("Human approval required: --approve \"Your Name\"")
    slug = slug_of(prop["skill_id"])
    print(f"Proposal : {prop['proposal_id']} ({prop['change_type']})")
    print(f"Skill    : linkedin.{slug} {prop['base_version']} -> {bump_version(prop['base_version'], prop['version_bump'])}")
    print(f"Approver : {a.approve}")
    print(f"Note     : content patch is authored by agent/human; this tool records approval, bumps version, writes changelog + audit.")
    if not a.apply:
        print("DRY-RUN: nothing changed. Re-run with --apply to release.")
        return
    skill_md = os.path.join(REPO_ROOT, "skills", slug, "SKILL.md")
    text = open(skill_md, encoding="utf-8").read()
    new_ver = bump_version(prop["base_version"], prop["version_bump"])
    text = text.replace(f"version: {prop['base_version']}", f"version: {new_ver}", 1)
    text = text.replace('"version": "%s"' % prop["base_version"], '"version": "%s"' % new_ver, 1)
    marker = "Changelog:"
    entry = f"{marker} [{new_ver}] {prop['changelog_entry']} (via {prop['proposal_id']}, approved by {a.approve})"
    if marker in text:
        text = text.replace(marker, entry, 1)
    else:
        text = text.rstrip() + f"\n\n{entry}\n"
    atomic_write(skill_md, text)
    prop["approval"] = a.approve
    with open(a.proposal, "w", encoding="utf-8") as f:
        json.dump(prop, f, indent=2)
    audit(f"apply {prop['proposal_id']} linkedin.{slug} -> {new_ver} approved by {a.approve}")
    print(f"RELEASED linkedin.{slug} v{new_ver}. Monitor next runs; regression -> ROLLBACK proposal.")


def main(argv=None):
    ap = argparse.ArgumentParser(description="Self-evolution gatekeeper for LinkedIn skills.")
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("record"); r.add_argument("--skill", required=True); r.add_argument("--outcome", required=True, choices=["succeeded", "partial", "failed", "refused"]); r.add_argument("--skill-version", default="1.0.0"); r.add_argument("--input-hash", default="unhashed"); r.add_argument("--confidence", type=float, default=0.5); r.add_argument("--human-rating", type=int, default=None); r.add_argument("--reused", action="store_true"); g = r.add_mutually_exclusive_group(); g.add_argument("--eval-passed", dest="eval", action="store_true", default=None); g.add_argument("--eval-failed", dest="eval", action="store_false"); r.add_argument("--notes", required=True)
    s = sub.add_parser("score", help="Summarize evidence and identify evolution candidates"); s.add_argument("--skill", default="", help="Optional skill slug")
    p = sub.add_parser("propose"); p.add_argument("--skill", required=True); p.add_argument("--from-runs", required=True); p.add_argument("--change-type", required=True); p.add_argument("--summary", required=True); p.add_argument("--files", default="SKILL.md"); p.add_argument("--base-version", default="1.0.0"); p.add_argument("--version-bump", default="patch"); p.add_argument("--changelog", required=True); p.add_argument("--rollback", required=True)
    v = sub.add_parser("validate"); v.add_argument("--proposal", required=True)
    y = sub.add_parser("apply"); y.add_argument("--proposal", required=True); y.add_argument("--approve", default=""); y.add_argument("--apply", action="store_true")
    args = ap.parse_args(argv)
    {"record": cmd_record, "score": cmd_score, "propose": cmd_propose, "validate": cmd_validate, "apply": cmd_apply}[args.cmd](args)


if __name__ == "__main__":
    main()

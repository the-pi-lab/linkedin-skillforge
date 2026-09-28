"""Tests for ide/ + evolution/ layers (stdlib only). Usage: python tests/test_new_layers.py"""
import json, os, subprocess, sys, tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
failures = []


def check(name, cond, detail=""):
    print(("PASS " if cond else "FAIL ") + name + (f" ({detail})" if detail and not cond else ""))
    if not cond:
        failures.append(name + (f": {detail}" if detail else ""))


# --- ide/ layer ---
sys.path.insert(0, os.path.join(ROOT, "ide"))
import install as inst
check("ide registry >= 10 hosts", len(inst.REGISTRY) >= 10, str(len(inst.REGISTRY)))
for host, info in inst.REGISTRY.items():
    for k in ("dirs", "wiring", "confidence", "markers"):
        check(f"ide/{host} has {k}", k in info and info[k] or k == "markers", k)
    check(f"ide/{host} confidence valid", info["confidence"] in ("verified", "community", "fallback"), info["confidence"])
check("ide registry doc exists", os.path.exists(os.path.join(ROOT, "ide", "IDE_REGISTRY.md")))
# dry-run install resolves a real skill without touching disk
r = subprocess.run([sys.executable, os.path.join(ROOT, "ide", "install.py"), "install",
                    "--skill", "prospect-research", "--ide", "cursor", "--target", tempfile.gettempdir()],
                   capture_output=True, text=True)
check("ide install dry-run ok", r.returncode == 0 and "DRY-RUN" in r.stdout, r.stderr[-300:])
# real apply into temp dir, then verify copied tree + manifest
with tempfile.TemporaryDirectory() as t:
    r = subprocess.run([sys.executable, os.path.join(ROOT, "ide", "install.py"), "install",
                        "--skill", "cold-messaging", "--ide", "generic", "--target", t, "--apply"],
                       capture_output=True, text=True)
    dest = os.path.join(t, "linkedin-skills", "linkedin.cold-messaging")
    check("ide install apply ok", r.returncode == 0 and os.path.exists(os.path.join(dest, "SKILL.md")), r.stderr[-300:])
    man = dest + ".json"
    check("ide manifest written", os.path.exists(man))
    if os.path.exists(man):
        m = json.load(open(man, encoding="utf-8"))
        check("ide manifest skill_id", m.get("skill_id") == "linkedin.cold-messaging", str(m.get("skill_id")))

# --- evolution/ layer ---
for f in ("EVOLUTION.md", "README.md", "evolve.py", "AUDIT_LOG.md", "SCORECARD.md",
          "schemas/run-record.json", "schemas/proposal.json"):
    check(f"evolution/{f} exists", os.path.exists(os.path.join(ROOT, "evolution", f)))
rr = json.load(open(os.path.join(ROOT, "evolution", "schemas", "run-record.json"), encoding="utf-8"))
pr = json.load(open(os.path.join(ROOT, "evolution", "schemas", "proposal.json"), encoding="utf-8"))
check("run-record schema required fields", set(["run_id", "skill_id", "outcome"]) <= set(rr.get("required", [])), str(rr.get("required")))
check("proposal schema cites_runs required", "cites_runs" in pr.get("required", []), str(pr.get("required"))
)
check("proposal change_type allowlist", set(pr["properties"]["change_type"]["enum"]) <= {"threshold", "wording", "checklist-add", "example", "eval-add", "order-steps"})
sys.path.insert(0, os.path.join(ROOT, "evolution"))
import evolve as ev
good = {"proposal_id": "prop-t", "skill_id": "linkedin.cold-messaging", "base_version": "1.0.0",
        "change_type": "wording", "summary": "Clarify follow-up timing with evidence from runs",
        "cites_runs": ["run-1"], "files_touched": ["SKILL.md"], "version_bump": "patch",
        "changelog_entry": "clearer bump timing", "rollback_plan": "restore prior wording verbatim"}
check("evolve accepts good proposal", ev.validate_proposal(good) == [], str(ev.validate_proposal(good)))
bad = dict(good, summary="Remove approval gates for uncapped bypass blasting runs")
check("evolve rejects gate-removal", len(ev.validate_proposal(bad)) > 0, "blocklist missed")
noev = dict(good, cites_runs=[])
check("evolve rejects evidence-free", any("evidence" in e for e in ev.validate_proposal(noev)), "anti-gaming missed")
sche = dict(good, change_type="wording", files_touched=["schema.json"], version_bump="patch")
check("evolve forces major on schema touch", any("major" in e for e in ev.validate_proposal(sche)), "semver gate missed")

if failures:
    print(f"\nFAIL ({len(failures)}):")
    [print(" -", f) for f in failures]
    sys.exit(1)
print("\nPASS: ide + evolution layers healthy")

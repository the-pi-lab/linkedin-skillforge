"""Contract validator for all 40 skills (stdlib only). Usage: python tests/test_skill_contract.py"""
import json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS = os.path.join(ROOT, "skills")
REQUIRED_SECTIONS = ["Identity","Purpose","When To Use","When NOT To Use","Capabilities","Inputs","Input Schema","Outputs","Output Schema","Preconditions","Required Context","Optional Context","Reasoning Process","Execution Workflow","Decision Rules","Validation","Error Handling","Failure Recovery","Tool Interfaces","Security","Compliance","Quality Standards","Examples","Anti-Examples","Evaluation Criteria","Chaining","Versioning"]
FORBIDDEN = ["session cookie", "captcha bypass", "bypassing captcha", "credential theft", "hijack session"]
failures = []
skills = sorted([d for d in os.listdir(SKILLS) if os.path.isdir(os.path.join(SKILLS, d))])
print(f"Found {len(skills)} skills")
if len(skills) != 40:
    failures.append(f"Expected 40 skills, found {len(skills)}: {skills}")
for slug in skills:
    base = os.path.join(SKILLS, slug)
    for rel in ["SKILL.md", "schema.json", "README.md", "examples/example-basic.md", "examples/example-advanced.md", "tests/eval.json"]:
        if not os.path.exists(os.path.join(base, rel)):
            failures.append(f"{slug}: missing {rel}")
    p = os.path.join(base, "SKILL.md")
    if os.path.exists(p):
        text = open(p, encoding="utf-8").read()
        if not text.startswith("---"):
            failures.append(f"{slug}: missing frontmatter")
        else:
            fm = text.split("---")[1]
            for k in ["skill_id", "skill_name", "version", "category", "spec_version"]:
                if k not in fm:
                    failures.append(f"{slug}: frontmatter missing {k}")
            m = re.search(r"skill_id:\s*linkedin\.([a-z0-9-]+)", fm)
            if m and m.group(1) != slug:
                failures.append(f"{slug}: skill_id slug mismatch ({m.group(1)})")
        for sec in REQUIRED_SECTIONS:
            if f"## {sec}" not in text:
                failures.append(f"{slug}: missing section ## {sec}")
        low = text.lower()
        for pat in FORBIDDEN:
            if pat in low and "forbidden" not in low[max(0, low.find(pat)-200):low.find(pat)]:
                # allow only if discussed as forbidden; crude check: flag if imperative
                if "do not" not in low[max(0, low.find(pat)-200):low.find(pat)+200] and "never" not in low[max(0, low.find(pat)-200):low.find(pat)+200] and "forbidden" not in low:
                    failures.append(f"{slug}: suspicious forbidden pattern '{pat}'")
        if "confidence" not in low or "provenance" not in low or "gaps" not in low:
            failures.append(f"{slug}: must discuss provenance/confidence/gaps")
    sp = os.path.join(base, "schema.json")
    if os.path.exists(sp):
        try:
            s = json.load(open(sp, encoding="utf-8"))
            for key in ["$schema", "skill_id", "title", "properties"]:
                if key not in s:
                    failures.append(f"{slug}/schema.json: missing {key}")
            props = s.get("properties", {})
            if "Input" not in props or "Output" not in props:
                failures.append(f"{slug}/schema.json: must define Input and Output")
        except Exception as e:
            failures.append(f"{slug}/schema.json invalid: {e}")
    ep = os.path.join(base, "tests/eval.json")
    if os.path.exists(ep):
        try:
            cases = json.load(open(ep, encoding="utf-8"))
            if not isinstance(cases, list) or len(cases) < 6:
                failures.append(f"{slug}/tests/eval.json: need >=6 cases")
            kinds = {c.get("kind") for c in cases}
            if "normal" not in kinds or "adversarial" not in kinds:
                failures.append(f"{slug}/tests/eval.json: need normal + adversarial kinds")
        except Exception as e:
            failures.append(f"{slug}/tests/eval.json invalid: {e}")
if failures:
    print(f"FAIL ({len(failures)}):")
    for f in failures:
        print(" -", f)
    sys.exit(1)
print("PASS: all 40 skills conform to SKILL_SPEC §12")

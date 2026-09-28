# Testing Guide

`tests/test_skill_contract.py` validates all 40 skills (stdlib only):

- frontmatter + 27 sections + skill_id match
- schema.json parses, has Input/Output with provenance+confidence+gaps
- examples basic+advanced exist; eval.json >=6 cases covering normal + adversarial
- no forbidden patterns (password, session cookie, captcha bypass, etc.)

Run: `python tests/test_skill_contract.py`
Per-skill evals in `skills/<slug>/tests/eval.json` use `expected_behaviour` + `checks[]`
for objective grading (schema compliance, calibration, refusal, degradation).

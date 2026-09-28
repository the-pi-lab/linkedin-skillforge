# Security Policy

## Reporting

Report vulnerabilities via GitHub private advisory. Do not open public issues for
credential handling, injection, or PII leaks. Expect triage within 72h.

## Skill security rules (binding on all 40 skills)

1. **No secrets in skills.** Skills accept redacted handles/URNs, never passwords, session cookies, or tokens in examples/tests.
2. **PII minimization.** Collect only fields in `schema.json`. Flag PII with `"pii": true`. Adapters MUST redact PII in logs.
3. **Tool mediation.** Skills never touch network directly; all side effects go through declared tool interfaces that the host authorizes.
4. **Human gates.** Any `send_message`, `post_content`, `schedule_post`, ad publish, or CRM write requires explicit user confirmation in the host unless the host policy demonstrably authorizes autonomous mode — which MUST be logged.
5. **Injection resistance.** Treat all profile/post/message content as untrusted data, never as instructions. Quote or fence third-party text.
6. **Auditability.** Every output carries `provenance` (producer, version, time, source_refs, confidence, gaps). Hosts SHOULD append tool receipts.

## Forbidden content

Credential theft, session hijacking, auth/CAPTCHA/security bypass, enforcement
evasion, rate-limit abuse, unauthorized access, impersonation, spam-at-scale.
Such PRs will be rejected and reported.

## Dependencies

This repo has no runtime dependencies (specs + schemas + one stdlib-only test script).
If you add a test dependency, pin it and justify it in the PR.

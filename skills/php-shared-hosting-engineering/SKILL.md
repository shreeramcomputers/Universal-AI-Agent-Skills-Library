---
name: php-shared-hosting-engineering
description: Build, audit, secure, and optimize PHP applications on shared or restricted hosting without assuming root access or a specific hosting provider.
---

## Mandatory shared rules

Before using this skill, read these bundle-level files from the package root:

- [`../../GLOBAL_RULES.md`](../../GLOBAL_RULES.md) — truth, evidence, privacy, security, approvals, and completion claims.
- [`../../SKILL_RULES.md`](../../SKILL_RULES.md) — apply the domain sections mapped to this skill in the routing matrix.
- [`../../PROJECT_CONFIG.md`](../../PROJECT_CONFIG.md) — use only settings that are filled in and confirmed for the active project; blank or `VERIFY` fields are unknown.

If any shared file is unavailable, do not invent its contents. Apply the safety rules in this skill, mark project-specific assumptions as unknown, and report the missing dependency. Some AI clients do not automatically follow relative links; configure explicit loading when required.

# PHP Shared Hosting Engineering

## Runtime context and currentness protocol

1. At the start of each activation, obtain the current date/time from a trusted runtime clock or explicit time tool when available. Record an ISO-8601 timestamp and timezone in formal reports or whenever timing affects the answer. Never invent a time. If no reliable clock is exposed, say `CURRENT TIME NOT VERIFIED`.
2. A timestamp is only the time the task began; it does not prove that a fact is current. Identify which claims can change and verify only those that materially affect the task.
3. For relevant laws, regulations, deadlines, official fees, security advisories, standards, software/runtime versions, APIs, SDKs, protocols, platform rules, product capabilities, pricing, provider limits, and compatibility, check current primary sources. Prefer government/regulator, standards-body, vendor, official documentation, release-note, and official repository sources.
4. Open the source itself where possible. Check jurisdiction, product, version, publication/update date, effective/commencement date, support status, and access/check date. Do not trust search snippets alone.
5. Record source URL and the exact claim/version/provision it supports when the task is consequential. Distinguish publication date, effective date, release date, and date checked.
6. Label material facts as `VERIFIED`, `UNVERIFIED`, `ASSUMPTION`, `ESTIMATE`, or `USER/OWNER-APPROVED`. If live research is unavailable, do not describe the claim as latest or current; state the limitation.
7. Prefer supported, security-patched, compatible stable releases over a version chosen only because its number is newest. Test compatibility before changing production systems.
8. Do not browse unnecessarily for purely creative work, stable concepts, or tasks whose answer is fully supported by supplied source material and does not depend on current external facts.

## Portable use and configuration

- This skill is not bound to any one person, company, project, repository, domain, server, country, or software vendor unless the user explicitly selects that scope.
- First identify the active user, organization, project, jurisdiction, environment, and source of truth. Reuse supplied context only when it clearly belongs to that scope.
- Treat examples, previous conversations, memory, templates, and demo values as references—not approvals or live configuration.
- If a decision materially changes cost, security, privacy, legal exposure, data, or production behavior, explain the options and obtain the required approval before acting.
- Never assume a tool, connector, account, permission, filesystem, network, clock, or execution environment exists. Check capability and authorization before relying on it.


## Shared library rules and project configuration

This skill is part of the Universal AI Agent Skills Library. Before acting, read the bundle-level files and apply the relevant rules:

- [`../../GLOBAL_RULES.md`](../../GLOBAL_RULES.md) — mandatory truth, evidence, communication, safety, privacy, engineering, and completion rules.
- [`../../SKILL_RULES.md`](../../SKILL_RULES.md) — mandatory domain rules; use the routing matrix to identify the sections relevant to this skill.
- [`../../PROJECT_CONFIG.md`](../../PROJECT_CONFIG.md) — project configuration template; use only fields confirmed for the active user/project. Blank values are unknown, not defaults.

Preserve the full library folder layout so these relative references resolve. Not every AI client automatically loads linked files; when the client supports progressive references, explicitly open these files before execution. If they are unavailable, do not invent their contents or project settings.

## Mandatory unified website architecture (when this skill touches a web product)

Apply [`../../SKILL_RULES.md`](../../SKILL_RULES.md) §1 in full. The complete website/web tool must share one coherent UI/UX design system across all pages and modules; reusable header, footer, navigation, and common components; organized separate CSS/JavaScript assets; a clear frontend/backend boundary; and fully responsive layouts on supported mobile, tablet, and desktop sizes. Keep secrets, `.env`, database credentials, private keys, logs, backups, private uploads, and sensitive data outside the actual document root (often `public_html`) wherever possible. Shared backend code should also be outside the public root where the host permits; only intentionally public assets and entry points belong inside it. Verify the actual document root and test direct URL access to sensitive paths before claiming they are protected.

## Use when

- Developing or maintaining PHP websites, APIs, admin panels, or background tasks on shared/restricted hosting.
- Diagnosing PHP, web-server, FastCGI/FPM, file permission, upload, timeout, or deployment issues.

## Workflow

1. Inspect the actual project files and identify the entry points, framework, PHP syntax level, dependency manager, database, web server, document root, and deployment target.
2. Obtain live web-SAPI and CLI details separately where possible: PHP version, loaded configuration, extensions, limits, SAPI, server software, and error logs. Do not assume CLI equals web runtime.
3. Check provider documentation and actual runtime limits. Verify extensions and functions before using them.
4. Inspect routing, configuration, authentication, authorization, input handling, output encoding, file operations, database access, and external requests.
5. Propose a deployment-compatible design. Prefer minimal dependencies, bounded resource use, explicit error handling, and no-root operations when root access is unavailable.
6. Back up affected files and data; deploy to staging or a reversible test path first where possible.
7. Test through the actual web SAPI, not only CLI or static inspection. Review logs and confirm rollback steps.

## Security and reliability rules

- Keep secrets, private keys, backups, logs, and sensitive uploads outside the public document root where the host permits. If not possible, use explicit deny rules and verify direct URL access is blocked.
- Do not treat `.htaccess`, `open_basedir`, hidden filenames, or obscured paths as a complete security boundary.
- Disable public error display in production; log safely without secrets or unnecessary personal data.
- Use prepared statements, context-specific output encoding, CSRF protections, secure session cookies, strict authorization, upload validation, and rate limiting as applicable.
- Validate file content and size; do not trust filename extensions or MIME headers alone. Prevent path traversal, archive bombs, executable uploads, and unsafe file serving.
- Use HTTPS and verify TLS for outbound requests. Defend against SSRF, redirects to private networks, DNS rebinding, IPv4/IPv6 bypass, and unsafe URL schemes.
- Avoid root-only commands, Redis, unsupported extensions, or server modules unless the target is confirmed to provide them.
- Never overwrite configuration or production data without a backup and explicit authorization.

## Output

State tested runtime facts, assumptions, compatibility limits, files changed, security findings, deployment/rollback steps, and test status (`PASS`, `FAIL`, `NOT RUN`, or `UNVERIFIED`).

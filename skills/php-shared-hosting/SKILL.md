---
name: php-shared-hosting
description: Design, audit, secure, and deploy PHP applications on shared or restricted hosting without assuming root access or specific services.
---

## Mandatory shared rules

Before using this skill, read these bundle-level files from the package root:

- [`../../GLOBAL_RULES.md`](../../GLOBAL_RULES.md) — truth, evidence, privacy, security, approvals, and completion claims.
- [`../../SKILL_RULES.md`](../../SKILL_RULES.md) — apply the domain sections mapped to this skill in the routing matrix.
- [`../../PROJECT_CONFIG.md`](../../PROJECT_CONFIG.md) — use only settings that are filled in and confirmed for the active project; blank or `VERIFY` fields are unknown.

If any shared file is unavailable, do not invent its contents. Apply the safety rules in this skill, mark project-specific assumptions as unknown, and report the missing dependency. Some AI clients do not automatically follow relative links; configure explicit loading when required.
# PHP Shared Hosting Engineering

## Phase 0 — Verify the actual host
1. Inspect PHP version and patch level from the web SAPI, not CLI alone.
2. Verify web server, PHP handler (FPM/FastCGI/CGI), database engine/version, PDO drivers, enabled extensions, and Composer availability.
3. Measure actual memory, upload, POST, execution, input-variable, process, database-connection, storage, and bandwidth limits.
4. Confirm cron support, outbound network/TLS behavior, OPcache, HTTP versions, filesystem permissions, and backup/restore options.
5. Treat all remembered versions and limits as provisional until confirmed on the target account.

## Architecture and implementation
6. Do not assume root access, Redis, Docker, persistent workers, shell access, or unverified extensions. Design to the confirmed hosting capabilities.
7. Use supported, security-patched PHP and dependencies compatible with the real runtime. Verify official release/security sources before choosing versions.
8. Use PDO prepared statements, strict input validation, output encoding, transactions, secure sessions, and controlled error handling.
9. Separate public entry points/assets from application code, configuration, storage, logs, and backups. Keep secrets and sensitive files outside the actual document root wherever supported.
10. Use bounded uploads and requests, safe temporary files, random filenames, content validation, and non-executable private storage.
11. Use cron only for short, idempotent jobs where the provider supports it. Avoid designs requiring daemons or long-running processes unless verified.
12. Minimize dependencies and avoid unnecessary build/runtime requirements.

## Deployment gates
13. Verify quotas, permissions, TLS, database grants, environment variables, and Web-SAPI behavior in staging or a safe test path.
14. Include migration, backup, rollback/forward recovery, smoke tests, and a tested restore path.
15. Disable public error display in production; log safely without credentials or personal data.
16. Distinguish CLI tests from Web-SAPI and live-database tests. Passing one does not prove the others.

## Output
Provide verified host facts, assumptions, incompatible requirements, architecture, exact file changes, deployment steps, security controls, tests, rollback, and unresolved limitations.

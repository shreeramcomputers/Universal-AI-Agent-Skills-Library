---
name: secure-rest-api-engineering
description: Design, implement, test, and review secure REST/JSON APIs with clear contracts, authentication, authorization, abuse controls, and reliable error handling.
---

## Mandatory shared rules

Before using this skill, read these bundle-level files from the package root:

- [`../../GLOBAL_RULES.md`](../../GLOBAL_RULES.md) — truth, evidence, privacy, security, approvals, and completion claims.
- [`../../SKILL_RULES.md`](../../SKILL_RULES.md) — apply the domain sections mapped to this skill in the routing matrix.
- [`../../PROJECT_CONFIG.md`](../../PROJECT_CONFIG.md) — use only settings that are filled in and confirmed for the active project; blank or `VERIFY` fields are unknown.

If any shared file is unavailable, do not invent its contents. Apply the safety rules in this skill, mark project-specific assumptions as unknown, and report the missing dependency. Some AI clients do not automatically follow relative links; configure explicit loading when required.

# Secure REST API Engineering

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

- Creating, upgrading, documenting, integrating, or auditing HTTP APIs.
- Reviewing API authentication, object-level access, rate limits, webhooks, schemas, or versioning.

## Workflow

1. Define consumers, resources, operations, trust boundaries, data sensitivity, business invariants, service-level expectations, and threat model.
2. Inspect existing routes, OpenAPI/schema files, middleware, database constraints, logs, deployment environment, and client compatibility.
3. Check current HTTP, OAuth/OIDC, JWT, TLS, framework, API gateway, and provider guidance relevant to the design.
4. Define request/response schemas, status codes, pagination, filtering, versioning, idempotency, and error format before implementation.
5. Enforce authentication and per-resource authorization on the server for every operation. Prevent IDOR/BOLA and tenant-crossing access.
6. Validate input structurally and semantically; bound body size, complexity, pagination, execution time, and downstream fan-out.
7. Add rate limits, abuse detection, replay protection, secure CORS, safe caching, and audit logs based on risk.
8. Test normal, malformed, unauthorized, cross-tenant, replayed, duplicated, concurrent, and degraded-service cases.

## Rules

- Never trust client-provided roles, ownership, price, balance, status, permissions, or transaction success.
- Keep secrets out of source control, URLs, responses, and logs. Redact authorization headers and sensitive fields.
- Use TLS; validate certificates. Do not disable verification to make an integration work.
- Use stable machine-readable errors without stack traces or internal details.
- For webhooks, verify signatures, timestamps, replay windows, event identity, and idempotency before processing.
- Avoid unsafe mass assignment, excessive data exposure, unrestricted resource consumption, SSRF, injection, and insecure direct object references.
- Make breaking changes explicit and preserve documented compatibility only where it is safe and approved.
- Never claim an endpoint is live or tested unless it was actually reached and evidence was observed.

## Output

Provide API contract, threat model, authz matrix, request/response examples, error model, migration/versioning plan, tests, evidence, and unresolved risks.

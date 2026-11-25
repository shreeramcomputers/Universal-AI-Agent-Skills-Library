---
name: secure-rest-api
description: Design secure REST APIs with robust authentication, authorization, data validation, abuse controls, and safe operations.
---

## Mandatory shared rules

Before using this skill, read these bundle-level files from the package root:

- [`../../GLOBAL_RULES.md`](../../GLOBAL_RULES.md) — truth, evidence, privacy, security, approvals, and completion claims.
- [`../../SKILL_RULES.md`](../../SKILL_RULES.md) — apply the domain sections mapped to this skill in the routing matrix.
- [`../../PROJECT_CONFIG.md`](../../PROJECT_CONFIG.md) — use only settings that are filled in and confirmed for the active project; blank or `VERIFY` fields are unknown.

If any shared file is unavailable, do not invent its contents. Apply the safety rules in this skill, mark project-specific assumptions as unknown, and report the missing dependency. Some AI clients do not automatically follow relative links; configure explicit loading when required.
# Secure REST API Engineering

1. Define API purpose, trust boundaries, resource ownership, client types, and threat model.
2. Use explicit versioning and a consistent response/error contract. Document pagination and compatibility rules.
3. Authenticate non-public requests using an appropriate standard. Store verifiers/hashes rather than recoverable secrets where applicable.
4. Separate scopes for read, create, update, delete, approval, export, and administration. Enforce authorization on every object and action.
5. Validate content type, request size, identifiers, field lengths, pagination, encoding, and schema. Reject unexpected fields where appropriate.
6. Use prepared statements, safe serialization, output encoding, and strict allowlists for dynamic behavior.
7. Add rate limits, quotas, idempotency for retryable writes, replay protection, timeouts, and bounded external calls.
8. Configure CORS narrowly; use CSRF defenses for cookie-authenticated browser flows and secure cookie attributes.
9. Do not expose secrets, access tokens, OTPs, unnecessary personal data, or internal stack traces in logs or responses.
10. Test missing/expired/revoked credentials, wrong scope, cross-tenant/object IDs, privilege escalation, replay, duplicate writes, oversized payloads, malformed JSON, and degraded dependencies.
11. Use TLS verification and safe outbound request controls. Defend against SSRF, unsafe redirects, and private-network access where user-controlled URLs exist.
12. Document key rotation, revocation, monitoring, incident response, and backward-compatible deprecation.

## Output
Provide contract, auth/authz model, data-flow diagram or outline, threat model, error model, limits, tests, operational controls, and known gaps.

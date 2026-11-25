---
name: memory-governance
description: Govern durable AI memory creation, review, approval, versioning, expiry, retrieval, and deletion.
---

## Mandatory shared rules

Before using this skill, read these bundle-level files from the package root:

- [`../../GLOBAL_RULES.md`](../../GLOBAL_RULES.md) — truth, evidence, privacy, security, approvals, and completion claims.
- [`../../SKILL_RULES.md`](../../SKILL_RULES.md) — apply the domain sections mapped to this skill in the routing matrix.
- [`../../PROJECT_CONFIG.md`](../../PROJECT_CONFIG.md) — use only settings that are filled in and confirmed for the active project; blank or `VERIFY` fields are unknown.

If any shared file is unavailable, do not invent its contents. Apply the safety rules in this skill, mark project-specific assumptions as unknown, and report the missing dependency. Some AI clients do not automatically follow relative links; configure explicit loading when required.
# Memory Governance

1. Read the active system's governance policy and only the records relevant to the task.
2. Never treat historical, provisional, unverified, rejected, or expired records as current truth without fresh evidence.
3. Search by canonical subject/key and exact scope before creating a record.
4. For an exact duplicate, link to the canonical record; for a near duplicate, propose a merge; for a conflict, preserve both and request review.
5. Require explicit owner/user approval before converting uncertain conversation content into durable memory or changing critical rules.
6. Store immutable versions with author/approver, timestamp and timezone, reason, source, scope, and verification status.
7. Give temporary facts an expiry or review date. Retire stale records without erasing audit history where retention policy requires it.
8. Exclude passwords, OTPs, tokens, private keys, recovery secrets, payment credentials, customer records, and unnecessary sensitive personal data.
9. Keep records concise, structured, searchable, and limited to the purpose for which they are retained.
10. Provide user access, correction, export, and deletion paths consistent with applicable law and the system's retention policy.
11. Run schema and integrity validators after changes; update indexes/registries atomically where possible.

## Output
State what should be stored, what should not be stored, the proposed scope/status/expiry, provenance, conflicts, and the required approval. Do not claim memory was saved unless the storage system confirms it.

---
name: project-reverse-engineering
description: Understand and safely improve an existing software system before changing or replacing it.
---

## Mandatory shared rules

Before using this skill, read these bundle-level files from the package root:

- [`../../GLOBAL_RULES.md`](../../GLOBAL_RULES.md) — truth, evidence, privacy, security, approvals, and completion claims.
- [`../../SKILL_RULES.md`](../../SKILL_RULES.md) — apply the domain sections mapped to this skill in the routing matrix.
- [`../../PROJECT_CONFIG.md`](../../PROJECT_CONFIG.md) — use only settings that are filled in and confirmed for the active project; blank or `VERIFY` fields are unknown.

If any shared file is unavailable, do not invent its contents. Apply the safety rules in this skill, mark project-specific assumptions as unknown, and report the missing dependency. Some AI clients do not automatically follow relative links; configure explicit loading when required.
# Project Reverse Engineering

## Discovery
1. Inventory source files, entry points, routes, jobs, dependencies, configuration, schemas, permissions, external services, and deployment targets.
2. Read project documentation and existing tests. Identify the real runtime and supported compatibility range.
3. Trace representative flows end-to-end: request/event → validation → authorization → service/business logic → data access/external system → response/UI.
4. Build a dependency map and identify shared modules, duplicated logic, dead code candidates, and critical data paths.
5. Never infer that a file is unused from its name or lack of obvious references alone. Search dynamic includes, routing, reflection, scheduled jobs, and external callers before removal.

## Preservation and change
6. Record current behavior and business rules before modifying them. Separate verified behavior from assumptions and defects.
7. Protect secrets and private configuration; do not paste raw credentials, tokens, or customer data into reports.
8. Reproduce defects with safe test data and add regression coverage before or with the fix.
9. Prefer the smallest safe patch. Preserve public interfaces and data compatibility unless a breaking change is approved.
10. Include migration and rollback/forward-recovery for schema or data changes.
11. Test adjacent flows and security boundaries, not only the exact failing line.

## Reporting
12. Separate confirmed defects, security findings, design risks, technical debt, and optional improvements.
13. List inspected, changed, tested, untested, and blocked areas explicitly.
14. Do not claim the system is fully audited if parts were inaccessible or not tested.

---
name: github-delivery
description: Prepare safe Git commits, pull requests, repository documentation, CI, releases, and deployment workflows.
---

## Mandatory shared rules

Before using this skill, read these bundle-level files from the package root:

- [`../../GLOBAL_RULES.md`](../../GLOBAL_RULES.md) — truth, evidence, privacy, security, approvals, and completion claims.
- [`../../SKILL_RULES.md`](../../SKILL_RULES.md) — apply the domain sections mapped to this skill in the routing matrix.
- [`../../PROJECT_CONFIG.md`](../../PROJECT_CONFIG.md) — use only settings that are filled in and confirmed for the active project; blank or `VERIFY` fields are unknown.

If any shared file is unavailable, do not invent its contents. Apply the safety rules in this skill, mark project-specific assumptions as unknown, and report the missing dependency. Some AI clients do not automatically follow relative links; configure explicit loading when required.
# GitHub Delivery

## Before changes
1. Confirm the exact repository, owner, visibility, default branch, permissions, and intended target branch.
2. Read repository instructions (`AGENTS.md`, `CONTRIBUTING.md`, README, and relevant docs) before editing.
3. Inspect current branch status and existing files. Preserve unrelated work and avoid overwriting existing files without review.
4. Classify the data before publication. Never commit secrets, `.env`, credentials, private keys, production data, customer records, personal data, logs, database dumps, backups, or private configuration.
5. Keep repository visibility unchanged unless the owner explicitly requests and confirms a visibility change.

## Change workflow
6. Prefer a descriptive feature branch and pull request for multi-file or risky changes. Use small, reviewable commits.
7. Validate formatting, schemas, links, tests, security scans, and generated artifacts before committing.
8. Keep CI permissions minimal. Pin third-party Actions to verified immutable commit SHAs for production workflows; document update strategy.
9. Do not automate production deployment before access, target paths, secrets, compatibility, backup, approval, and rollback are verified.
10. Do not add or change a license without the rights holder's explicit choice. Public visibility alone does not grant reuse rights.
11. Protect against force pushes, stale branch updates, concurrent writes, and accidental commits to the default branch.

## Verify delivery
12. After writes, verify repository, branch, commit SHA, changed file paths, visibility, and pull-request state.
13. Distinguish files created, commit pushed, PR opened, PR merged, release published, and production deployed. They are separate states.
14. Report tests run, tests not run, unresolved warnings, and any remaining user action. Never claim deployment from a local commit alone.

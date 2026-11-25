# Changelog

## 4.0.0 — 2026-11-25

- Made a strict no-assumption, evidence-first, one-question-per-turn clarification protocol mandatory across all 45 Skills.
- Required AI agents to finish necessary clarification before starting the main task, without delaying independent work for optional details.
- Added an explicit truth-over-agreement rule: verify factual claims and respectfully correct unsafe, false, or unsupported statements.
- Standardized a single user-owned context template: `AI_CONTEXT.md`; removed the duplicate configuration concept.
- Updated installer, validator, documentation, and release packaging to use the canonical context filename.
- Added validation that every Skill contains the mandatory interaction contract.
- Kept private user context out of the public repository.

## 3.1.0

- Added bilingual guides, AI repository connection guidance, and Personal Assistant Context Steward workflow.

## 3.0.0

- Expanded and consolidated the skill library, shared governance, installer, validator, and CI checks.

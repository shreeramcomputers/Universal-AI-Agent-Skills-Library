# Validation Report — v4.0.0

**Date:** 2026-11-25  
**Branch:** `upgrade/v4.0.0-core-behavior-context`  
**Status:** Implementation in progress; validation must be rerun against the final branch head.

## Scope
- 45 existing Skills receive the mandatory no-assumption, one-question-per-turn, truth-over-agreement contract.
- Canonical context template is `AI_CONTEXT.md`.
- Installer, validator, release packaging, and user documentation are being aligned to the single context file.

## Required checks

| Check | Status |
|---|---|
| All Skill files contain the mandatory interaction contract | Pending final static validation |
| All Skill shared links resolve | Pending final static validation |
| No stale `PROJECT_CONFIG.md` references in active docs/tooling | Pending final scan |
| Catalogue matches the 45 Skill folders | Pending final static validation |
| Python validator unit tests | NOT RUN in this editing session |
| GitHub Actions CI | Pending PR run |
| Cross-client runtime behavior | NOT RUN; requires separate tests in each AI client |

Do not treat this report as a passing test result until the checks above are executed.

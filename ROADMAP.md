# Roadmap

This roadmap describes potential priorities, not promises or scheduled delivery.

## Current release — 4.0.0

- 45 focused, portable Agent Skills.
- Mandatory evidence-first, no-assumption, one-question-per-turn interaction contract across all 45 Skills.
- One canonical blank context template: `AI_CONTEXT.md`; completed user context stays private.
- Shared global/domain rules, installer, validator, unit tests, and GitHub Actions CI.
- Bilingual user guides, contribution/security/licensing documents, and release-packaging workflow.

**Release status:** v4.0.0 changes are merged into `main` and the latest main-branch validation workflow passed. The Git tag and published GitHub Release are still pending; creating tag `v4.0.0` will trigger the release workflow.

## Next priorities

1. Run controlled activation and behavior tests in named Agent Skills-compatible clients; record exact client, version, date, test cases, and results.
2. Add a small deterministic evaluation suite for activation, clarification, refusal boundaries, evidence quality, privacy, and completion claims.
3. Add structured examples and fixtures only for high-value skills where they improve repeatability.
4. Add focused reference files only where the main `SKILL.md` would otherwise become difficult to maintain.
5. Improve translations only when maintainers can review technical accuracy.
6. Strengthen release provenance and reproducibility checks, then record artifact hashes and validation evidence for each published release.

## Quality principles

- Prefer correctness, usefulness, safety, and maintainability over skill count.
- Add a new skill only for a distinct recurring workflow.
- Retire or merge overlap rather than keeping duplicate folders.
- Never claim cross-platform compatibility without testing.
- Keep public templates generic; never commit a user's private context file.

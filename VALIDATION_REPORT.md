# Validation Report — v3.0.0

## Automated checks

The repository includes:
- scripts/validate_skills.py — frontmatter, naming, description length, folder/name match, unique names, shared links, relative links, catalogue count/path parity, routing coverage, and known privacy/secret patterns.
- tests/test_validate_skills.py — unit tests for frontmatter parsing and name validation.
- .github/workflows/validate-skills.yml — runs validation and tests on pushes, pull requests, and manual dispatch.

## Expected repository invariants

- 44 unique skill folders.
- Each skill contains one SKILL.md with valid required fields.
- Skill names match directory names and follow the Agent Skills naming constraints.
- Each description is non-empty and no longer than 1024 characters.
- SKILL.md remains under 500 lines.
- All skills link to all three shared files.
- Catalogue names, paths, descriptions, and count match the folder tree.
- Every skill appears in the domain routing matrix.
- No known private owner/business identifiers or common secret patterns appear in skill instructions/shared rules.

## Verification status

- Source files and CI workflow: CREATED.
- Static validation in GitHub Actions: RUN BY WORKFLOW; final result must be read from the linked workflow run.
- Cross-client activation (Claude, Codex, Cursor, Copilot, Gemini, and others): NOT RUN unless separately recorded.
- Runtime behavior and tool execution: NOT GUARANTEED by static checks.
- Legal/licensing review by counsel: NOT PERFORMED.

This report must be updated if CI changes or checks are added/removed. Do not convert a test plan into a PASS claim.

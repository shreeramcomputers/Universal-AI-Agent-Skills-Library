# Repository instructions for AI coding agents

This repository is the public Universal AI Agent Skills Library. These rules apply when modifying this repository; they do not grant access to any external project or private data.

## Before editing
1. Read GLOBAL_RULES.md and the relevant sections of SKILL_RULES.md.
2. Read CONTRIBUTING.md, the target skill, and related tests/scripts.
3. Keep private SRC/user-specific information out of this public repository.
4. Check the current branch, working tree, and existing file contents before writing.

## Skill authoring
- Follow the Agent Skills specification: valid YAML frontmatter, name matching folder, description describing purpose and trigger.
- Keep SKILL.md focused and under 500 lines where practical; move long reference material into references/.
- Every skill must link to the shared root rules, define when to use it, provide an actionable workflow, guardrails, and a useful output.
- Add distinct capabilities only. Merge overlap rather than creating near-duplicate skills.
- Use portable, vendor-neutral language unless a skill is intentionally provider-specific.
- Do not copy third-party skill content. Study public guidance, cite sources where relevant, and write original material.

## Required checks
Run:
- python3 scripts/validate_skills.py
- python3 -m unittest discover -s tests -v

Update README.md, CATALOG.json, SKILL_RULES.md, CHANGELOG.md, and relevant docs when skill inventory or behavior changes. Report checks not run. Never claim cross-platform runtime compatibility without testing the named clients.

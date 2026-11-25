# Contributing

Thank you for helping improve the Universal AI Agent Skills Library.

## Before opening a contribution
- Read GLOBAL_RULES.md, SKILL_RULES.md, the relevant skill, and SECURITY.md.
- Search the current catalogue to avoid duplicate or overlapping skills.
- Confirm that all proposed material can legally be contributed under the repository's content or code license.
- Remove private information, secrets, customer data, and organization-specific settings.

## Adding or changing a skill
1. Create or update a folder under skills/<skill-name>/ with SKILL.md.
2. Use the Agent Skills format. The name must match the folder, be lowercase, use hyphens, and stay within 64 characters. The description must say what it does and when to use it and stay within 1024 characters.
3. Keep SKILL.md focused and under 500 lines where practical. Move detailed reference material to references/.
4. Include activation/use cases, a clear workflow, safety boundaries, failure paths, and an expected output.
5. Use portable instructions. Avoid one person's defaults, private URLs, private data, and unverified runtime assumptions.
6. Link to GLOBAL_RULES.md, relevant SKILL_RULES.md sections, and PROJECT_CONFIG.md.
7. Update CATALOG.json, README.md, SKILL_RULES.md, CHANGELOG.md, and installation/migration docs when relevant.
8. Add or update tests when scripts, validation, or machine-readable behavior changes.

## Quality requirements
- Prefer primary sources for current facts and cite exact claims.
- Do not copy a third-party skill, reference, or example unless its license permits the intended reuse and attribution is retained.
- Do not include executable scripts unless they have a clear purpose, safe inputs, error handling, documentation, and tests.
- Do not add a tool dependency just to perform a simple static check.
- Do not create broad, vague skills that duplicate several existing entries.
- State untested assumptions and platform-specific limitations.

## Run checks locally

```bash
python3 scripts/validate_skills.py
python3 -m unittest discover -s tests -v
```

## Pull requests
- Use a focused branch and explain the problem, intended change, affected skills, and user impact.
- Include test output and any manual client testing with exact client/version.
- Note licensing/attribution implications.
- Mark incomplete or unverified work clearly.
- Do not include secrets or private data in screenshots, logs, or test artifacts.

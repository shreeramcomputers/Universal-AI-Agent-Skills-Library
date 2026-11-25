# Migration Guide

## Upgrading from v2.2.0 to v3.0.0

Version 3.0.0 consolidates overlapping skills, adds 17 new skills, updates the shared rules, and adds a tested installation/validation toolchain.

### Renamed or consolidated skill folders

| Previous folder | v3.0.0 replacement |
|---|---|
| `php-shared-hosting` | `php-shared-hosting-engineering` |
| `secure-rest-api` | `secure-rest-api-engineering` |
| `memory-governance` | `memory-governance-and-source-control` |
| `project-planning` | `contract-first-project-planning` |

Review local customizations before replacing these folders. The new target skills should be treated as the maintained source of truth.

### New skills

See the 17 additions listed in CHANGELOG.md and the full CATALOG.json.

### Installation changes

Use scripts/install_skill.py to install selected folders together with the three shared files. This resolves an important portability issue: many single-skill installers copy only a skill folder and do not copy repository-root shared documents.

### Rules and configuration

- Review GLOBAL_RULES.md v3.0.0.
- Review the expanded SKILL_RULES.md routing matrix.
- Reconfirm AI_CONTEXT.md values for each project; do not transfer private settings from another project.
- The website architecture rule remains mandatory: unified UI/UX, reusable common layout/components, separate CSS/JS, frontend/backend separation, responsiveness, and private files outside the actual document root wherever supported.

### License change

The repository now uses CC BY 4.0 for skill/documentation content and MIT for scripts/tests/workflow code. Review LICENSE and LICENSE-CONTENT.md before redistribution.

### Validation

Run:
```bash
python3 scripts/validate_skills.py
python3 -m unittest discover -s tests -v
```

Client runtime testing is separate from static validation.

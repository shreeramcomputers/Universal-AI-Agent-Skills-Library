# Changelog\n\n## 3.1.0 — documentation and context workflow upgrade (under review)\n\n### Added\n- English and Hinglish repository user guides and per-Skill discovery/usage guides for all catalogue Skills.\n- Direct AI-to-GitHub connection guide covering read-only access, scoped connector access, MCP/API bridge safety, version pinning, and optional PHP adapter architecture.\n- Personal Assistant Context Steward Skill and transparent context export/review/import workflow.\n- Conditional website/software/application page standard with shared legal-content governance.\n\n### Safety and compatibility\n- Explicitly documents that hidden AI memory and provider databases are not automatically accessible or writable.\n- config.php may be the only user-edited configuration file, but must not contain secrets; secure credentials stay server-side.\n- No duplicate Skills added; one distinct personal-context stewardship capability added after checking existing context and memory Skills.

All notable library changes are documented here.

## 3.0.0 — 2026-11-25

### Added
- Expanded to 44 skills with new workflows for specification, TDD, debugging, code review, frontend UI, accessibility, performance, browser testing, CI/CD, observability/incident response, technical research, data analysis, product discovery, documentation/ADRs, supply-chain security, cloud architecture/cost, and workflow automation.
- Added an installation helper that copies selected skills and the shared rules as one coherent unit.
- Added a dependency-free validator, unit tests, GitHub Actions validation, and public contribution/security/support guidance.
- Added explicit content and code license scopes.

### Improved
- Standardized all retained skills with portable execution discipline and shared rule references.
- Consolidated overlapping skill folders and documented migration names.
- Updated the full catalogue, routing matrix, and website architecture/security standard.
- Added public repository hygiene: README, LICENSE, LICENSE-CONTENT, .gitignore, .gitattributes, .editorconfig, AGENTS.md, issue templates, and CI.

### Consolidated
- php-shared-hosting → php-shared-hosting-engineering
- secure-rest-api → secure-rest-api-engineering
- memory-governance → memory-governance-and-source-control
- project-planning → contract-first-project-planning

### Validation scope
- Static format/catalogue/link/routing/privacy checks are automated.
- Cross-client runtime activation and platform-specific tool behavior are not claimed without separate tests.

## 2.2.0 — 2026-11-25
- Expanded the 21-skill collection to 31 and generalized 10 reusable workflows from a separate private repository.
- Added mandatory shared files and a website UI/UX/security standard.

## 2.1.0 — 2026-11-25
- Added GLOBAL_RULES.md, SKILL_RULES.md, and PROJECT_CONFIG.md to the original skill collection.

# Universal AI Agent Skills Library

**A practical, open collection of portable Agent Skills for real work.**

[![Agent Skills format](https://img.shields.io/badge/format-Agent%20Skills-blue)](https://agentskills.io/)
[![Skills](https://img.shields.io/badge/skills-45-brightgreen)](skills/)
[![Validation](https://github.com/shreeramcomputers/Universal-AI-Agent-Skills-Library/actions/workflows/validate-skills.yml/badge.svg)](https://github.com/shreeramcomputers/Universal-AI-Agent-Skills-Library/actions/workflows/validate-skills.yml)
[![MIT code](https://img.shields.io/badge/code-MIT-green)](LICENSE)
[![CC BY 4.0 content](https://img.shields.io/badge/skill%20content-CC%20BY%204.0-blue)](LICENSE-CONTENT.md)

A vendor-neutral library of **45 reusable AI agent skills** for individuals, developers, teams, agencies, and organizations. It covers software engineering, web development, security, data, finance, product discovery, research, operations, and content workflows.

The library uses the open [Agent Skills format](https://agentskills.io/): each skill is a folder containing a `SKILL.md` with YAML frontmatter and clear task instructions. Skills are modular; use only the ones relevant to the job.

## Documentation in English and Hinglish

- [English user guide](docs/USER_GUIDE_EN.md)
- [Hinglish user guide](docs/USER_GUIDE_HINGLISH.md)
- [English guide for all 45 Skills](docs/ALL_SKILLS_GUIDE_EN.md)
- [Hinglish guide for all 45 Skills](docs/ALL_SKILLS_GUIDE_HINGLISH.md)
- [Connect an AI agent directly to this GitHub repository](docs/AI_REPOSITORY_CONNECTION.md)
- [Personal Assistant context export, review and import](docs/PERSONAL_ASSISTANT_DATA_WORKFLOW.md)
- [Website/software legal and project page standard](docs/WEBSITE_PROJECT_PAGE_STANDARD.md)

## Quick start

### Browse before installing

```bash
npx skills add shreeramcomputers/Universal-AI-Agent-Skills-Library --list
```

### Install one skill with its shared rules (recommended)

Clone the repository, then use the included dependency-free installer from your project directory:

```bash
git clone --depth 1 https://github.com/shreeramcomputers/Universal-AI-Agent-Skills-Library.git
python3 Universal-AI-Agent-Skills-Library/scripts/install_skill.py \
  --skill php-shared-hosting-engineering \
  --destination .agents/skills
```

Install more than one skill by repeating `--skill`. Install the complete collection with:

```bash
python3 Universal-AI-Agent-Skills-Library/scripts/install_skill.py \
  --all --destination .agents/skills
```

The installer copies the selected skill folders and places `GLOBAL_RULES.md`, `SKILL_RULES.md`, and `AI_CONTEXT.md` at the correct shared location. It refuses to overwrite existing files unless `--force` is provided. Review existing files before using that option.

### Install using a Skills-compatible CLI

```bash
npx skills add shreeramcomputers/Universal-AI-Agent-Skills-Library \
  --skill php-shared-hosting-engineering
```

**Important:** some CLI installers copy only the selected skill folder, not repository-root shared files. In that case, copy the three shared files into the location expected by the installed relative links, or use the included installer. Client behavior varies; verify the installed paths.

## What is included

- **45 skills** with focused triggers, workflows, guardrails, and expected outputs.
- **Three shared rules files** used across the collection.
- A neutral project configuration template; unfilled values are unknown, not defaults.
- Installation and migration guidance.
- A zero-dependency Python validator and unit tests.
- GitHub Actions validation on pull requests and pushes.
- Contribution, security, support, code-of-conduct, changelog, and roadmap documents.

## Skill catalogue

| Skill | What it helps with |
|---|---|
| `accessibility-engineering` | Accessibility audits, semantic UI, keyboard and screen-reader workflows |
| `agricultural-marketplace-planning` | Marketplace roles, inventory, fulfillment, disputes, and settlement |
| `android-extension-engineering` | Android extension/component engineering and compatibility |
| `android-platform-policy-compliance` | Android API, permissions, privacy, and distribution review |
| `authentication-and-session-security` | Authentication, MFA, OTP, session, and authorization security |
| `browser-testing-and-automation` | Reliable browser automation and end-to-end testing |
| `ci-cd-and-release-engineering` | CI pipelines, release artifacts, permissions, deployment, and rollback |
| `client-website-delivery` | Multi-client website delivery and handover |
| `cloud-architecture-and-cost-optimization` | Cloud architecture, reliability, cost, and exit planning |
| `code-review-and-quality` | Correctness, security, maintainability, and release reviews |
| `consent-based-location-sharing` | Consent-based GPS sharing and location privacy |
| `context-builder` | Task-relevant context retrieval under privacy and size limits |
| `contract-first-project-planning` | Scoped plans, acceptance criteria, dependencies, and approvals |
| `data-analysis-and-visualization` | Reproducible data analysis and accurate visualization |
| `dependency-and-supply-chain-security` | Dependency, license, provenance, and build-supply-chain review |
| `digital-service-center-operations` | Customer-facing service workflows, documents, payments, and privacy |
| `documentation-and-architecture-decisions` | Technical documentation, architecture decisions, and runbooks |
| `financial-data-governance` | Financial records, sensitive data, consent, and reconciliation |
| `frontend-ui-engineering` | Consistent design systems, responsive layouts, and frontend architecture |
| `github-delivery` | Safe repository changes, pull requests, CI, and releases |
| `mariadb-database-engineering` | Relational schemas, migrations, queries, and integrity |
| `mcp-and-api-integration` | MCP servers, tool schemas, API integrations, and safe permissions |
| `memory-governance-and-source-control` | Versioned knowledge, decisions, provenance, and source conflicts |
| `observability-and-incident-response` | Logs, metrics, traces, alerts, incidents, and recovery |
| `payment-and-wallet-ledger-workflow` | Payment, wallet, refund, settlement, and ledger integrity |
| `performance-engineering` | Measurement-led latency, throughput, and resource optimization |
| `php-shared-hosting-engineering` | Secure PHP engineering for shared/restricted hosting |
| `privacy-first-browser-tools` | Browser tools with clear storage, network, and privacy behavior |
| `product-discovery-and-validation` | User problem discovery and evidence-led product experiments |
| `qr-code-api-engineering` | QR/barcode APIs, validation, decoding, and resource limits |
| `repository-first-memory` | Using authorized project repositories as canonical context |
| `scoped-memory-governance` | Project-scoped memory, approvals, versions, and privacy boundaries |
| `secure-rest-api-engineering` | Secure REST/JSON contracts, authorization, validation, and abuse controls |
| `security-audit` | Authorized defensive security reviews and evidence-based findings |
| `spec-driven-development` | Approved specifications and observable acceptance criteria |
| `systematic-debugging` | Reproduction, root-cause analysis, narrow fixes, and regression proof |
| `technical-research-and-source-verification` | Current primary-source research and claim-to-source traceability |
| `test-driven-development` | Red-green-refactor implementation and regression testing |
| `universal-skill-creator` | Creating, upgrading, reviewing, and validating portable skills |
| `upi-payment-integrity` | UPI intent/QR integrity and server-side payment verification |
| `website-seo-and-local-search` | Technical SEO, local search, structured data, and evidence-based listings |
| `workflow-automation-and-process-design` | Safe, observable, approval-aware workflow automation |
| `youtube-content-and-trust-safety` | Accurate YouTube content and platform/trust review |

The complete machine-readable catalogue is [CATALOG.json](CATALOG.json). The routing rules are in [SKILL_RULES.md](SKILL_RULES.md).

## Shared rules

Every skill links to these files:

- [GLOBAL_RULES.md](GLOBAL_RULES.md) — truth, evidence, communication, privacy, safety, engineering, and completion claims.
- [SKILL_RULES.md](SKILL_RULES.md) — domain-specific rules and the skill routing matrix.
- [AI_CONTEXT.md](AI_CONTEXT.md) — neutral per-user/per-project settings. Unknown values must remain unconfigured until verified.

Preserve the shared files alongside the skills. Relative links do not guarantee automatic loading in every AI client.

## Mandatory website and web-tool standard

Every website, web app, admin panel, customer portal, browser-based tool, and web UI must be treated as one coherent product:

- One consistent UI/UX design system across the complete tool.
- Reusable common header, footer, navigation, page shell, and shared components.
- Organized, separate CSS and JavaScript assets/modules.
- Clear frontend/backend boundary; secrets and trusted business logic remain server-side.
- Fully responsive mobile, tablet, laptop, and desktop layouts.
- Sensitive files and data—including environment files, credentials, private keys, logs, backups, private uploads, and customer data—outside the actual document root wherever the host permits.
- Shared server-side code outside the public document root where possible.
- Direct URL tests for sensitive paths before claiming that they are protected.

See [SKILL_RULES.md §1](SKILL_RULES.md) for the full standard.

## Quality and validation

Run the validator and tests before submitting a change:

```bash
python3 scripts/validate_skills.py
python3 -m unittest discover -s tests -v
```

The validator checks names, frontmatter limits, unique skill folders, shared-file links, local links, catalogue consistency, routing-matrix coverage, and known private-data/secret patterns. It is a static safety net, not a full YAML parser, security audit, or runtime test.

## Portability and limitations

Skills are instruction packages, not executable programs or permission grants. Tool access, activation, references, and UI differ by AI client. A skill may need client-specific installation or explicit file loading. Runtime compatibility and real behavior must be tested in the target environment.

## Research basis

The collection's structure and quality practices were informed by public documentation and examples from the Agent Skills specification and well-known skill collections, including [agentskills/agentskills](https://github.com/agentskills/agentskills), [anthropics/skills](https://github.com/anthropics/skills), [obra/superpowers](https://github.com/obra/superpowers), [mattpocock/skills](https://github.com/mattpocock/skills), [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills), [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills), and [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill).

These are independent projects. This library does not claim affiliation or endorsement. Their skill files were not copied into this repository; the references were used to study public structure, workflow, testing, and quality practices.

## Licensing

- Skill files and documentation: **CC BY 4.0**. Attribution and change-notice conditions apply.
- Scripts, tests, and workflow code: **MIT**.
- See [LICENSE](LICENSE), [LICENSE-CODE](LICENSE-CODE), and [LICENSE-CONTENT.md](LICENSE-CONTENT.md) for exact scope. Check third-party asset licenses separately.

## Contributing

Contributions are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md), [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md), and [SECURITY.md](SECURITY.md) before opening a pull request.

## Project status

Version 4.0.0 has been merged into `main`. The repository changes are merged and CI validation passed; a version tag/GitHub release and cross-client runtime certification are separate steps and have not been claimed. Static validation is automated. Cross-platform runtime activation is not claimed unless explicitly tested and documented.

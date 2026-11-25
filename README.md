# Universal AI Agent Skills Library v2.2.0

A portable library of **31 reusable, general-purpose AI agent skills** for individuals, developers, teams, and organizations. The library includes software engineering, security, project planning, data governance, content, and workflow skills.

## What is included

- 31 self-contained skill folders, each with a `SKILL.md` and YAML frontmatter.
- `GLOBAL_RULES.md` — cross-skill truth, evidence, communication, privacy, safety, engineering, and action rules.
- `SKILL_RULES.md` — domain-specific requirements, including the mandatory unified website UI/UX and security architecture.
- `PROJECT_CONFIG.md` — neutral configuration template. Empty or `VERIFY` values are unknown, not defaults.
- `CATALOG.json`, `CHANGELOG.md`, `MIGRATION.md`, and `VALIDATION_REPORT.md`.

## Skill index

| Skill | Purpose |
|---|---|
| `memory-governance-and-source-control` | Organize project knowledge, memories, documents, decisions, and source conflicts for individuals or teams. Use when an AI agent must retrieve, update, verify, or hand over project context. |
| `php-shared-hosting-engineering` | Build, audit, secure, and optimize PHP applications on shared or restricted hosting without assuming root access or a specific hosting provider. |
| `secure-rest-api-engineering` | Design, implement, test, and review secure REST/JSON APIs with clear contracts, authentication, authorization, abuse controls, and reliable error handling. |
| `mariadb-database-engineering` | Design, inspect, migrate, optimize, and validate MariaDB/MySQL schemas, queries, transactions, and data workflows. |
| `payment-and-wallet-ledger-workflow` | Design and review payment, wallet, refund, cashback, settlement, and ledger workflows with reliable evidence and reconciliation. |
| `authentication-and-session-security` | Design, implement, and audit account authentication, MFA, OTP, recovery, sessions, device trust, and authorization. |
| `qr-code-api-engineering` | Build, maintain, and secure QR/barcode generation and decoding APIs with format validation, resource limits, and backward compatibility. |
| `consent-based-location-sharing` | Design and secure user-consented location sharing, GPS ingestion, session controls, map display, and location-data retention. |
| `android-extension-engineering` | Build, audit, upgrade, and maintain Android extensions/components for supported builders such as Niotron or App Inventor. |
| `android-platform-policy-compliance` | Review Android platform behavior, API compatibility, permissions, privacy, background limits, and app-store distribution requirements. |
| `financial-data-governance` | Govern financial records, credit data, statements, calculations, account matching, AI access, and consent across personal or business finance systems. |
| `website-seo-and-local-search` | Improve websites, technical SEO, local search presence, structured data, accessibility, and business listings using accurate evidence. |
| `youtube-content-and-trust-safety` | Create and audit YouTube scripts, titles, descriptions, thumbnails, tags, and educational content with factual accuracy and platform-policy awareness. |
| `privacy-first-browser-tools` | Design browser-based tools that minimize data collection, protect files and user input, and clearly disclose network and storage behavior. |
| `upi-payment-integrity` | Design and review India UPI intent/QR payment journeys with secure server-side verification, idempotency, and dispute reconciliation. |
| `mcp-and-api-integration` | Design and integrate APIs with Model Context Protocol (MCP) servers, tools, resources, and AI clients using least privilege and safe action approval. |
| `client-website-delivery` | Plan, build, audit, and hand over websites for multiple clients while protecting identity, data separation, approvals, and deployment integrity. |
| `digital-service-center-operations` | Improve customer-facing digital service centers through accurate SOPs, document handling, queue management, printing, payments, and privacy controls. |
| `agricultural-marketplace-planning` | Plan digital marketplaces that connect farmers, food producers, buyers, logistics providers, and service partners with clear roles and transaction controls. |
| `contract-first-project-planning` | Convert complex requests into scoped, testable plans with dependencies, acceptance criteria, risks, and verified completion status. |
| `universal-skill-creator` | Create, review, improve, validate, and package portable AI Agent Skills for individuals, teams, and organizations. Use when a workflow must become a reusable SKILL.md or an existing skill needs upgrading. |
| `context-builder` | Retrieve only task-relevant project context under a defined context and privacy budget. |
| `github-delivery` | Prepare safe Git commits, pull requests, repository documentation, CI, releases, and deployment workflows. |
| `memory-governance` | Govern durable AI memory creation, review, approval, versioning, expiry, retrieval, and deletion. |
| `php-shared-hosting` | Design, audit, secure, and deploy PHP applications on shared or restricted hosting. |
| `project-planning` | Plan products and technical work in phases with scope, evidence, risk controls, and measurable acceptance criteria. |
| `project-reverse-engineering` | Understand and safely improve existing software systems before changing or replacing them. |
| `repository-first-memory` | Use authorized project repositories as canonical context without leaking data across project scopes. |
| `secure-rest-api` | Design secure REST APIs with authentication, authorization, validation, abuse controls, and safe operations. |
| `scoped-memory-governance` | Curate durable project memory with explicit scope, provenance, approval, versions, and privacy boundaries. |
| `security-audit` | Audit explicitly authorized software and deployments using evidence-based defensive security methods. |

## Mandatory shared files

Every skill explicitly links to all three shared files. Before using a skill, load `GLOBAL_RULES.md`, the relevant `SKILL_RULES.md` sections, and the active project's confirmed `PROJECT_CONFIG.md`. Preserve the package directory structure. Some agent clients do not follow Markdown links automatically; configure explicit loading or copy the shared files into a supported references location.

## Website and web-application standard

For every website, web app, admin panel, or browser tool, apply `SKILL_RULES.md` §1: one consistent UI/UX design system across the complete product; reusable common header, footer, navigation, and components; organized separate CSS and JavaScript; clear frontend/backend separation; full responsive behavior; and sensitive configuration, credentials, logs, backups, and private data outside the actual web document root wherever the host allows. Verify the real document root and test direct URL access before claiming files are protected.

## Portability and limitations

Each skill is instruction content, not an executable program. Skill discovery paths, tool availability, and references behavior vary by AI client. A skill does not grant permissions, install tools, train a model, or guarantee identical behavior across providers.

## License status

No license is included. Public visibility does not automatically grant permission to reuse, modify, or redistribute this content. A license should be added only after the rights holder selects one.

## Validation

Static checks cover all skill names, frontmatter, shared-file links, catalog paths, package layout, and known private identifiers. Runtime behavior must still be tested in each target AI platform. See `VALIDATION_REPORT.md` for exact scope and limitations.

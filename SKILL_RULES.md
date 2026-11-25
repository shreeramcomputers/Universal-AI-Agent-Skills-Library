# Shared Domain Rules for All Skills

**Version:** 2.2.0  
**Scope:** Domain-specific rules used by the 31 skills in this library. Read the relevant section(s) before acting. These rules complement `GLOBAL_RULES.md` and never replace higher-priority requirements.

## 1. Universal website and web-application rules

These requirements apply whenever a skill creates, modifies, audits, or deploys a website, web application, admin panel, customer portal, browser-based tool, or web UI. The directly responsible skills include `client-website-delivery`, `php-shared-hosting-engineering`, `website-seo-and-local-search`, `privacy-first-browser-tools`, `authentication-and-session-security`, `secure-rest-api-engineering`, `php-shared-hosting`, and `secure-rest-api`. Other skills must apply the parts that touch their work.

### 1.1 One coherent UI/UX across the complete web product

- Treat the website/web application as one product, not a set of unrelated pages. Define and reuse one design system: typography, spacing, colors, surfaces, icons, buttons, form controls, tables, alerts, navigation, loading states, empty states, and error states.
- Keep header, footer, navigation, sidebar, breadcrumbs, page shells, dialogs, and shared controls consistent across all applicable pages and modules. Admin, customer, and public areas may have different navigation or access, but must still follow the same design system and interaction rules.
- Apply the same design language to every relevant screen in the complete web tool, including login, registration, dashboard, settings, reports, forms, search, detail pages, and responsive/mobile views.
- Build shared/reusable components or include files for common UI and layout. Avoid copy-pasting the same header, footer, menu, validation, or component markup across many pages.
- Keep CSS and JavaScript organized as separate, maintainable assets/modules instead of scattering repeated inline code. Use bundling/minification where useful, but preserve source separation and clear ownership. Never put secrets or server-only logic in browser JavaScript.
- Maintain a clear frontend/backend boundary. The browser handles presentation and interaction; trusted business rules, authorization, secrets, payment verification, and sensitive data operations remain server-side.
- The complete product must be responsive on supported mobile, tablet, laptop, and desktop sizes. Check real content, tables, menus, forms, modals, keyboard use, zoom, touch targets, and overflow—not only the landing page.
- Use semantic HTML, accessible labels, visible focus, keyboard operation, sufficient contrast, and understandable validation/errors. Do not sacrifice accessibility for visual similarity.
- Shared components may accept controlled variants where user role or task requires them. Consistency does not mean forcing an identical layout where it would harm usability or accessibility.

### 1.2 Common code and file architecture

- Identify repeated logic and create appropriate shared modules for layout, navigation, footer, UI components, validation, authentication helpers, database access, API clients, configuration loading, logging, and domain utilities.
- Keep shared business logic in one maintained source of truth. Avoid multiple slightly different implementations of the same rule.
- Separate public assets, server-side code, configuration, storage, and deployment artifacts. Use a clear directory map and document entry points and dependencies.
- Do not expose internal include paths, source maps containing secrets, development files, backups, SQL dumps, logs, or environment files through the web server.
- Common/reusable does not mean public: shared server-side modules belong outside the public document root where possible and should be loaded by trusted server-side code.

### 1.3 Sensitive files and data outside the public document root

- First identify the actual web document root. It is often named `public_html`, `www`, `htdocs`, or `public`, but the name must be verified.
- Store `.env`, database credentials, API keys, private keys, signing secrets, session secrets, private configuration, application logs, backups, database dumps, private uploads, and sensitive customer files **outside the actual document root** wherever the hosting environment allows.
- Keep only intentionally public resources inside the document root: public entry points, public CSS/JS/images/fonts, and files that are safe for anyone to request.
- Browser code, HTML, CSS, source maps, public JSON, and downloadable assets must be treated as public. Never place API secrets, private tokens, internal credentials, or privileged business rules there.
- Load private configuration through server-side code using paths derived from a trusted application root. Do not construct include paths from untrusted request input.
- Apply least-privilege filesystem permissions. Do not rely on obscure filenames, hidden folders, or a deny rule as the primary protection for secrets.
- If a hosting provider makes storage outside the document root impossible, use a provider-supported private storage area or server-level deny rules, disable directory listing, test direct HTTP access to every sensitive path, and document the residual risk. Treat this as a fallback, not equivalent to keeping files outside the document root.
- Never claim a file is private until direct URL access and relevant server routes have been tested.

### 1.4 Web delivery gates

Before release, check: shared design consistency; responsive behavior on supported breakpoints; accessibility basics; frontend/backend separation; authorization on the server; no secrets in public assets; sensitive files outside document root; secure headers/cookies/CSRF where relevant; input/output validation; error and empty states; performance; browser console/network errors; backup and rollback; and owner approval.

## 2. Software architecture and API rules

Applies especially to `secure-rest-api-engineering`, `mcp-and-api-integration`, `qr-code-api-engineering`, `php-shared-hosting-engineering`, `php-shared-hosting`, and `authentication-and-session-security`.

- Define request/response contracts, data ownership, trust boundaries, authorization rules, error models, idempotency, rate limits, and versioning before implementation.
- Enforce access control server-side on every resource/action. Never trust client-supplied role, owner ID, amount, balance, permission, or transaction status.
- Keep credentials and private configuration out of source control, public responses, URLs, client bundles, and logs.
- Bound input sizes, execution, file dimensions, pagination, recursion, concurrency, and external request fan-out.
- Use safe timeouts, TLS verification, replay protection, idempotency, and structured error handling where appropriate.
- Test unauthorized, malformed, duplicate, replayed, concurrent, cross-user/tenant, and degraded-service cases.

## 3. Data, database, and migration rules

Applies especially to `mariadb-database-engineering`, `memory-governance-and-source-control`, `memory-governance`, `scoped-memory-governance`, `financial-data-governance`, `payment-and-wallet-ledger-workflow`, and `digital-service-center-operations`.

- Inspect the real schema, constraints, current data, indexes, encoding, engine, transaction behavior, and backup/restore path before migration.
- Prefer constraints and transactions to fragile application-only assumptions. Make migrations repeatable where practical and provide rollback or forward-recovery steps.
- Do not overwrite, fabricate, or seed production data without explicit approval. Test with a safe copy or synthetic data.
- Apply least privilege, tenant separation, data minimization, auditability, retention, and deletion rules.
- Treat financial and identity records as high sensitivity; reconcile totals and preserve an auditable source trail.

## 4. Authentication, payments, and financial safety

Applies especially to `authentication-and-session-security`, `upi-payment-integrity`, `payment-and-wallet-ledger-workflow`, and `financial-data-governance`.

- Authentication does not replace authorization. Enforce permissions on the server for every sensitive action.
- Credentials, OTPs, recovery secrets, tokens, and signing keys must be protected, short-lived where applicable, and excluded from logs.
- A payment intent, QR scan, client callback, screenshot, or user claim is not proof of settlement. Verify transaction status through a trusted authoritative source before crediting value or marking a bill paid.
- Use idempotency, immutable ledger entries, reconciliation, explicit reversal/refund handling, and audit events for money movement.
- Never invent rates, charges, eligibility, balances, approvals, or financial outcomes.

## 5. Android and device-platform rules

Applies especially to `android-extension-engineering` and `android-platform-policy-compliance`.

- Verify current Android API/SDK behavior, target and minimum SDK, extension builder/compiler support, permission policy, privacy requirements, and distribution rules from official documentation.
- Do not add permissions, background activity, accessibility access, notification access, package visibility, or data collection without a documented need and owner/user approval.
- Separate source review, compilation, emulator/device runtime testing, and store-policy review; report each status independently.

## 6. Privacy, consent, and user data

Applies especially to `consent-based-location-sharing`, `privacy-first-browser-tools`, `financial-data-governance`, `digital-service-center-operations`, and `client-website-delivery`.

- Collect only the data necessary for the disclosed purpose. Obtain meaningful consent before sensitive collection or sharing.
- Make data flows, recipients, retention, storage, deletion, and third-party transfers clear.
- Apply access control, encryption in transit and at rest when available, retention limits, deletion handling, and safe error/logging practices.
- Location, financial, identity, customer, and document data must not be exposed in public URLs, analytics, or unnecessary logs.

## 7. Business, content, and service rules

Applies especially to `agricultural-marketplace-planning`, `digital-service-center-operations`, `website-seo-and-local-search`, and `youtube-content-and-trust-safety`.

- Do not fabricate service availability, business details, reviews, testimonials, prices, qualifications, delivery promises, legal status, or government affiliation.
- Distinguish a service provider from an intermediary, referral, application assistant, or independent decision-maker.
- Verify facts before publishing; clearly separate allegation, suspicion, evidence, and opinion.
- Respect copyright, privacy, platform rules, and consent for images, audio, text, and personal data.

## 8. Planning, memory, and skill-authoring rules

Applies especially to `contract-first-project-planning`, `project-planning`, `project-reverse-engineering`, `repository-first-memory`, `context-builder`, `memory-governance`, `scoped-memory-governance`, `github-delivery`, `security-audit`, and `universal-skill-creator`.

- Capture requirements, constraints, owner decisions, assumptions, dependencies, acceptance criteria, risks, and unresolved questions separately.
- Preserve provenance, timestamps, superseded decisions, and source conflicts. Do not silently turn old memory into current truth.
- Do not make one person's private settings universal. Use a configurable project profile and require confirmation for consequential values.
- When creating/upgrading a skill, read this whole library's shared rules, add dependency links to all three shared files, update catalog/docs, and validate link targets and package integrity.

## 9. Skill-to-rule routing matrix

Every skill must load `GLOBAL_RULES.md` and its active project's confirmed `PROJECT_CONFIG.md`. Apply these `SKILL_RULES.md` sections as follows:

| Skill | Required sections |
|---|---|
| `agricultural-marketplace-planning` | 3, 4, 6, 7, 8 |
| `android-extension-engineering` | 5, 6 |
| `android-platform-policy-compliance` | 5, 6 |
| `authentication-and-session-security` | 1, 2, 4, 6 |
| `client-website-delivery` | 1, 2, 3, 4, 6, 7 |
| `consent-based-location-sharing` | 4, 6 |
| `contract-first-project-planning` | 8 |
| `digital-service-center-operations` | 1, 3, 4, 6, 7 |
| `financial-data-governance` | 3, 4, 6 |
| `mariadb-database-engineering` | 1, 2, 3, 6 |
| `mcp-and-api-integration` | 1, 2, 6, 8 |
| `memory-governance-and-source-control` | 3, 8 |
| `payment-and-wallet-ledger-workflow` | 3, 4, 6 |
| `php-shared-hosting-engineering` | 1, 2, 3, 4, 6 |
| `privacy-first-browser-tools` | 1, 2, 6 |
| `qr-code-api-engineering` | 1, 2, 4 |
| `secure-rest-api-engineering` | 1, 2, 4, 6 |
| `universal-skill-creator` | 1, 2, 5, 6, 8 |
| `upi-payment-integrity` | 2, 3, 4, 6 |
| `website-seo-and-local-search` | 1, 6, 7 |
| `youtube-content-and-trust-safety` | 6, 7 |
| `context-builder` | 3, 6, 8, 10 |
| `github-delivery` | 1, 2, 6, 8, 10 |
| `memory-governance` | 3, 6, 8, 10 |
| `php-shared-hosting` | 1, 2, 3, 6, 10 |
| `project-planning` | 1, 2, 6, 8, 10 |
| `project-reverse-engineering` | 1, 2, 3, 6, 8, 10 |
| `repository-first-memory` | 3, 6, 8, 10 |
| `secure-rest-api` | 1, 2, 4, 6, 10 |
| `scoped-memory-governance` | 3, 6, 8, 10 |
| `security-audit` | 1, 2, 3, 5, 6, 10 |

## 10. Conflict handling

- Apply the narrowest applicable rule that is consistent with higher-priority requirements and the active user's confirmed instructions.
- A project config is descriptive input, not permission to take an action. Approval gates still apply.
- If a global rule, domain rule, and project setting conflict, do not silently choose a risky interpretation. Explain the conflict and use the safer valid option until clarified.

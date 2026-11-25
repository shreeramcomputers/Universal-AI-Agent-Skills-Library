---
name: payment-and-wallet-ledger-workflow
description: Design and review payment, wallet, refund, cashback, settlement, and ledger workflows with reliable evidence and reconciliation.
---

## Mandatory shared rules

Before using this skill, read these bundle-level files from the package root:

- [`../../GLOBAL_RULES.md`](../../GLOBAL_RULES.md) — truth, evidence, privacy, security, approvals, and completion claims.
- [`../../SKILL_RULES.md`](../../SKILL_RULES.md) — apply the domain sections mapped to this skill in the routing matrix.
- [`../../PROJECT_CONFIG.md`](../../PROJECT_CONFIG.md) — use only settings that are filled in and confirmed for the active project; blank or `VERIFY` fields are unknown.

If any shared file is unavailable, do not invent its contents. Apply the safety rules in this skill, mark project-specific assumptions as unknown, and report the missing dependency. Some AI clients do not automatically follow relative links; configure explicit loading when required.

# Payment and Wallet Ledger Workflow

## Runtime context and currentness protocol

1. At the start of each activation, obtain the current date/time from a trusted runtime clock or explicit time tool when available. Record an ISO-8601 timestamp and timezone in formal reports or whenever timing affects the answer. Never invent a time. If no reliable clock is exposed, say `CURRENT TIME NOT VERIFIED`.
2. A timestamp is only the time the task began; it does not prove that a fact is current. Identify which claims can change and verify only those that materially affect the task.
3. For relevant laws, regulations, deadlines, official fees, security advisories, standards, software/runtime versions, APIs, SDKs, protocols, platform rules, product capabilities, pricing, provider limits, and compatibility, check current primary sources. Prefer government/regulator, standards-body, vendor, official documentation, release-note, and official repository sources.
4. Open the source itself where possible. Check jurisdiction, product, version, publication/update date, effective/commencement date, support status, and access/check date. Do not trust search snippets alone.
5. Record source URL and the exact claim/version/provision it supports when the task is consequential. Distinguish publication date, effective date, release date, and date checked.
6. Label material facts as `VERIFIED`, `UNVERIFIED`, `ASSUMPTION`, `ESTIMATE`, or `USER/OWNER-APPROVED`. If live research is unavailable, do not describe the claim as latest or current; state the limitation.
7. Prefer supported, security-patched, compatible stable releases over a version chosen only because its number is newest. Test compatibility before changing production systems.
8. Do not browse unnecessarily for purely creative work, stable concepts, or tasks whose answer is fully supported by supplied source material and does not depend on current external facts.

## Portable use and configuration

- This skill is not bound to any one person, company, project, repository, domain, server, country, or software vendor unless the user explicitly selects that scope.
- First identify the active user, organization, project, jurisdiction, environment, and source of truth. Reuse supplied context only when it clearly belongs to that scope.
- Treat examples, previous conversations, memory, templates, and demo values as references—not approvals or live configuration.
- If a decision materially changes cost, security, privacy, legal exposure, data, or production behavior, explain the options and obtain the required approval before acting.
- Never assume a tool, connector, account, permission, filesystem, network, clock, or execution environment exists. Check capability and authorization before relying on it.


## Shared library rules and project configuration

This skill is part of the Universal AI Agent Skills Library. Before acting, read the bundle-level files and apply the relevant rules:

- [`../../GLOBAL_RULES.md`](../../GLOBAL_RULES.md) — mandatory truth, evidence, communication, safety, privacy, engineering, and completion rules.
- [`../../SKILL_RULES.md`](../../SKILL_RULES.md) — mandatory domain rules; use the routing matrix to identify the sections relevant to this skill.
- [`../../PROJECT_CONFIG.md`](../../PROJECT_CONFIG.md) — project configuration template; use only fields confirmed for the active user/project. Blank values are unknown, not defaults.

Preserve the full library folder layout so these relative references resolve. Not every AI client automatically loads linked files; when the client supports progressive references, explicitly open these files before execution. If they are unavailable, do not invent their contents or project settings.

## Use when

- Building payment collection, stored-value wallets, credits/debits, refunds, commissions, cashback, or settlement processes.
- Auditing financial state transitions, duplicate payments, race conditions, or reconciliation gaps.

## Workflow

1. Identify the jurisdiction, regulated activity, payment rails, provider/acquirer/PSP, account model, custody of funds, user roles, and legal entity.
2. Retrieve the latest approved business rules and provider contract. Treat old product briefs and example amounts as provisional.
3. Map the end-to-end payment lifecycle: initiation, pending, authorization, capture/settlement, success, failure, reversal, refund, dispute, expiry, and reconciliation.
4. Define a server-authoritative state machine and evidence required for each state transition.
5. Design an append-only ledger with unique transaction references, idempotency, atomic balance updates, concurrency protection, and linked reversal entries.
6. Define operator/admin permissions, approval separation, limits, fee/cashback calculations, customer notices, and audit events.
7. Test duplicate callbacks, retries, late events, concurrent requests, partial failures, reversals, chargebacks, and reconciliation mismatches.
8. Verify live provider and regulator requirements before launch or a material design change.

## Non-negotiable controls

- A client redirect, app callback, screenshot, SMS, UI success flag, or customer statement is not settlement proof.
- Credit a wallet or mark a payment settled only after trusted server-side verification from the approved provider, bank/PSP evidence, signed webhook, or other authorized settlement source.
- Never trust client-supplied amount, beneficiary, user, wallet, fee, payment status, or transaction identifier without server validation.
- Enforce idempotency and exactly-once ledger effects even when events are delivered more than once.
- Keep transaction history immutable. Correct errors with linked compensating/reversal entries rather than deleting or rewriting history.
- Separate customer funds, platform revenue, fees, commissions, cashback, and accounting balances.
- Make refund eligibility, funding source, approval roles, timing, and disclosures explicit. Do not assume all top-ups or transfers are refundable/non-refundable.
- Obtain qualified legal/compliance review for regulated payment, lending, deposit-taking, stored value, or custody activities.

## Output

Provide sequence/state diagrams, role matrix, ledger model, evidence gates, reconciliation plan, failure/refund cases, security risks, source list, and launch blockers.

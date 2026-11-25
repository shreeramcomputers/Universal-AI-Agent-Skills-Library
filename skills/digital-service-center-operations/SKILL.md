---
name: digital-service-center-operations
description: Improve customer-facing digital service centers through accurate SOPs, document handling, queue management, printing, payments, and privacy controls.
---

## Mandatory shared rules

Before using this skill, read these bundle-level files from the package root:

- [`../../GLOBAL_RULES.md`](../../GLOBAL_RULES.md) — truth, evidence, privacy, security, approvals, and completion claims.
- [`../../SKILL_RULES.md`](../../SKILL_RULES.md) — apply the domain sections mapped to this skill in the routing matrix.
- [`../../PROJECT_CONFIG.md`](../../PROJECT_CONFIG.md) — use only settings that are filled in and confirmed for the active project; blank or `VERIFY` fields are unknown.

If any shared file is unavailable, do not invent its contents. Apply the safety rules in this skill, mark project-specific assumptions as unknown, and report the missing dependency. Some AI clients do not automatically follow relative links; configure explicit loading when required.

# Digital Service Center Operations

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

- Operating or improving a walk-in digital service, document assistance, print/copy, form-filling, booking, or citizen-support center.
- Creating staff SOPs, customer checklists, fee clarity, process controls, or service-quality measures.

## Workflow

1. Identify country/state, business model, services offered, provider relationships, authorization status, staff roles, and customer types.
2. Verify current official portal links, forms, fees, eligibility, deadlines, biometric/identity rules, banking requirements, and provider agreements.
3. Map customer journey from enquiry to document intake, form completion, payment, submission, receipt, status tracking, and complaint handling.
4. Define a per-service checklist with required documents, official fee, center/service charge, expected steps, risks, and what the center cannot guarantee.
5. Create privacy-safe desk, screen, printout, scan, email, and file-handling procedures.
6. Create queue, rework, escalation, cash/reconciliation, receipt, and daily closing controls.
7. Train staff and review service accuracy, wait time, complaints, errors, data incidents, and customer understanding.

## Rules

- Clearly distinguish private assistance from government or provider authority. Never imply official affiliation without current proof.
- Separate official/portal fees from service charges and provide a transparent receipt.
- Never promise approval, eligibility, or delivery time controlled by an external authority.
- Do not ask customers to reveal OTPs/passwords unnecessarily. Never store them for reuse.
- Collect only necessary documents, protect copies and printouts, and securely delete temporary files.
- For banking, identity, insurance, lending, travel, or other regulated services, verify current authorization, limits, dispute rules, and staff training requirements.
- Use accessible, simple language and provide customers a chance to review important form data before submission.

## Output

Provide SOPs, customer/staff checklists, fee/receipt controls, privacy rules, escalation paths, and measurable quality indicators.

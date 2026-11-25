---
name: contract-first-project-planning
description: Convert complex requests into scoped, testable plans with dependencies, acceptance criteria, risks, and verified completion status.
---

## Mandatory shared rules

Before using this skill, read these bundle-level files from the package root:

- [`../../GLOBAL_RULES.md`](../../GLOBAL_RULES.md) — truth, evidence, privacy, security, approvals, and completion claims.
- [`../../SKILL_RULES.md`](../../SKILL_RULES.md) — apply the domain sections mapped to this skill in the routing matrix.
- [`../../PROJECT_CONFIG.md`](../../PROJECT_CONFIG.md) — use only settings that are filled in and confirmed for the active project; blank or `VERIFY` fields are unknown.

If any shared file is unavailable, do not invent its contents. Apply the safety rules in this skill, mark project-specific assumptions as unknown, and report the missing dependency. Some AI clients do not automatically follow relative links; configure explicit loading when required.

# Contract-First Project Planning

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

- Planning software, business, research, migration, content, or operational work with multiple dependencies.
- Turning a vague request into an ordered delivery plan or implementation prompt.

## Workflow

1. Restate the desired outcome, users, scope, constraints, deadline, budget, and success measures.
2. Inspect available project files and current state before drafting work. Distinguish existing capability from proposed capability.
3. Break the outcome into small tasks with a single clear result each.
4. For each task define: purpose, inputs, outputs, dependencies, inclusions, exclusions, owner/approver, acceptance criteria, tests, rollback, and evidence.
5. Order work by dependency, risk, and value. Identify critical path, blockers, and parallelizable tasks.
6. Separate discovery, design, implementation, verification, release, and handover.
7. Assign status using `PASS`, `FAIL`, `BLOCKED`, `NOT RUN`, or `UNVERIFIED`; never infer completion from a plan.
8. Update the plan when scope changes, recording what changed and why.

## Rules

- Do not silently expand scope or treat a suggestion as approved work.
- Do not create duplicate tasks where an existing task already covers the requirement.
- State what the task does not include to prevent ambiguity.
- Make acceptance criteria observable and testable, not subjective phrases such as “works perfectly.”
- A prompt, plan, generated code, or successful syntax check is not proof of end-to-end completion.
- Require explicit approval before destructive actions, production releases, spending, public communication, or changes to access.
- Keep one logical phase or implementation unit in focus when sequencing work for incremental review.

## Output

Provide objective, assumptions, scope/exclusions, task sequence, dependencies, acceptance tests, risk register, approvals, and status/evidence table.

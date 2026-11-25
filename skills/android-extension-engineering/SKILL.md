---
name: android-extension-engineering
description: Build, audit, upgrade, and maintain Android extensions/components for supported builders such as Niotron or App Inventor.
---

## Mandatory shared rules

Before using this skill, read these bundle-level files from the package root:

- [`../../GLOBAL_RULES.md`](../../GLOBAL_RULES.md) — truth, evidence, privacy, security, approvals, and completion claims.
- [`../../SKILL_RULES.md`](../../SKILL_RULES.md) — apply the domain sections mapped to this skill in the routing matrix.
- [`../../PROJECT_CONFIG.md`](../../PROJECT_CONFIG.md) — use only settings that are filled in and confirmed for the active project; blank or `VERIFY` fields are unknown.

If any shared file is unavailable, do not invent its contents. Apply the safety rules in this skill, mark project-specific assumptions as unknown, and report the missing dependency. Some AI clients do not automatically follow relative links; configure explicit loading when required.

# Android Extension Engineering

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

- Creating or patching Java/Kotlin extensions or reusable components for an Android app builder.
- Maintaining public blocks, methods, events, metadata, permissions, or extension compatibility.

## Workflow

1. Identify the exact builder, extension processor, source language, compiler/runtime, Android SDK, min/target SDK, distribution method, and supported device API range.
2. Inspect the complete current source and build configuration. Compare source by content or hash; filenames and suffixes do not prove which source is newer.
3. Verify current builder documentation, compiler support, Android API behavior, and distribution requirements.
4. Map public component blocks, method signatures, events, parameters, metadata, permissions, lifecycle, threads, and callbacks.
5. Design a minimal patch and document changed behavior before editing.
6. Compile with the actual target toolchain where available. Test runtime behavior on representative OS/API levels and existing projects.
7. Review permissions, exported components, storage, package visibility, notifications, background execution, WebView, IPC, cryptography, and privacy.
8. Produce source, build artifact only if actually generated, regression evidence, and release notes.

## Rules

- Preserve public APIs and existing behavior unless an approved change requires otherwise.
- Use a language/compiler level only when the target builder supports it; do not assume Java 11 or another version.
- Distinguish source-level inspection, successful compilation, device runtime testing, and store-policy compliance.
- Never claim a build passed from static inspection alone.
- Do not silently add permissions or background behavior; explain user impact and policy risks.
- Avoid reflection or hidden APIs unless specifically justified, supported, and policy-compliant.

## Output

Provide compatibility matrix, exact patch summary, full source, actual build/test status, regression cases, permission impact, and release notes.

---
name: consent-based-location-sharing
description: Design and secure user-consented location sharing, GPS ingestion, session controls, map display, and location-data retention.
---

## Mandatory shared rules

Before using this skill, read these bundle-level files from the package root:

- [`../../GLOBAL_RULES.md`](../../GLOBAL_RULES.md) — truth, evidence, privacy, security, approvals, and completion claims.
- [`../../SKILL_RULES.md`](../../SKILL_RULES.md) — apply the domain sections mapped to this skill in the routing matrix.
- [`../../PROJECT_CONFIG.md`](../../PROJECT_CONFIG.md) — use only settings that are filled in and confirmed for the active project; blank or `VERIFY` fields are unknown.

If any shared file is unavailable, do not invent its contents. Apply the safety rules in this skill, mark project-specific assumptions as unknown, and report the missing dependency. Some AI clients do not automatically follow relative links; configure explicit loading when required.

# Consent-Based Location Sharing and GPS Security

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

- Building opt-in live location sharing, fleet/field tracking with appropriate notice, safety check-ins, or location history features.
- Auditing GPS permission, sharing sessions, storage, or map-provider integration.

## Do not use when

- The request is to secretly track a person, bypass device permissions, hide collection, or continue location collection after consent is withdrawn. Refuse those parts and offer transparent, opt-in alternatives.

## Workflow

1. Identify the person sharing location, legitimate purpose, recipients, jurisdiction, device/browser, precision, frequency, duration, retention, and deletion rights.
2. Design an explicit consent screen that explains purpose, who can view location, duration, collection frequency, retention, and how to stop sharing.
3. Request OS/browser permission only when needed. Permission does not replace server authorization or informed consent.
4. Use authenticated, scoped, expiring sessions. Authorize create/read/update/stop/delete operations on the server.
5. Validate coordinate ranges, timestamps, accuracy, payload size, sample rate, and session ownership.
6. Store precise location data in access-controlled storage with retention and deletion rules; minimize it in logs and analytics.
7. Make stop-sharing effective immediately for future collection. Explain separately the effect on previously collected points.
8. Check map/tile provider terms, privacy, caching, attribution, quotas, and uptime commitments.
9. Test consent denied/granted, stop sharing, expired/replayed tokens, cross-session access, malformed GPS, rate limits, retention, and device lifecycle behavior.

## Rules

- Never implement covert, hidden, or non-consensual location collection.
- Do not collect more frequently or retain longer than the stated purpose requires.
- Avoid exposing precise coordinates, tracker tokens, or identifying location trails in public URLs and logs.
- Provide a visible status and stop control throughout active sharing.
- Defend against replay, IDOR, token theft, session fixation, and unauthorized recipient changes.

## Output

Provide consent UX, data-flow map, access-control model, retention/deletion policy, provider terms, test evidence, and unresolved privacy risks.

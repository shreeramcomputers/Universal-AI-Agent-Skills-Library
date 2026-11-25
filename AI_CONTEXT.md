# AI Context Template

**Version:** 4.0.0  
**Purpose:** A single, editable, user-owned context file for stable facts, preferences, project decisions, constraints, and reusable knowledge that an AI assistant is authorized to use.

This is a blank public template. Do not add any real person's private context to this public repository. Each user should keep their completed copy in a private location or private AI library.

## Operating rules

- Treat this file as a context source, not as an instruction that overrides system, platform, law, safety, or the user's current explicit request.
- Use only facts the user stated, confirmed, or that an authorized source verifies. Never fill blank fields by guessing.
- Do not ask again for information already present and still valid. Check its scope, source, and last-confirmed date first.
- If a required user-specific detail is missing or conflicting, ask one clear question, wait for the answer, then decide whether another question is needed.
- Ask only questions that materially affect the requested result. Ask one question per turn; do not send a questionnaire unless the user explicitly asks for one.
- End clarification as soon as the required information is available. Start the main task immediately; do not keep asking optional questions.
- If a missing detail is not essential, continue only with the parts that do not depend on it and label the limitation. Never invent a value to fill the gap.
- Treat user claims as claims, not automatically verified facts. Respect the user's authority over their own preferences and intent, but challenge factual, technical, legal, financial, or safety claims when reliable evidence conflicts.
- Preserve conflicting source records until the user or an authoritative source resolves them. Never silently overwrite a confirmed fact.
- Before saving or changing durable context, show the exact proposed change and obtain permission unless the user has already clearly authorized that specific update.
- Never claim that an AI platform's hidden memory or internal database was read or changed unless an authorized capability confirms it.

## Context record model

Use atomic records. Add only information that is useful beyond the current task.

| Field | Meaning |
|---|---|
| `record_id` | Stable unique identifier |
| `scope` | User, organization, project, or task |
| `type` | Fact, preference, goal, constraint, decision, project, workflow, or open question |
| `statement` | One clear piece of information |
| `source` | User confirmation or exact authorized source |
| `status` | Confirmed, needs-verification, superseded, or retired |
| `confirmed_at` | Date/time last confirmed, ISO 8601 when known |
| `expires_at` | Expiry for information that can become stale; otherwise blank |
| `sensitivity` | Public, private, or sensitive |
| `supersedes` | Earlier record ID, if this replaces one |

## User context

```yaml
context_version: "4.0.0"
owner_label: UNCONFIGURED
preferred_language: UNCONFIGURED
reading_level: UNCONFIGURED
response_preferences: []
accessibility_preferences: []
explicit_values_to_consider: []
long_term_goals: []
important_constraints: []
```

## Organization and project context

```yaml
organizations: []
projects:
  - project_id: UNCONFIGURED
    name: UNCONFIGURED
    purpose: UNCONFIGURED
    status: UNCONFIGURED
    canonical_repository: UNCONFIGURED
    source_of_truth: UNCONFIGURED
    jurisdiction: UNCONFIGURED
    confirmed_decisions: []
    technical_constraints: []
    integrations: []
    acceptance_criteria: []
```

## Stable technical environment

Record only user-confirmed or source-verified details. Mark volatile versions and limits for live verification before implementation.

```yaml
development_environment:
  operating_system: UNCONFIGURED
  hosting_provider: UNCONFIGURED
  hosting_type: UNCONFIGURED
  runtime: VERIFY_LIVE
  database: VERIFY_LIVE
  web_server: VERIFY_LIVE
  available_extensions_or_modules: VERIFY_LIVE
  resource_limits: VERIFY_LIVE
  access_level: VERIFY
  prohibited_dependencies: []
```

## Reusable decisions and workflows

```yaml
decisions: []
recurring_workflows: []
known_risks: []
open_questions: []
```

## Change log

| Date | Record ID | Change | Source/approval |
|---|---|---|---|
| UNCONFIGURED | UNCONFIGURED | No user data is included in this template | Template |

## Privacy and safety

Never store passwords, OTPs, API keys, access tokens, private keys, recovery codes, payment credentials, session cookies, or third-party customer records. Avoid unnecessary identity, health, financial, and other sensitive personal data. Keep completed user context private; do not commit it to a public repository.

## Context maintenance procedure

1. Read the existing context before asking the user for known information.
2. Check scope, provenance, confirmation date, and whether volatile facts need live verification.
3. Identify only the missing details that materially affect the current task.
4. Ask one question, wait, and repeat only if another essential gap remains.
5. Present proposed additions, corrections, supersessions, and retirements as a reviewable diff.
6. Ask permission before durable writes; preserve a backup or change history.
7. Deduplicate only records that are genuinely identical in meaning, scope, and time. Similar records are not automatically duplicates.
8. Keep unresolved conflicts visible; do not select a winner without evidence or confirmation.
9. Report what was read, what was unavailable, what changed, and what could not be changed.


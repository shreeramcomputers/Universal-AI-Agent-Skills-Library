# config.md — Persistent User and Project Context

**Schema version:** 1.0.0  
**Purpose:** A user-owned, editable source of stable context for compatible AI agents. This file is documentation/data for the AI library. It is NOT PHP, server configuration, executable code, or a credential store.

## Core rules for every AI agent

1. Look for `config.md` in the current conversation uploads, the user's explicitly connected private AI Library, or the selected project repository. Do not assume it exists or that a platform can access it.
2. If found, read it before asking the user to repeat information. Apply only records whose scope matches the current user and task.
3. If it is missing or unavailable, continue the requested task. Do not block work, repeatedly ask for the whole profile, or invent missing values.
4. Gradually collect only high-value, reusable facts during normal work. Do not interrupt every task with a questionnaire.
5. At the end of each substantial task, perform a brief **Context Gap Check**:
   - Is there a stable fact, preference, constraint, approved decision, or reusable project rule that is not in config.md?
   - Is it genuinely useful in future tasks, explicitly stated/confirmed, and safe to retain?
   - Is it already present under another wording or scope?
   - Is it volatile, sensitive, temporary, or task-specific and therefore unsuitable?
6. If there is a worthwhile candidate, tell the user exactly what is missing, why it would help, and show the proposed text/section. Do not silently edit or persist it.
7. Ask permission before creating, uploading, replacing, or permanently updating config.md. If permission is declined or unavailable, continue without it.
8. When the user approves, produce a complete updated file and a concise change report. Preserve prior verified records and history; remove true duplicates only. Surface conflicts instead of silently choosing.
9. Never claim that a platform's internal memory changed unless an authorized memory capability confirms it. If no write capability exists, provide the corrected file and upload instructions.
10. Never put passwords, OTPs, API keys, private keys, recovery codes, session tokens, payment credentials, or third-party customer records in config.md.

## File lookup and fallback behavior

Search in this order, subject to actual client capabilities and user permission:
1. Current conversation attachments.
2. User's private AI Library / uploaded files.
3. The active project repository, if explicitly selected.
4. A user-provided local path or connected drive.

A public Skills repository is not a safe home for a personal config.md. It must contain only a blank schema/template and generic instructions. Never commit a user's personal config.md to this public repository.

If no config.md is available:
- Start the task with known context from the current conversation and authorized memory sources.
- Mark unknown project details as `UNKNOWN` or `VERIFY`.
- Ask only for a missing detail that blocks the next safe step.
- During normal work, collect reusable information gradually.
- At a suitable point, offer to create the first config.md after showing the proposed contents and obtaining permission.

## Record model

Use YAML-compatible records inside this Markdown document. Keep records atomic and scoped.

```yaml
config_schema_version: "1.0.0"
profile:
  display_preferences:
    language: "MATCH_USER"
    reading_level: "MATCH_USER"
    response_format: ["clear bullets", "practical examples"]
    confirmed_at: "YYYY-MM-DD"
  stable_preferences: []
  user_approved_rules: []
projects:
  - project_id: "stable-slug"
    name: "Project name"
    status: "active"
    source_of_truth: "repository or document URL"
    stable_decisions: []
    architecture_constraints: []
    approved_integrations: []
    deployment_constraints: []
    project_pages_and_policies: []
    confirmed_at: "YYYY-MM-DD"
records:
  - record_id: "unique-stable-id"
    scope: "user | project:<project_id>"
    type: "fact | preference | approved_decision | constraint | workflow"
    statement: "One clear statement"
    source: "user-confirmed | file:<path> | connector:<name>"
    confidence: "confirmed | high | medium"
    status: "active | superseded | needs_confirmation"
    confirmed_at: "YYYY-MM-DD"
    review_after: null
    supersedes: null
change_log: []
```

Do not store a fact merely because it appeared in generated text. Prefer direct user statements, authoritative project files, and owner-approved decisions. Store source and confirmation date.

## Stable vs changing information

**Good candidates:** preferred language/reading level, long-term coding constraints, confirmed project architecture, domain ownership, approved security rules, recurring workflow, stable integration decisions.

**Do not treat as permanent:** current software versions, API prices, quotas, laws, deadlines, balances, account status, temporary tasks, active incidents, open bugs, and changing hosting limits. Store these only as dated observations with a source and mandatory re-verification.

## Context Gap Check — required end-of-task behavior

Use a concise note, not a long form:

- `No update suggested` — no new stable information worth saving.
- `Suggested update` — show exact proposed record and reason; ask permission.
- `Conflict found` — show competing values and sources; ask which is current.
- `Config unavailable` — task continued; explain how the user can upload it if they want persistent continuity.

Do not repeat this prompt after trivial conversational replies. Run it after substantial research, decisions, project changes, code delivery, or new durable preferences.

## Duplicate and conflict policy

- Match exact record IDs first, then compare normalized meaning and scope.
- Merge only when scope, meaning, source quality, and time validity are compatible.
- Keep different projects, people, accounts, legal entities, and environments separate.
- Prefer the latest owner-confirmed value for the same field, but retain the superseded record in change history.
- A newer observation does not automatically invalidate a stable decision.
- Never resolve a material conflict by guessing.

## User-controlled update procedure

1. AI reads the current config.md and prepares a proposed diff.
2. User reviews additions, edits, retirements, and conflicts.
3. AI asks explicit permission to apply the update.
4. After approval, AI creates the complete replacement file, increments schema version only when structure changes, and adds a dated change-log entry.
5. AI validates Markdown/YAML structure, duplicate IDs, secret leakage, scope, and links.
6. User uploads the new file to their private AI Library or selected project repository.
7. AI confirms the exact new file is accessible before claiming it is the active config.

## Privacy and portability

This file may contain personal or business context. Keep it in a private AI Library or private repository. Do not publish it in this public repository, attach it to public bug reports, or send it to third-party services without the user's informed approval. Users may keep separate files for separate legal entities or sensitive projects where needed.

## English and Hinglish note

This canonical file uses simple English field names for portability. The AI should explain changes in the user's preferred language, including Hinglish, without duplicating the data into separate language copies.

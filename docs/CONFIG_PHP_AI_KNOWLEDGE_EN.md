# Use config.php as Your AI's Persistent Context File (English)

## Correct purpose
This `config.php` is NOT a server configuration and is NOT uploaded to web hosting. The user uploads it to the private Knowledge / Files area of the AI assistant (or attaches it to a chat when persistent Knowledge is unavailable). The AI reads it as plain text. It must never execute, include, or evaluate the PHP file.

## What belongs in the file?
Only information that is stable, repeatedly useful, and approved by the user:
- response language, reading level, communication preferences;
- confirmed identity or business facts the user wants retained;
- long-running projects, canonical repositories, durable decisions and constraints;
- verified technical defaults, clearly marked for re-verification when volatile;
- reusable legal/content preferences.

Do not store passwords, OTPs, API keys, private keys, recovery codes, full bank/card numbers, customer records, or unnecessary sensitive data. Avoid storing temporary tasks, one-time amounts, short-lived status, guesses, or unconfirmed facts.

## AI task-end context gap check
At the end of each substantial task, the AI must check the current conversation for useful durable facts that are absent from this file:
1. Is there a new stable preference, confirmed decision, project constraint, reusable technical default, or long-term fact?
2. Is it genuinely useful in future tasks, rather than a one-time detail?
3. Is it already present under another wording/key?
4. Does it conflict with a newer confirmed value?
5. Is it sensitive or uncertain and therefore requires explicit confirmation?

If nothing qualifies, say nothing about updating the file. Do not annoy the user with repeated empty checks.

If something qualifies, briefly tell the user:
- what new information was found;
- why it is useful to retain;
- the exact section/key and suggested value to add or change;
- whether the user should confirm it first.

Never silently edit or replace the user's canonical file. Provide a minimal patch or exact replacement snippet. The user reviews it, updates the file, and uploads/replaces the file in the AI Knowledge area.

## Updating the file
1. Download or open the current `config.php` from AI Knowledge.
2. Edit only the relevant key/value; preserve other confirmed information.
3. Increment `config_version` and update `updated_at`.
4. Review for duplicates, conflicts, temporary data, and secrets.
5. Upload the revised file and replace the old Knowledge file (or remove the old attachment from the active project/chat if the platform uses attachments rather than managed Knowledge).
6. Ask the AI to read the new version and confirm the version/date and changed keys.

## Platform limitations
The exact Knowledge/Files upload process differs by AI platform. This repository cannot directly update a user's ChatGPT/Claude/Gemini private Knowledge store. The user must upload/replace the file or use an officially supported, explicitly authorized connector. The AI must never claim the update was saved unless the platform confirms it.

## PHP file handling
The file returns a PHP array for a familiar, structured format. AI clients should inspect the source as text only. Never run it on an untrusted server or include it in application code. If a platform blocks PHP files, use the equivalent JSON or Markdown export; keep one canonical source and avoid maintaining conflicting copies.

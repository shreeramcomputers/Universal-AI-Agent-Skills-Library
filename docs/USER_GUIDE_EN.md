# User Guide (English)

## What this library is
A versioned collection of portable Agent Skills. A Skill is an instruction package, not a model, executable application, account permission, or guarantee that a client can use a tool.

## Start here
1. Browse [CATALOG.json](../CATALOG.json) and [Skills Directory](../skills/README.md).
2. Select the smallest set of Skills that covers the task.
3. Read the complete selected `SKILL.md`, then load [GLOBAL_RULES.md](../GLOBAL_RULES.md), relevant sections of [SKILL_RULES.md](../SKILL_RULES.md), and the user's confirmed `AI_CONTEXT.md` (if available). If it is missing, continue with available evidence and ask one question at a time only when a missing detail blocks the task.
4. Follow the relevant client installation guide in [INSTALLATION.md](../INSTALLATION.md).
5. Test on a harmless representative task before relying on the Skill.

## Choose and combine Skills
Use the catalogue description as a discovery hint, not proof of runtime activation. When work spans domains, use a small set of complementary Skills (for example, spec-driven development + PHP engineering + database engineering + security audit + test-driven development). Avoid installing every Skill unless the agent/client genuinely needs them.

## Compatibility
Agent clients differ in skill discovery, folder locations, frontmatter support, linked-file loading, tool access, and execution. This repository does not guarantee identical behavior across ChatGPT, Claude, Gemini, Codex, IDE agents, or other clients. Verify each client independently.

## Updating
Read [CHANGELOG.md](../CHANGELOG.md) and [MIGRATION.md](../MIGRATION.md), back up local edits, compare changes, update selected Skills, and rerun validation. Never overwrite customized files blindly.

## Evidence labels
PASS = tested and passed; FAIL = tested and failed; NOT RUN = not performed; UNVERIFIED = insufficient evidence; BLOCKED = missing permission or dependency.

## License
Written Skills and documentation are CC BY 4.0; scripts, tests, and workflow code are MIT. Read the license files before redistribution.

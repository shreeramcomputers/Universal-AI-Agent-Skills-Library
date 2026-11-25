# Migration Notes — v2.2.0

## Upgrade summary

Version 2.2.0 adds 10 general-purpose skills to the 21-skill v2.1.0 library. The 10 transferred workflows were rewritten to remove project-specific names, private repository references, owner/business/contact details, fixed URLs, API identifiers, and deployment assumptions. They are now portable across projects.

## Installation

1. Copy the complete `skills/` directory and the three shared files to your agent's supported skill/reference locations.
2. Keep relative folder structure unchanged unless the client requires a different layout.
3. Configure the agent to load `GLOBAL_RULES.md`, relevant `SKILL_RULES.md` sections, and the active project's confirmed `PROJECT_CONFIG.md`.
4. Fill project configuration only with values verified for that project. Do not copy another person's private settings.
5. Review client-specific skill discovery rules, permissions, tools, and runtime compatibility before use.

## License

No license is assigned in this release. Obtain the rights holder's decision before adding one or redistributing the material under a license.

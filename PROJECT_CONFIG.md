# PROJECT_CONFIG.md — Legacy compatibility notice

The canonical user/project context file is now **[config.md](config.md)**.

This file remains temporarily so older Skills, installers, and AI clients that still look for `PROJECT_CONFIG.md` do not fail. It is not a second configuration file and must not hold a separate copy of user data.

Rules:
- Read `config.md` as the single source of user/project context.
- If `config.md` is unavailable, continue safely with current authorized context and mark unknowns; do not block the task.
- Do not create or update this legacy file independently.
- Do not put personal `config.md` data in this public repository.
- Update old Skill links to point to `config.md` over time.

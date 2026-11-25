# Installation Guide

This library uses the open Agent Skills folder format. Agent clients differ in how they discover skills and load linked files. Always verify the installed paths and behavior in the selected client.

## Recommended: use the bundled installer

The installer keeps the shared files adjacent to the skill folders so the relative links resolve.

### Install one skill

From the directory where the skills should be installed:

```bash
git clone --depth 1 https://github.com/shreeramcomputers/Universal-AI-Agent-Skills-Library.git
python3 Universal-AI-Agent-Skills-Library/scripts/install_skill.py \
  --skill secure-rest-api-engineering \
  --destination .agents/skills
```

### Install multiple skills

```bash
python3 Universal-AI-Agent-Skills-Library/scripts/install_skill.py \
  --skill frontend-ui-engineering \
  --skill accessibility-engineering \
  --skill test-driven-development \
  --destination .agents/skills
```

### Install all skills

```bash
python3 Universal-AI-Agent-Skills-Library/scripts/install_skill.py \
  --all --destination .agents/skills
```

Default destination is `.agents/skills`. Shared policy files are copied into the destination's parent directory. For the default destination this is `.agents/`, so the skill's `../../GLOBAL_RULES.md` reference resolves correctly.

The installer refuses to overwrite existing files. Review conflicts first; use `--force` only after backing up and reviewing existing content.

## Skills CLI

The community Skills CLI can install compatible folders into supported agents:

```bash
npx skills add shreeramcomputers/Universal-AI-Agent-Skills-Library --list
npx skills add shreeramcomputers/Universal-AI-Agent-Skills-Library --skill frontend-ui-engineering
```

Some CLI installations copy only the selected skill folder. If root shared files were not installed, copy GLOBAL_RULES.md, SKILL_RULES.md, and PROJECT_CONFIG.md to the location expected by the skill links, or use the bundled installer.

## Manual installation

1. Copy a selected folder from `skills/<skill-name>/` to the chosen agent's skill directory.
2. Copy the three shared files into the location that makes the skill's relative links resolve.
3. Confirm the installed folder contains SKILL.md and that all three shared links resolve.
4. Configure the client to load the shared rules before skill execution when the client does not follow Markdown links automatically.
5. Test the skill on a safe, representative task.

## Updating

- Review the new version and CHANGELOG before replacing existing skills.
- Back up local edits.
- Re-run the installer; it will refuse to overwrite until you resolve conflicts or explicitly use --force.
- Re-run the validation and representative client tests.
- Do not assume an update is compatible merely because the skill name is unchanged.

## Requirements and limitations

- Python 3.9+ for the bundled installer and validator; no third-party Python packages are required.
- A compatible Agent Skills client or a manual workflow for reading the skill files.
- Skills are instructions. They do not install system packages, grant permissions, or guarantee tool availability.

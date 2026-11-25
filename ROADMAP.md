# Roadmap

This roadmap describes potential priorities, not promises or scheduled delivery.

## Current release — 3.0.0
- 44 focused, portable skills.
- Shared global, domain, and project-configuration rules.
- Bundled installer, validator, tests, and GitHub Actions validation.
- Contribution, security, support, licensing, and migration documentation.

## Next priorities
1. Validate selected skills in multiple Agent Skills-compatible clients and record exact client/version/results.
2. Add focused reference files only where a skill's core instructions would otherwise become long or difficult to maintain.
3. Add structured examples and small, deterministic fixtures for high-value skills.
4. Add evaluation cases that test correct activation, refusal boundaries, evidence quality, and completion claims.
5. Improve translations only when maintainers can review technical accuracy.
6. Add release packaging and changelog automation after reproducible build and license checks are established.

## Quality principles
- Prefer correctness, usefulness, safety, and maintainability over skill count.
- Add a new skill only for a distinct recurring workflow.
- Retire or merge overlap rather than keeping duplicate folders.
- Never claim cross-platform compatibility without testing.

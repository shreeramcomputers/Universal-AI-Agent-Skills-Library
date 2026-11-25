#!/usr/bin/env python3
"""Install one or more skills and their shared rules without external packages."""
from __future__ import annotations
import argparse, shutil, sys
from pathlib import Path

SHARED = ("GLOBAL_RULES.md", "SKILL_RULES.md", "AI_CONTEXT.md")

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--skill", action="append", help="Skill folder name; may be repeated")
    group.add_argument("--all", action="store_true", help="Install every skill in this library")
    parser.add_argument("--destination", type=Path, default=Path(".agents/skills"))
    parser.add_argument("--force", action="store_true", help="Replace existing files")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    skills_root = root / "skills"
    selected = sorted(p.name for p in skills_root.iterdir() if p.is_dir()) if args.all else args.skill
    if not selected:
        parser.error("No skills were selected")
    for name in selected:
        if Path(name).name != name or name in {".", ".."}:
            parser.error("Invalid skill name: " + repr(name))
        if not (skills_root / name / "SKILL.md").is_file():
            parser.error("Unknown skill: " + name)
    destination = args.destination.expanduser().resolve()
    shared_destination = destination.parent
    conflicts = [shared_destination / name for name in SHARED if (shared_destination / name).exists()]
    conflicts += [destination / name for name in selected if (destination / name).exists()]
    if conflicts and not args.force:
        print("Refusing to overwrite existing files. Review them or rerun with --force:", file=sys.stderr)
        for path in conflicts:
            print("- " + str(path), file=sys.stderr)
        return 2
    destination.mkdir(parents=True, exist_ok=True)
    for name in SHARED:
        shutil.copy2(root / name, shared_destination / name)
    for name in selected:
        target = destination / name
        if target.exists():
            shutil.rmtree(target)
        shutil.copytree(skills_root / name, target)
    print("Installed " + str(len(selected)) + " skill(s) into " + str(destination))
    print("Shared rules installed into " + str(shared_destination))
    print("The installed structure preserves each skill's ../../ shared-file links.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

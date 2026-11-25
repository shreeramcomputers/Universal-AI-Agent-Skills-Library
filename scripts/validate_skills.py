#!/usr/bin/env python3
"""Dependency-free static validator for the Universal AI Agent Skills Library."""
from __future__ import annotations
import argparse, json, re
from pathlib import Path

NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
PRIVATE_PATTERNS = [
    re.compile(r"(?i)\bgaurav(?:\s+jain)?\b"),
    re.compile(r"(?i)\bshree\s*ram\s*computers\b"),
    re.compile(r"(?i)\bshreeramcomputers\b"),
    re.compile(r"(?i)\bdaurala\b|\bmeerut\b"),
    re.compile(r"(?i)shreeramcomputers\.com"),
    re.compile(r"(?i)-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}\b"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
]
REQUIRED_SHARED = ("GLOBAL_RULES.md", "SKILL_RULES.md", "PROJECT_CONFIG.md")

def parse_frontmatter(text):
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("SKILL.md must begin with YAML frontmatter")
    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration as exc:
        raise ValueError("YAML frontmatter closing delimiter is missing") from exc
    values = {}
    for line in lines[1:end]:
        if not line.strip() or line.lstrip().startswith("#") or line[:1].isspace():
            continue
        if ":" not in line:
            raise ValueError("Invalid frontmatter line: " + line)
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip().strip("\"'")
        if key in values:
            raise ValueError("Duplicate frontmatter key: " + key)
        values[key] = value
    return values, "\n".join(lines[end + 1:])

def validate_skill(skill_file, root):
    errors = []
    folder_name = skill_file.parent.name
    try:
        text = skill_file.read_text(encoding="utf-8")
        values, body = parse_frontmatter(text)
    except Exception as exc:
        return [str(skill_file.relative_to(root)) + ": " + str(exc)]
    name = values.get("name", "")
    description = values.get("description", "")
    if not name:
        errors.append("missing name")
    elif not NAME_RE.fullmatch(name) or len(name) > 64:
        errors.append("invalid name: " + repr(name))
    if name != folder_name:
        errors.append("name does not match its parent directory")
    if not description:
        errors.append("missing description")
    elif len(description) > 1024:
        errors.append("description exceeds 1024 characters")
    if values.get("license") != "CC-BY-4.0":
        errors.append("license must be CC-BY-4.0")
    if not body.strip():
        errors.append("instruction body is empty")
    if len(text.splitlines()) > 500:
        errors.append("SKILL.md exceeds 500 lines")
    for required in REQUIRED_SHARED:
        if "../../" + required not in text:
            errors.append("missing shared-file link to ../../" + required)
    for match in LINK_RE.finditer(text):
        target = match.group(1).strip()
        if target.startswith(("https://", "http://", "mailto:", "#")):
            continue
        target = target.split("#", 1)[0]
        if target and not (skill_file.parent / target).resolve().exists():
            errors.append("broken relative link: " + match.group(1))
    for pattern in PRIVATE_PATTERNS:
        if pattern.search(text):
            errors.append("possible private data/secret pattern: " + pattern.pattern)
    return [str(skill_file.relative_to(root)) + ": " + item for item in errors]

def validate_library(root):
    errors = []
    skills_dir = root / "skills"
    skill_files = sorted(skills_dir.glob("*/SKILL.md")) if skills_dir.exists() else []
    if not skill_files:
        return ["no skill folders were found"]
    names = set()
    for file in skill_files:
        errors.extend(validate_skill(file, root))
        try:
            name = parse_frontmatter(file.read_text(encoding="utf-8"))[0].get("name", "")
            if name in names:
                errors.append("duplicate skill name: " + name)
            names.add(name)
        except Exception:
            pass
    for shared in REQUIRED_SHARED:
        path = root / shared
        if not path.is_file():
            errors.append("missing shared file: " + shared)
        elif path.stat().st_size == 0:
            errors.append("empty shared file: " + shared)
    catalog_path = root / "CATALOG.json"
    if catalog_path.exists():
        try:
            catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
            entries = catalog.get("skills", [])
            catalog_names = {item.get("name") for item in entries}
            if catalog.get("skill_count") != len(skill_files):
                errors.append("catalog skill_count does not match skill files")
            if len(entries) != len(skill_files):
                errors.append("catalog entry count does not match skill files")
            if catalog_names != names:
                errors.append("catalog names do not match skill folder names")
            for item in entries:
                rel = item.get("path", "")
                if not rel or not (root / rel).is_file():
                    errors.append("catalog path missing: " + repr(rel))
                if len(item.get("description", "")) > 1024:
                    errors.append("catalog description too long: " + str(item.get("name")))
        except Exception as exc:
            errors.append("CATALOG.json invalid: " + str(exc))
    else:
        errors.append("missing CATALOG.json")
    rules_path = root / "SKILL_RULES.md"
    if rules_path.exists():
        rules = rules_path.read_text(encoding="utf-8")
        for name in sorted(names):
            if name not in rules:
                errors.append("SKILL_RULES.md routing matrix missing " + name)
    scan_files = list(skill_files) + [root / name for name in REQUIRED_SHARED if (root / name).is_file()]
    for file in scan_files:
        text = file.read_text(encoding="utf-8")
        for pattern in PRIVATE_PATTERNS:
            if pattern.search(text):
                errors.append(str(file.relative_to(root)) + ": possible private data/secret pattern " + pattern.pattern)
    return errors

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    root = args.root.resolve()
    errors = validate_library(root)
    if errors:
        print("FAIL: " + str(len(errors)) + " validation issue(s)")
        for error in errors:
            print("- " + error)
        return 1
    count = len(list((root / "skills").glob("*/SKILL.md")))
    print("PASS: " + str(count) + " skills, frontmatter, names, shared links, local links, catalog, routing, privacy patterns")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""
Strict gate:
- If a commit changes architecture/runtime files, ARCH_CHANGELOG.md must contain
  a completed entry with: Date, Files, Changed, Why, UAT.

This prevents "patch drift" and missing audit trails.
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
CHANGELOG = REPO_ROOT / "ARCH_CHANGELOG.md"

# What we consider "architecture/runtime" changes that require audit trail
ARCH_PATH_PREFIXES = (
    "00__LOCKED__UPLOAD_SET/",
    "runner/",
    "tests/",
)

ARCH_EXEMPT_FILES = set()


def run(cmd: list[str]) -> str:
    p = subprocess.run(cmd, capture_output=True, text=True)
    if p.returncode != 0:
        raise RuntimeError(f"Command failed: {' '.join(cmd)}\n{p.stderr}")
    return p.stdout.strip()


def staged_files() -> list[str]:
    out = run(["git", "diff", "--cached", "--name-only"])
    return [ln.strip() for ln in out.splitlines() if ln.strip()]


def is_arch_change(path: str) -> bool:
    if path in ARCH_EXEMPT_FILES:
        return False
    return any(path.startswith(prefix) for prefix in ARCH_PATH_PREFIXES)


def read_changelog() -> str:
    if not CHANGELOG.exists():
        return ""
    return CHANGELOG.read_text(encoding="utf-8", errors="replace")


def extract_last_entry(text: str) -> str:
    """
    We take the content AFTER "## Entries" and look for the last non-empty block.
    An "entry" is everything from a "Date:" line up to the next "Date:" or EOF.
    """
    if "## Entries" not in text:
        return ""
    tail = text.split("## Entries", 1)[1].strip()
    if not tail:
        return ""

    # Find all entry starts (Date:)
    starts = [m.start() for m in re.finditer(r"(?m)^\s*-?\s*Date:\s*", tail)]
    if not starts:
        return ""

    last_start = starts[-1]
    entry = tail[last_start:].strip()
    return entry


def field_value(entry: str, field: str) -> str:
    m = re.search(rf"(?mi)^\s*-?\s*{re.escape(field)}:\s*(.+?)\s*$", entry)
    return m.group(1).strip() if m else ""


def main() -> int:
    files = staged_files()
    arch_files = [f for f in files if is_arch_change(f)]

    # If no arch/runtime files are staged, allow commit.
    if not arch_files:
        return 0

    text = read_changelog()
    entry = extract_last_entry(text)
    if not entry:
        print(
            "ARCH_CHANGELOG gate failed:\n"
            "- You staged architecture/runtime changes but ARCH_CHANGELOG.md has no entry.\n"
            "Add an entry under '## Entries' with Date/Files/Changed/Why/UAT.\n"
            "Staged arch files:\n- " + "\n- ".join(arch_files),
            file=sys.stderr,
        )
        return 1

    required = ["Date", "Files", "Changed", "Why", "UAT"]
    missing = [k for k in required if not field_value(entry, k)]
    if missing:
        print(
            "ARCH_CHANGELOG gate failed:\n"
            f"- Last changelog entry is missing fields: {missing}\n"
            "Fill them in (non-empty) before committing.\n"
            f"Staged arch files:\n- " + "\n- ".join(arch_files),
            file=sys.stderr,
        )
        return 1

    # Lightweight relevance check: Files field must mention at least one changed file name
    files_field = field_value(entry, "Files")
    if files_field.upper() not in {"MULTIPLE", "ALL"}:
        mentioned = {p.strip() for p in re.split(r"[,\n]", files_field) if p.strip()}
        changed_basenames = {Path(f).name for f in arch_files}
        mentioned_basenames = {Path(m).name for m in mentioned}
        if mentioned_basenames.isdisjoint(changed_basenames):
            print(
                "ARCH_CHANGELOG gate failed:\n"
                "- 'Files:' in the last entry does not mention any staged arch file.\n"
                "Tip: set Files: MULTIPLE or list at least one of the changed files.\n"
                f"Files field: {files_field}\n"
                f"Staged arch files:\n- " + "\n- ".join(arch_files),
                file=sys.stderr,
            )
            return 1

    # UAT field must not be placeholder text
    uat_field = field_value(entry, "UAT")
    if uat_field.strip().upper() in {"TBD", "TODO", "NONE", "N/A"}:
        print(
            "ARCH_CHANGELOG gate failed:\n"
            "- 'UAT:' must name the UAT case(s) or command used (not TBD/TODO/NONE/N/A).\n"
            "Example: UAT: case_id=ppf_mixed (run_uat.py)\n"
            "Staged arch files:\n- " + "\n- ".join(arch_files),
            file=sys.stderr,
        )
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

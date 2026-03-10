#!/usr/bin/env python3
import subprocess
from pathlib import Path

CHANGELOG = Path("ARCH_CHANGELOG.md")


def staged_files():
    result = subprocess.run(
        ["git", "diff", "--cached", "--name-only"],
        capture_output=True,
        text=True,
    )
    return [f.strip() for f in result.stdout.splitlines() if f.strip()]


def main():
    files = staged_files()

    arch_files = [
        f for f in files
        if f.startswith("00__LOCKED__UPLOAD_SET/")
        or f.startswith("runner/")
        or f.startswith("tests/")
    ]

    # Prevent recursion if only changelog itself is staged
    arch_files = [
        f for f in arch_files
        if f not in {"ARCH_CHANGELOG.md", "runner/generate_arch_changelog.py"}
    ]

    if not arch_files:
        return

    # Stop if TODO template already exists
    if CHANGELOG.exists():
        content = CHANGELOG.read_text()
        if "Changed: TODO" in content:
            return

    entry = """
Date: TODO
Files: MULTIPLE
Changed: TODO
Why: TODO
UAT: TODO
"""

    with CHANGELOG.open("a") as f:
        f.write("\n" + entry)

    subprocess.run(["git", "add", "ARCH_CHANGELOG.md"])


if __name__ == "__main__":
    main()

import subprocess
from datetime import date
from pathlib import Path

CHANGELOG = Path("ARCH_CHANGELOG.md")


def run(cmd):
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout.strip()


def staged_files():
    files = run(["git", "diff", "--cached", "--name-only"])
    return [f for f in files.splitlines() if f]


def main():
    files = staged_files()

    if not files:
        return

    arch_files = [
        f for f in files
        if f.startswith("00__LOCKED__UPLOAD_SET/")
        or f.startswith("runner/")
        or f.startswith("tests/")
    ]

    # Prevent recursion: if the only staged file is the changelog itself
    arch_files = [f for f in arch_files if f not in {"ARCH_CHANGELOG.md", "runner/generate_arch_changelog.py"}]

    if not arch_files:
        return

    entry = f"""

Date: {date.today()}
Files: MULTIPLE
Changed: TODO
Why: TODO
UAT: TODO
"""

    with open(CHANGELOG, "a") as f:
        f.write(entry)

    print("\nARCH_CHANGELOG template inserted.\n")


if __name__ == "__main__":
    main()

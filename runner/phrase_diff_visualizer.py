import subprocess
from pathlib import Path

PHRASE_FILE = "00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_6_HUMAN_PHRASE_LIBRARY.md"


def run(cmd):
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout.strip()


def main():
    if not Path(PHRASE_FILE).exists():
        return

    diff = run(["git", "diff", "--cached", PHRASE_FILE])

    if not diff:
        return

    print("\n--- Phrase Change Review ---\n")

    for line in diff.splitlines():
        if line.startswith("+") and not line.startswith("+++"):
            print("ADD:", line[1:])
        elif line.startswith("-") and not line.startswith("---"):
            print("DEL:", line[1:])
        elif line.startswith("@@"):
            print("\nSECTION CHANGE\n")


if __name__ == "__main__":
    main()

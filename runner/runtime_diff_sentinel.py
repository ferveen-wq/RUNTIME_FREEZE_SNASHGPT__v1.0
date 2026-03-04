import subprocess
import sys

# Maximum allowed deletions in a single commit before blocking
MAX_DELETIONS = 300

# Runtime-critical files that should trigger warnings if edited
PROTECTED_FILES = [
    "PRICE_TABLE_VAT_INCL.md",
    "SKU_SELECTION_MATRIX.md",
    "PHASE4_6_HUMAN_PHRASE_LIBRARY.md",
]


def get_diff():
    result = subprocess.run(
        ["git", "diff", "--cached", "--numstat"],
        capture_output=True,
        text=True,
    )
    return result.stdout.splitlines()


def main():
    lines = get_diff()

    for line in lines:
        parts = line.split("\t")

        if len(parts) != 3:
            continue

        added, deleted, file = parts

        try:
            deleted = int(deleted)
        except ValueError:
            continue

        # Block extremely large deletions
        if deleted > MAX_DELETIONS:
            print(f"BLOCKED: Large deletion detected in {file}")
            sys.exit(1)

        # Warn if protected runtime files are modified
        for protected in PROTECTED_FILES:
            if protected in file and deleted > 0:
                print(f"WARNING: Editing protected runtime file: {file}")

    print("Runtime diff sentinel passed")


if __name__ == "__main__":
    main()

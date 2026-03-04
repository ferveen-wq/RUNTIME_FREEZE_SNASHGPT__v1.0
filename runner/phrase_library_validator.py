import sys
from pathlib import Path

# Location of the phrase library
PHRASE_FILE = Path("00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_6_HUMAN_PHRASE_LIBRARY.md")

# Critical phrase keys that must always exist
REQUIRED_PHRASE_KEYS = [
    "PHASE4_PPF_SILENCE_COVERAGE_NARROW",
    "PHASE3B_PPF_RANGE",
    "PHASE 5 — STRUCTURED DEEPENING (OBJECTION / CLARIFICATION LAYER)",
    "## H. OBJECTION EXPLANATION LANGUAGE",
]

# Safety threshold to detect accidental truncation
MIN_EXPECTED_LINES = 400


def main():

    # Check phrase library exists
    if not PHRASE_FILE.exists():
        print("ERROR: Phrase library file missing")
        sys.exit(1)

    content = PHRASE_FILE.read_text()
    lines = content.splitlines()

    # Detect accidental large deletions
    if len(lines) < MIN_EXPECTED_LINES:
        print("ERROR: Phrase library appears truncated")
        sys.exit(1)

    # Ensure critical phrase IDs exist
    for key in REQUIRED_PHRASE_KEYS:
        if key not in content:
            print(f"ERROR: Missing phrase key: {key}")
            sys.exit(1)

    print("PHRASE LIBRARY VALIDATION PASSED")


if __name__ == "__main__":
    main()

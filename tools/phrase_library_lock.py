from pathlib import Path
import sys

PHRASE_FILE = "00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_6_HUMAN_PHRASE_LIBRARY.md"

if not Path(PHRASE_FILE).exists():
    print("ERROR: Phrase library file missing.")
    sys.exit(1)

text = Path(PHRASE_FILE).read_text(encoding="utf-8")

if "PHASE3A" not in text or "PHASE4" not in text:
    print("ERROR: Phrase library structure appears corrupted.")
    sys.exit(1)

print("Phrase library integrity OK.")

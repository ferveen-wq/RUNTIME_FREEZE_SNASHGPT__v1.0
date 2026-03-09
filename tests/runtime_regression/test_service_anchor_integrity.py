import sys
from pathlib import Path

FILE = Path("00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_6_HUMAN_PHRASE_LIBRARY.md")

REQUIRED_ANCHORS = [
    "PHASE3A_Q_PPF",
    "PHASE3A_Q_CERAMIC",
    "PHASE3A_Q_TINT",
    "PHASE3A_Q_WRAP",
    "PHASE3A_Q_POLISH",

    "PHASE4_PPF",
    "PHASE4_CERAMIC",
    "PHASE4_TINT",
    "PHASE4_WRAP",
    "PHASE4_POLISH",

    "PHASE5_POLISH",
]

text = FILE.read_text()

missing = []

for anchor in REQUIRED_ANCHORS:
    if anchor not in text:
        missing.append(anchor)

if missing:
    print("SERVICE ANCHOR REGRESSION FAILED")
    print("Missing anchors:")
    for m in missing:
        print("-", m)
    sys.exit(1)

print("SERVICE ANCHOR REGRESSION PASSED")

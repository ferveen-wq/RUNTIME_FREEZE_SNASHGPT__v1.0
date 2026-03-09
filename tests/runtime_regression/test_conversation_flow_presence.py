import sys
from pathlib import Path

FILE = Path("00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_6_HUMAN_PHRASE_LIBRARY.md")

REQUIRED_FLOW_MARKERS = [

    # Phase3A qualification
    "PHASE3A_Q_PPF",
    "PHASE3A_Q_CERAMIC",
    "PHASE3A_Q_TINT",
    "PHASE3A_Q_WRAP",
    "PHASE3A_Q_POLISH",

    # Phase4 pressure handling
    "PHASE4_PPF",
    "PHASE4_CERAMIC",
    "PHASE4_TINT",
    "PHASE4_WRAP",
    "PHASE4_POLISH",

    # Phase5 deeper handling
    "PHASE5_POLISH",
]

text = FILE.read_text()

missing = []

for marker in REQUIRED_FLOW_MARKERS:
    if marker not in text:
        missing.append(marker)

if missing:
    print("CONVERSATION FLOW REGRESSION FAILED")
    print("Missing flow markers:")
    for m in missing:
        print("-", m)
    sys.exit(1)

print("CONVERSATION FLOW REGRESSION PASSED")

import sys
from pathlib import Path

FILE = Path("00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_6_HUMAN_PHRASE_LIBRARY.md")

REQUIRED_SELECTORS = [

    # Phase 3A qualification
    "PHASE3A_Q_PPF_COVERAGE_INTENT",
    "PHASE3A_Q_PPF_COMPARISON_FOCUS",
    "PHASE3A_Q_PPF_DRIVING_PATTERN",
    "PHASE3A_Q_CERAMIC_GOAL",
    "PHASE3A_Q_TINT_GOAL",
    "PHASE3A_Q_WRAP_FINISH",
    "PHASE3A_Q_POLISHING_SCOPE",

    # Phase 4 pressure handling
    "PHASE4_PPF_PRICE_PRESSURE_L1",
    "PHASE4_CERAMIC_PRICE_PRESSURE_L1",
    "PHASE4_TINT_PRICE_PRESSURE_L1",
    "PHASE4_WRAP_PRICE_PRESSURE_L1",
    "PHASE4_POLISH_PRICE_PRESSURE_L1",

    # Phase 5 polishing ladder
    "PHASE5_POLISH_EXPECTATION_DEEPEN_L1",
    "PHASE5_POLISH_NARROW_L2",
    "PHASE5_POLISH_EXIT_FORK_L3",
]

text = FILE.read_text()

missing = []

for selector in REQUIRED_SELECTORS:
    if selector not in text:
        missing.append(selector)

if missing:
    print("PHRASE SELECTOR REGRESSION FAILED")
    print("Missing selectors:")
    for m in missing:
        print("-", m)
    sys.exit(1)

print("PHRASE SELECTOR REGRESSION PASSED")

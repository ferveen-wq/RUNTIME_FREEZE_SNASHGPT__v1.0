import sys
from pathlib import Path

phrase_file = Path("00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_6_HUMAN_PHRASE_LIBRARY.md")

required_phrases = [
"PHASE3A_Q_POLISHING_SCOPE",
"PHASE4_POLISH_EXPECTATION_REALISM_L1",
"PHASE4_POLISH_SCOPE_CLARITY_L1",
"PHASE4_POLISH_PRICE_PRESSURE_L1",
"PHASE4_POLISH_PRICE_PRESSURE_L2",
"PHASE4_POLISH_PRICE_PRESSURE_L3",
"PHASE4_POLISH_VS_PROTECTION_SIMPLE_L1",
"PHASE4_POLISH_SILENCE_PRIMARY",
"PHASE4_POLISH_SILENCE_SCOPE_NUDGE",
"PHASE5_POLISH_EXPECTATION_DEEPEN_L1",
"PHASE5_POLISH_NARROW_L2",
"PHASE5_POLISH_EXIT_FORK_L3"
]

text = phrase_file.read_text()

missing = []

for phrase in required_phrases:
    if phrase not in text:
        missing.append(phrase)

if missing:
    print("POLISH PHRASE REGRESSION FAILED")
    print("Missing phrases:")
    for m in missing:
        print("-", m)
    sys.exit(1)

print("POLISH PHRASE REGRESSION PASSED")

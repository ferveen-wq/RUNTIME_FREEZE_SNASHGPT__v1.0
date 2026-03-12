import os

required_files = [
    "00__LOCKED__UPLOAD_SET/00__Runtime/PHASE7_EDUCATION_SNIPPETS.md",
    "00__LOCKED__UPLOAD_SET/00__Runtime/PHASE7__CORE_EDUCATION.md",
    "00__LOCKED__UPLOAD_SET/00__Runtime/EDUCATION_TRIGGER_MATRIX.md",
    "00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_8_MESSAGE_ASSEMBLY_MAP.md"
]

missing = []

for f in required_files:
    if not os.path.exists(f):
        missing.append(f)

if missing:
    print("\n❌ Phase 7 wiring problem detected.")
    for m in missing:
        print("Missing:", m)
else:
    print("\n✔ Phase 7 education architecture verified.")

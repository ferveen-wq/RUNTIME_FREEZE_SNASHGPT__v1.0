from pathlib import Path

FILE = "00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_6_HUMAN_PHRASE_LIBRARY.md"

print("\n=== BILINGUAL PHRASE SYMMETRY AUDIT ===\n")

lines = Path(FILE).read_text(encoding="utf-8").splitlines()

issues = 0

for i, line in enumerate(lines):
    if line.strip().startswith("EN:"):
        if i + 1 >= len(lines) or not lines[i + 1].strip().startswith("AR:"):
            print(f"Missing AR after line {i+1}:")
            print(line.strip())
            print("")
            issues += 1

    if line.strip().startswith("AR:"):
        if i == 0 or not lines[i - 1].strip().startswith("EN:"):
            print(f"Missing EN before line {i+1}:")
            print(line.strip())
            print("")
            issues += 1

if issues == 0:
    print("No EN/AR symmetry issues detected.")

print("\nAudit complete.\n")

FILE = "00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_6_HUMAN_PHRASE_LIBRARY.md"

print("\n=== BILINGUAL PHRASE SYMMETRY AUDIT ===\n")

lines = Path(FILE).read_text(encoding="utf-8").splitlines()

issues = 0

for i, line in enumerate(lines):

    if line.strip().startswith("EN:"):
        window = lines[i+1:i+6]
        if not any(line_item.strip().startswith("AR:") for line_item in window):
            print(f"Possible missing AR near line {i+1}")
            print(line.strip())
            print("")
            issues += 1

    if line.strip().startswith("AR:"):
        window = lines[max(i-5,0):i]
        if not any(line_item.strip().startswith("EN:") for line_item in window):
            print(f"Possible missing EN near line {i+1}")
            print(line.strip())
            print("")
            issues += 1

if issues == 0:
    print("No bilingual symmetry issues detected.")

print("\nAudit complete.\n")
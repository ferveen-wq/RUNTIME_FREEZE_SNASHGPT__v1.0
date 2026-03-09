import re
from pathlib import Path

FILE = "00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_6_HUMAN_PHRASE_LIBRARY.md"

RISK_PATTERNS = {
    "FRONT_BIAS": r"\bfront\b",
    "PRICE_LEAK": r"\bprice\b|\bcost\b",
    "SKU_LEAK": r"\b5 year\b|\b10 year\b|\b7 year\b",
    "PROTECTION_CONFUSION": r"protects.*(ceramic|polish)",
    "DOWNGRADE_LANGUAGE": r"\bbudget\b|\bcheap\b",
}

text = Path(FILE).read_text()

print("\n=== PHRASE RISK AUDIT ===\n")

for name, pattern in RISK_PATTERNS.items():
    matches = re.findall(pattern, text, re.IGNORECASE)
    if matches:
        print(f"{name}: {len(matches)} matches")

print("\nAudit complete.\n")


import re
from pathlib import Path

FILE = "00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_6_HUMAN_PHRASE_LIBRARY.md"

RISK_PATTERNS = {
    "FRONT_BIAS": r"\bfront\b",
    "PRICE_LEAK": r"\bprice\b|\bcost\b",
    "SKU_LEAK": r"\b5 year\b|\b7 year\b|\b10 year\b",
    "PROTECTION_CONFUSION": r"protects.*(ceramic|polish)",
    "DOWNGRADE_LANGUAGE": r"\bbudget\b|\bcheap\b",
}

print("\n=== PHRASE RISK AUDIT ===\n")

with open(FILE, "r", encoding="utf-8") as f:
    lines = f.readlines()

for risk_name, pattern in RISK_PATTERNS.items():
    print(f"\n--- {risk_name} ---")
    found = False

    for i, line in enumerate(lines, start=1):
        if re.search(pattern, line, re.IGNORECASE):
            print(f"Line {i}: {line.strip()}")
            found = True

    if not found:
        print("No matches")

print("\nAudit complete.\n")

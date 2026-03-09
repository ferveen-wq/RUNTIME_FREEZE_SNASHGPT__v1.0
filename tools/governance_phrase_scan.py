from pathlib import Path
import re

FILE = "00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_6_HUMAN_PHRASE_LIBRARY.md"

print("\n=== PHRASE GOVERNANCE SCAN ===\n")

text = Path(FILE).read_text(encoding="utf-8")

rules = {
    "FRONT_BIAS": r"\bfront only\b|\bfront protection\b",
    "PRICE_STEERING": r"\bbudget\b|\bcheapest\b|\blowest price\b",
    "DOWNGRADE_LANGUAGE": r"\bkeep it simple\b|\blight option\b|\bbasic option\b",
    "PROTECTION_CONFUSION": r"ceramic.*protect|protect.*ceramic",
    "SKU_LEAK": r"\bSKU\b|\bPPF-\d+\b"
}

for name, pattern in rules.items():
    matches = re.findall(pattern, text, re.IGNORECASE)
    print(f"{name}: {len(matches)} matches")

print("\nScan complete.\n")

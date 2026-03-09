import json
import re
from pathlib import Path

PHRASE_FILE = "00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_6_HUMAN_PHRASE_LIBRARY.md"

canon_product = json.load(open("governance/canon/product_canon.json"))
canon_phrase = json.load(open("governance/canon/phrase_governance.json"))
canon_arch = json.load(open("governance/canon/architecture_rules.json"))

text = Path(PHRASE_FILE).read_text(encoding="utf-8")

# Auto-patch replacements
auto_patch = {
    "cheap": "affordable",
    "budget": "practical option"
}

print("\n=== RUNTIME GUARDIAN ===\n")

violations = 0

# Forbidden words + auto patch
for word in canon_phrase["forbidden_words"]:
    if word in text:
        print(f"Forbidden phrase detected: {word}")
        violations += 1

        if word in auto_patch:
            replacement = auto_patch[word]
            text = re.sub(rf"\b{word}\b", replacement, text, flags=re.IGNORECASE)
            print(f"Auto-patched: {word} → {replacement}")

# Downgrade language + auto patch
for word in canon_phrase["downgrade_language"]:
    if word in text:
        print(f"Downgrade language detected: {word}")
        violations += 1

        if word in auto_patch:
            replacement = auto_patch[word]
            text = re.sub(rf"\b{word}\b", replacement, text, flags=re.IGNORECASE)
            print(f"Auto-patched: {word} → {replacement}")

# Product canon invalid claims
for claim in canon_product["ceramic"]["invalid_claims"]:
    if claim in text:
        print(f"Invalid ceramic claim detected: {claim}")
        violations += 1

if violations == 0:
    print("Runtime guardian passed.")

else:
    print(f"\nGuardian detected {violations} governance warnings.")
    print("Warnings logged. Guardian currently running in audit mode.")

# Save patched phrase library if changes occurred
Path(PHRASE_FILE).write_text(text, encoding="utf-8")

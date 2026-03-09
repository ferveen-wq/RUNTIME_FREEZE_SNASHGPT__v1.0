import os

ledger_path = "00__LOCKED__UPLOAD_SET/00__Runtime/RUNTIME_CHANGE_LEDGER.md"

block_header = "## OBJECTION MAP (AUTOMOTIVE PROTECTION)"

block = f"""
{block_header}

Purpose:
Map real customer objections to runtime architecture layers so future development stays aligned.

Price pressure → PHASE4_*_PRICE_PRESSURE → EDU_PPF_PRICE_GAP
Durability skepticism → PHASE4_*_DURABILITY_SKEPTICISM → EDU_PPF_DURABILITY_REALITY
Brand fixation → PHASE4_*_BRAND_FIXATION → EDU_PPF_INSTALL_QUALITY
Coverage confusion → PHASE3A_PPF_COVERAGE_INTENT → EDU_PPF_COVERAGE_LOGIC
Maintenance confusion → PHASE4_CERAMIC_MAINTENANCE_CONFUSION → EDU_CERAMIC_MAINTENANCE
Decision paralysis → PHASE5_*_NARROW → EDU_PROTECTION_PLAN_SIMPLIFIER
"""

if not os.path.exists(ledger_path):
    print("Ledger file not found.")
    exit()

with open(ledger_path, "r", encoding="utf-8") as f:
    content = f.read()

if block_header in content:
    print("OBJECTION MAP already exists — no changes made.")
else:
    content += "\n\n" + block
    with open(ledger_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("OBJECTION MAP inserted into ledger successfully.")

import os

path = "00__LOCKED__UPLOAD_SET/00__Runtime/RUNTIME_CHANGE_LEDGER.md"

section = """

## ARCHITECTURE GOVERNANCE ADDITION

Conversation Design Model introduced.

Framework includes:

- 4 customer behavior types
- 7 sales-driving questions
- 15 common objections
- 8 buying signals

Purpose:

Ensure Phase4 objection handling and Phase7 education snippets remain aligned with real automotive protection customer behavior.
"""

if not os.path.exists(path):
    print("File not found:", path)
    exit()

with open(path, encoding="utf-8") as f:
    content = f.read()

if "ARCHITECTURE GOVERNANCE ADDITION" in content:
    print("Entry already exists. No changes made.")
else:
    with open(path, "a", encoding="utf-8") as f:
        f.write("\n\n" + section)
    print("Architecture governance entry added to ledger.")

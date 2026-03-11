import os

path = "00__LOCKED__UPLOAD_SET/00__Runtime/PHRASE_GOVERNANCE_STANDARD.md"

section = """

## CONVERSATION ARCHITECTURE RULES

Customer Type Awareness

All phrases and education snippets must support the following behavioral profiles:

- Researcher
- Price Anchor
- Visual Buyer
- Convenience Buyer

Conversation Trap Prevention

Phrase design must avoid:

- Over-education (excessive explanation)
- Early price anchoring before scope clarity
- Defensive brand positioning

Education Snippet Compression

Education snippets must represent **concepts**, not individual questions.

Example:

Correct:
EDU_PRICE_GAP

Incorrect:
EDU_PPF_PRICE
EDU_WRAP_PRICE
EDU_TINT_PRICE

Target limit:

Total Phase7 education snippets < 20
"""

if not os.path.exists(path):
    print("File not found:", path)
    exit()

with open(path, encoding="utf-8") as f:
    content = f.read()

if "CONVERSATION ARCHITECTURE RULES" in content:
    print("Section already exists. No changes made.")
else:
    with open(path, "a", encoding="utf-8") as f:
        f.write("\n\n" + section)
    print("Conversation architecture rules added.")


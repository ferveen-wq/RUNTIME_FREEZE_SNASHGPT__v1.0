from pathlib import Path

file_path = Path("00__LOCKED__UPLOAD_SET/00__Runtime/PHRASE_GOVERNANCE_STANDARD.md")

content = file_path.read_text()

patch = """

====================================================
EDUCATION SNIPPET ARCHITECTURE
====================================================

Purpose:
Ensure education improves clarity without interrupting sales momentum.

Education snippets must follow this structure:

EXPLANATION
OPTIONAL_VISUAL_PROOF
RETURN_PROMPT

Rules:

1. Education Permission Gate
Education must be permission-based unless the customer explicitly asks for explanation.

Example:
"If you'd like, I can explain how that works."

2. Snippet Concept Rule
Education snippets must represent reusable concepts, not individual customer questions.

3. Snippet Compression
Maximum snippet target: <20.

4. Return Anchor Rule
Every education snippet must end with a RETURN_PROMPT that reconnects the conversation to the decision process.

Example:
"Would you prefer full protection or the front protection package?"

5. Education Trigger Matrix
All education snippets must be referenced inside:

EDUCATION_TRIGGER_MATRIX.md

This ensures:

• objections map to explanations
• phrases reference the same knowledge layer
• snippet duplication is prevented

"""

if "EDUCATION SNIPPET ARCHITECTURE" not in content:
    with open(file_path, "a") as f:
        f.write(patch)
    print("Education architecture added.")
else:
    print("Education architecture already exists.")

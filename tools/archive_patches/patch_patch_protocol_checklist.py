import os

path = "00__LOCKED__UPLOAD_SET/00__Runtime/PATCH_PROTOCOL.md"

section = """

## PATCH REVIEW CHECKLIST

Before approving any phrase or education snippet patch confirm:

✓ Does not introduce over-education  
✓ Does not introduce early price anchoring  
✓ Does not introduce defensive brand positioning  
✓ Does not exceed education snippet compression limits  
✓ Supports at least one defined customer type  
✓ Maps to existing objection framework  
✓ Maps to buying signal framework  
✓ Does not bypass phase routing logic
"""

if not os.path.exists(path):
    print("File not found:", path)
    exit()

with open(path, encoding="utf-8") as f:
    content = f.read()

if "PATCH REVIEW CHECKLIST" in content:
    print("Checklist already exists. No changes made.")
else:
    with open(path, "a", encoding="utf-8") as f:
        f.write("\n\n" + section)
    print("Patch checklist added.")


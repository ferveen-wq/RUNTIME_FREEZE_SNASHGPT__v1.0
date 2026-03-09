import os
import re

snippet_file = "00__LOCKED__UPLOAD_SET/00__Runtime/PHASE7_EDUCATION_SNIPPETS.md"

if not os.path.exists(snippet_file):
    print("Phase7 snippet file not yet created — skipping check.")
    exit(0)

with open(snippet_file, "r", encoding="utf-8") as f:
    content = f.read()

snippets = re.findall(r"### EDU_", content)

count = len(snippets)

print(f"Detected {count} education snippets.")

if count > 20:
    raise Exception("Education snippet compression rule violated (>20).")

print("Snippet compression check passed.")

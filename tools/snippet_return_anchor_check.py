import re
import os

file_path = "00__LOCKED__UPLOAD_SET/00__Runtime/PHASE7_EDUCATION_SNIPPETS.md"

if not os.path.exists(file_path):
    print("Phase7 snippet file not created yet.")
    exit(0)

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

snippets = re.split(r"### EDU_", content)[1:]

errors = []

for s in snippets:
    if "RETURN_PROMPT:" not in s:
        errors.append(s[:60])

if errors:
    raise Exception(
        f"{len(errors)} snippets missing RETURN_PROMPT anchor."
    )

print("Return anchor check passed.")

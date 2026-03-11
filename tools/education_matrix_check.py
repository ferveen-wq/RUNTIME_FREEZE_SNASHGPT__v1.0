import os
import re

matrix_file = "00__LOCKED__UPLOAD_SET/00__Runtime/EDUCATION_TRIGGER_MATRIX.md"
snippet_file = "00__LOCKED__UPLOAD_SET/00__Runtime/PHASE7_EDUCATION_SNIPPETS.md"

if not os.path.exists(snippet_file):
    print("Phase7 snippets not created yet.")
    exit(0)

if not os.path.exists(matrix_file):
    raise Exception("Education trigger matrix missing.")

with open(snippet_file) as f:
    snippets = re.findall(r"### (EDU_[A-Z_]+)", f.read())

with open(matrix_file) as f:
    matrix = f.read()

missing = []

for s in snippets:
    if s not in matrix:
        missing.append(s)

if missing:
    raise Exception(f"Snippets not mapped in matrix: {missing}")

print("Education trigger matrix check passed.")

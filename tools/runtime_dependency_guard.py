import os
import re

MANIFEST = "00__LOCKED__UPLOAD_SET/00__Runtime/RUNTIME_LOAD_MANIFEST.md"
ROOT = "00__LOCKED__UPLOAD_SET"

print("\nSNASHGPT RUNTIME DEPENDENCY CHECK\n")

missing = []

with open(MANIFEST, encoding="utf-8") as f:
    for line in f:
        match = re.search(r"([A-Za-z0-9_\/\-]+\.md)", line)
        if match:
            file = match.group(1)
            runtime_paths = [
                "",
                "00__LOCKED__UPLOAD_SET/00__Runtime/",
                "00__LOCKED__UPLOAD_SET/01__Engines/",
                "00__LOCKED__UPLOAD_SET/03__Parameters/",
                "00__LOCKED__UPLOAD_SET/02__Repositories/",
            ]

            found = False
            for base in runtime_paths:
                 if os.path.exists(base + file):
                     found = True
                     break

            if not found:
                missing.append(file)

            
                

if missing:
    print("Missing files referenced in manifest:\n")
    for m in missing:
        print("-", m)
else:
    print("All manifest dependencies resolved.")

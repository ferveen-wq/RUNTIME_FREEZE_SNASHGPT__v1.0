import os

manifest = "00__LOCKED__UPLOAD_SET/00__Runtime/RUNTIME_LOAD_MANIFEST.md"

if not os.path.exists(manifest):
    print("Manifest not found.")
    exit()

with open(manifest) as f:
    lines = f.readlines()

cleaned = []
removed = False

for line in lines:
    if "0.md" in line:
        print("Removing invalid reference:", line.strip())
        removed = True
        continue
    cleaned.append(line)

with open(manifest, "w") as f:
    f.writelines(cleaned)

if removed:
    print("\nManifest cleaned successfully.")
else:
    print("\nNo invalid reference found.")

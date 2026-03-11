import os

ROOT = "00__LOCKED__UPLOAD_SET"

MAX_RUNTIME_FILES = 40

runtime_files = []

for root, _dirs, files in os.walk(ROOT):
    for f in files:
        if f.endswith(".md"):
            runtime_files.append(os.path.join(root, f))

print("\nSNASHGPT FILE AUTHORITY CHECK\n")

print("Runtime file count:", len(runtime_files))

if len(runtime_files) > MAX_RUNTIME_FILES:
    print("⚠ WARNING: Runtime file count exceeds safe limit.")
    print("Consider consolidating architecture files.")
else:
    print("Runtime file count within safe limit.")

print("\nRule:")
print("Do not create new files unless a new authority is required.")

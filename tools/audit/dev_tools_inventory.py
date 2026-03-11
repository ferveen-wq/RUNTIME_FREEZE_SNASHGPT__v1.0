import os

folders = [
    "tools",
    "simulator",
    "runtime_guard",
    "database"
]

print("\nSNASHGPT DEVELOPMENT TOOLS INVENTORY\n")

for folder in folders:

    print(f"\n{folder.upper()}")
    print("-"*40)

    if not os.path.exists(folder):
        print("Folder not found")
        continue

    for root, _dirs, files in os.walk(folder):
        for f in files:
            path = os.path.join(root, f)
            print(path)

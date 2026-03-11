import os

ROOT = "00__LOCKED__UPLOAD_SET"

sections = {
    "Runtime": [],
    "Engines": [],
    "Parameters": [],
    "Repositories": [],
    "Playbooks": [],
    "Other": []
}

for root, _dirs, files in os.walk(ROOT):

    for f in files:
        if not f.endswith(".md"):
            continue

        path = os.path.join(root, f)

        if "/00__Runtime/" in path:
            sections["Runtime"].append(path)

        elif "/01__Engines/" in path:
            sections["Engines"].append(path)

        elif "/03__Parameters/" in path:
            sections["Parameters"].append(path)

        elif "/02__Repositories/" in path:
            sections["Repositories"].append(path)

        elif "/03__Playbooks/" in path:
            sections["Playbooks"].append(path)

        else:
            sections["Other"].append(path)


print("\nSNASHGPT FULL ARCHITECTURE GRAPH\n")

for k,v in sections.items():

    print("\n" + k.upper())
    print("-"*40)

    for f in v:
        print(f)

    print("\nCOUNT:", len(v))

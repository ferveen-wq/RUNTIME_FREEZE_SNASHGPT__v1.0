import os

ROOT = "00__LOCKED__UPLOAD_SET/00__Runtime"

keywords = [
"RULE",
"GOVERNANCE",
"MANDATORY",
"MUST",
"DO NOT",
"PROHIBITED"
]

print("\nSNASHGPT GOVERNANCE SCAN\n")

for root, _dirs, files in os.walk(ROOT):

    for f in files:

        if not f.endswith(".md"):
            continue

        path = os.path.join(root, f)

        with open(path) as file:

            content = file.read()

        for k in keywords:

            if k in content:

                print(path)
                break

import os

ROOT = "00__LOCKED__UPLOAD_SET"

runtime_files = []
engine_files = []
parameter_files = []
other_files = []

for root, _dirs, files in os.walk(ROOT):
    for f in files:
        if not f.endswith(".md"):
            continue

        path = os.path.join(root, f)

        if "Runtime" in root:
            runtime_files.append(path)

        elif "Engines" in root:
            engine_files.append(path)

        elif "Parameters" in root:
            parameter_files.append(path)

        else:
            other_files.append(path)

print("\nSNASHGPT RUNTIME ARCHITECTURE MAP\n")

print("RUNTIME FILES")
print("----------------")
for f in runtime_files:
    print(f)

print("\nENGINE FILES")
print("----------------")
for f in engine_files:
    print(f)

print("\nPARAMETER FILES")
print("----------------")
for f in parameter_files:
    print(f)

print("\nOTHER FILES")
print("----------------")
for f in other_files:
    print(f)

print("\nSUMMARY")
print("----------------")
print("Runtime files:", len(runtime_files))
print("Engine files:", len(engine_files))
print("Parameter files:", len(parameter_files))
print("Other files:", len(other_files))

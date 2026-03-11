import os
import re

RUNTIME_DIR = "00__LOCKED__UPLOAD_SET/00__Runtime"
ENGINES_DIR = "00__LOCKED__UPLOAD_SET/01__Engines"

manifest_file = os.path.join(RUNTIME_DIR, "RUNTIME_LOAD_MANIFEST.md")
phrase_library = os.path.join(RUNTIME_DIR, "PHASE4_6_HUMAN_PHRASE_LIBRARY.md")
assembly_map = os.path.join(RUNTIME_DIR, "PHASE4_8_MESSAGE_ASSEMBLY_MAP.md")


def read_file(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def check_manifest_files():
    print("\nCHECK 1 — Manifest File Existence")

    manifest = read_file(manifest_file)
    files = re.findall(r'([A-Z0-9_]+\.md)', manifest)

    missing = []

    for f in files:
        runtime_path = os.path.join(RUNTIME_DIR, f)
        engine_path = os.path.join(ENGINES_DIR, f)

        if not os.path.exists(runtime_path) and not os.path.exists(engine_path):
            missing.append(f)

    if missing:
        print("Missing files referenced in manifest:")
        for m in missing:
            print("  -", m)
    else:
        print("OK")


def check_phrase_routing():
    print("\nCHECK 2 — Phrase Routing Integrity")

    assembly = read_file(assembly_map)
    phrases = read_file(phrase_library)

    ids = re.findall(r'→ ([A-Z0-9_ ]+)', assembly)

    missing = []

    for i in ids:
        if i.strip() not in phrases:
            missing.append(i)

    if missing:
        print("Routing references missing phrases:")
        for m in missing:
            print("  -", m)
    else:
        print("OK")


def check_engine_presence():
    print("\nCHECK 3 — Engine Presence")

    required = [
        "QUALIFICATION_ENGINE.md",
        "NEGOTIATION_LOGIC_MODULE.md",
        "PRICE_LADDER_ENGINE.md",
        "OBJECTION_RESOLUTION_ENGINE.md",
        "SILENCE_HANDLING_ENGINE.md"
    ]

    missing = []

    for e in required:
        path = os.path.join(ENGINES_DIR, e)
        if not os.path.exists(path):
            missing.append(e)

    if missing:
        print("Missing engines:")
        for m in missing:
            print("  -", m)
    else:
        print("OK")


def main():
    print("\nSNASHGPT RUNTIME INTEGRITY CHECK")

    check_manifest_files()
    check_phrase_routing()
    check_engine_presence()

    print("\nIntegrity check complete\n")


if __name__ == "__main__":
    main()

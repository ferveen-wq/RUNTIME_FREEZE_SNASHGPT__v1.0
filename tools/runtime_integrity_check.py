import os
import re
from collections import OrderedDict

BASE_DIR = "00__LOCKED__UPLOAD_SET"
RUNTIME_DIR = os.path.join(BASE_DIR, "00__Runtime")
ENGINES_DIR = os.path.join(BASE_DIR, "01__Engines")
REPOS_DIR = os.path.join(BASE_DIR, "02__Repositories")
PARAMS_DIR = os.path.join(BASE_DIR, "03__Parameters")
PLAYBOOKS_DIR = os.path.join(BASE_DIR, "03__Playbooks")

SEARCH_DIRS = [
    RUNTIME_DIR,
    ENGINES_DIR,
    REPOS_DIR,
    PARAMS_DIR,
    PLAYBOOKS_DIR,
]

manifest_file = os.path.join(RUNTIME_DIR, "RUNTIME_LOAD_MANIFEST.md")
phrase_library = os.path.join(RUNTIME_DIR, "PHASE4_6_HUMAN_PHRASE_LIBRARY.md")
assembly_map = os.path.join(RUNTIME_DIR, "PHASE4_8_MESSAGE_ASSEMBLY_MAP.md")


def read_file(path: str) -> str:
    with open(path, encoding="utf-8") as f:
        return f.read()


def dedupe_keep_order(items):
    return list(OrderedDict.fromkeys(items))


def build_file_index():
    index = {}
    for base in SEARCH_DIRS:
        if not os.path.isdir(base):
            continue
        for root, _, files in os.walk(base):
            for name in files:
                index.setdefault(name, []).append(os.path.join(root, name))
    return index


def check_manifest_files(file_index):
    print("\nCHECK 1 — Manifest File Existence")

    manifest = read_file(manifest_file)
    files = re.findall(r'\b([A-Z][A-Z0-9_.-]*\.md)\b', manifest)
    files = dedupe_keep_order(files)

    missing = []
    for fname in files:
        if fname == "RUNTIME_LOAD_MANIFEST.md":
            continue
        if fname not in file_index:
            missing.append(fname)

    if missing:
        print("Missing files referenced in manifest:")
        for m in missing:
            print("  -", m)
    else:
        print("OK")


def extract_candidate_phrase_ids(assembly: str):
    candidates = []

    # 1) selected_phrase_id: SOME_ID
    candidates += re.findall(r'selected_phrase_id:\s*"?([A-Z0-9_.()\- ][A-Z0-9_.()\- ]+?)"?\s*(?:\n|$)', assembly)

    # 2) selected_phrase_id MUST equal SOME_ID
    candidates += re.findall(r'selected_phrase_id MUST equal:?\s*"?([A-Z0-9_.()\- ][A-Z0-9_.()\- ]+?)"?\s*(?:\n|$)', assembly)

    # 3) Use ONLY / Output MUST use ONLY ... → PHRASE_ID
    candidates += re.findall(r'→\s*([A-Z][A-Z0-9_.()\- ]{2,})\s*(?:\n|$)', assembly)

    cleaned = []
    for item in candidates:
        phrase_id = item.strip().strip('"').strip("'")

        if not phrase_id:
            continue
        if phrase_id.endswith(".md"):
            continue

        # Ignore obvious placeholders or file bundle references
        if phrase_id.startswith("PHASE6__SERVICE_CANON_BUNDLE"):
            continue
        if phrase_id.startswith("OPTIONAL_"):
            continue
        if phrase_id.startswith("VIDEO_PROOF_"):
            continue
        if phrase_id in {"H1", "GRAPHENE", "INTERIOR_CERAMIC", "FOLLOW_UP_QUESTION"}:
            continue

        # Ignore descriptive route labels that are not actual phrase IDs
        if phrase_id.startswith("L.0 "):
            continue
        if phrase_id.startswith("L.2 "):
            continue
        if phrase_id.startswith("L.6 "):
            continue
        if phrase_id.startswith("B ("):
            continue
        if phrase_id.startswith("L ("):
            continue
        if phrase_id.startswith("G ("):
            continue

        cleaned.append(phrase_id)

    return dedupe_keep_order(cleaned)


def check_phrase_routing():
    print("\nCHECK 2 — Phrase Routing Integrity")

    assembly = read_file(assembly_map)
    phrases = read_file(phrase_library)

    ids = extract_candidate_phrase_ids(assembly)

    missing = []
    for phrase_id in ids:
        if phrase_id not in phrases:
            missing.append(phrase_id)

    if missing:
        print("Routing references missing phrases:")
        for m in missing:
            print("  -", m)
    else:
        print("OK")


def check_engine_presence(file_index):
    print("\nCHECK 3 — Engine Presence")

    required = [
        "QUALIFICATION_ENGINE.md",
        "NEGOTIATION_LOGIC_MODULE.md",
        "PRICE_LADDER_ENGINE.md",
        "OBJECTION_RESOLUTION_ENGINE.md",
        "SILENCE_HANDLING_ENGINE.md",
    ]

    missing = [name for name in required if name not in file_index]

    if missing:
        print("Missing engines:")
        for m in missing:
            print("  -", m)
    else:
        print("OK")


def main():
    print("\nSNASHGPT RUNTIME INTEGRITY CHECK")

    for required_path in (manifest_file, phrase_library, assembly_map):
        if not os.path.exists(required_path):
            raise SystemExit(f"Required file not found: {required_path}")

    file_index = build_file_index()

    check_manifest_files(file_index)
    check_phrase_routing()
    check_engine_presence(file_index)

    print("\nIntegrity check complete\n")


if __name__ == "__main__":
    main()

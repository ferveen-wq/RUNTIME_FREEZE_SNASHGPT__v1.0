#!/usr/bin/env python3

import sys
from pathlib import Path

ROOTS = [
    "00__ACTIVE_ROLLOUT_UPLOAD_SET",
    "00__LOCKED__UPLOAD_SET",
]

IGNORE = [
    ".bak",
    "deprecated",
    "tmp",
    "archive",
]

def is_ignored(path):
    return any(x in str(path).lower() for x in IGNORE)

def scan(term):
    results = []

    for root in ROOTS:
        base = Path(root)
        if not base.exists():
            continue

        for p in base.rglob("*.md"):
            if is_ignored(p):
                continue

            try:
                text = p.read_text(encoding="utf-8", errors="ignore")
            except:
                continue

            if term in text:
                lines = []
                for i, line in enumerate(text.splitlines(), 1):
                    if term in line:
                        lines.append((i, line.strip()))
                results.append((p, lines))

    return results


def classify(line):
    l = line.lower()
    if "set " in l or "set_" in l:
        return "WRITE"
    if "if " in l or "==" in l:
        return "READ"
    return "OTHER"


def main():
    if len(sys.argv) < 2:
        print("Usage: owner_map.py <TERM1> [TERM2 ...]")
        return

    terms = sys.argv[1:]

    for term in terms:
        print(f"\n===== TERM: {term} =====")

        results = scan(term)

        if not results:
            print("No matches found.")
            continue

        writers = []
        readers = []

        for path, lines in results:
            for _, content in lines:
                role = classify(content)
                if role == "WRITE":
                    writers.append(str(path))
                elif role == "READ":
                    readers.append(str(path))

        print("\n--- SUMMARY ---")
        print("Writers:")
        for w in sorted(set(writers)):
            print("  -", w)

        print("Readers:")
        for r in sorted(set(readers)):
            print("  -", r)

        print("\n--- DETAILS ---")

        for path, lines in results:
            print(f"\nFILE: {path}")

            for ln, content in lines[:5]:
                role = classify(content)
                print(f"  [{role}] L{ln}: {content}")


if __name__ == "__main__":
    main()

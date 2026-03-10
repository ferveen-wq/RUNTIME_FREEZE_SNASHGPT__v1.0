#!/usr/bin/env python3

import sys
from pathlib import Path

INDEX = Path("00__LOCKED__UPLOAD_SET/00__Runtime/PHRASE_INDEX.md")

def parse_index():
    service = None
    role = None
    trigger = None

    seen = {}
    conflicts = []

    for line in INDEX.read_text().splitlines():
        line = line.strip()

        if line.startswith("SERVICE:"):
            service = line.split(":",1)[1].strip()

        if line.startswith("ROLE:"):
            role = line.split(":",1)[1].strip()

        if line.startswith("TRIGGER:"):
            trigger = line.split(":",1)[1].strip()

            key = (service, role, trigger)

            if key in seen:
                conflicts.append(key)
            else:
                seen[key] = True

    return conflicts


def main():
    if not INDEX.exists():
        return 0

    conflicts = parse_index()

    if conflicts:
        print("\nPhrase Trigger Conflict detected:\n")
        for c in conflicts:
            print(f"SERVICE={c[0]} ROLE={c[1]} TRIGGER={c[2]}")
        print("\nResolve duplicate triggers before committing.\n")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())

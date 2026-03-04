from __future__ import annotations

import argparse
import re
from pathlib import Path

PRICE_UPDATES = {
    # PPF
    "GLOBAL_LUXE_5Y": (550, 630, 730),
    "GLOBAL_ELITE_8Y": (750, 790, 890),
    "GLOBAL_SIGNATURE_10Y": (800, 880, 990),
    "XPEL_EXO_7Y": (920, 1040, 1100),
    "XPEL_UP_10Y": (1320, 1340, 1400),
    "XPEL_FUSION_10Y": (1420, 1440, 1500),
    "XPEL_UP10_10Y": (1780, 1840, 1900),
    "GLOBAL_MATTE_10Y": (840, 920, 990),
    "XPEL_STEALTH_10Y": (1360, 1460, 1520),
    "PPF_FRONT_GLOBAL": (300, 295, 295),

    # CERAMIC
    "CERAMIC_1Y": (90, 100, 120),
    "CERAMIC_3Y": (120, 130, 150),
    "CERAMIC_5Y": (160, 170, 190),

    # GRAPHENE
    "GRAPHENE_1Y": (110, 120, 140),
    "GRAPHENE_3Y": (140, 150, 170),
    "GRAPHENE_5Y": (180, 190, 210),

    # INTERIOR (YOUR SHEET VALUES)
    "INTERIOR_CERAMIC": (35, 40, 50),

    # TINT
    "TINT_NANO_CERAMIC": (80, 110, 110),
    "TINT_XPEL_XR_PLUS": (180, 220, 220),

    # POLISHING
    "POLISH_SILVER": (45, 50, 55),
    "POLISH_GOLD": (70, 85, 95),

    # WRAP
    "ROOF_WRAP_BLACK": (60, 90, 130),
    "WRAP_GLOSS": (700, 750, 800),
    "WRAP_MATTE": (700, 750, 800),
    "WRAP_SATIN": (700, 750, 800),
}

DEFAULT_TARGETS = [
    Path("02__Parameters/PRICE_TABLE_VAT_INCL.md"),
    Path("00__LOCKED__UPLOAD_SET/03__Parameters/PRICE_TABLE_VAT_INCL.md"),
]

ROW_RE = re.compile(r"^\|\s*([A-Z0-9_]+)\s*\|.*\|\s*$")

def format_row(sku: str, v1: int, v2: int, v3: int) -> str:
    return f"| {sku} | {v1} | {v2} | {v3} |\n"

def patch_file(path: Path, dry_run: bool = False) -> int:
    if not path.exists():
        print(f"SKIP (missing): {path}")
        return 0

    original = path.read_text(encoding="utf-8")
    lines = original.splitlines(keepends=True)

    changed = 0
    new_lines = []

    for line in lines:
        m = ROW_RE.match(line)
        if not m:
            new_lines.append(line)
            continue

        sku = m.group(1)
        if sku not in PRICE_UPDATES:
            new_lines.append(line)
            continue

        v1, v2, v3 = PRICE_UPDATES[sku]
        new_line = format_row(sku, v1, v2, v3)
        if new_line != line:
            changed += 1
            new_lines.append(new_line)
        else:
            new_lines.append(line)

    if changed and not dry_run:
        path.write_text("".join(new_lines), encoding="utf-8")

    print(f"OK: {path} (rows changed: {changed})")
    return changed

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--targets", nargs="*", default=None)
    args = ap.parse_args()

    targets = DEFAULT_TARGETS if args.targets is None else [Path(t) for t in args.targets]
    total = 0
    for t in targets:
        total += patch_file(t, dry_run=args.dry_run)

    print(f"\n{'DRY RUN' if args.dry_run else 'PATCH'} complete. Total rows changed: {total}")

if __name__ == "__main__":
    main()

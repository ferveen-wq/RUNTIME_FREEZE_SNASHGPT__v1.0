from collections import Counter
from pathlib import Path

FILE = "00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_6_HUMAN_PHRASE_LIBRARY.md"

print("\n=== PHRASE COVERAGE HEATMAP ===\n")

text = Path(FILE).read_text(encoding="utf-8").lower()

services = {
    "ppf": ["ppf", "paint protection"],
    "tint": ["tint", "window tint"],
    "wrap": ["wrap", "color change"],
    "ceramic": ["ceramic"],
    "polish": ["polish", "paint correction"]
}

phase_markers = [
    "phase3a",
    "phase3b",
    "phase4",
    "phase5"
]

service_counts = Counter()
phase_counts = Counter()

for service, keywords in services.items():
    for k in keywords:
        service_counts[service] += text.count(k)

for phase in phase_markers:
    phase_counts[phase] = text.count(phase)

print("SERVICE COVERAGE\n")

for s, c in service_counts.items():
    bar = "█" * (c // 10 + 1)
    print(f"{s.upper():8} {bar} ({c})")

print("\nPHASE COVERAGE\n")

for p, c in phase_counts.items():
    bar = "█" * (c // 5 + 1)
    print(f"{p.upper():8} {bar} ({c})")

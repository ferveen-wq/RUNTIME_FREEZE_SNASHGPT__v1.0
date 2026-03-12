import sys
from pathlib import Path

BACKLOG = Path("00__CONTROL_TOWER/IDEA_BACKLOG.md")

idea = " ".join(sys.argv[1:])

text = BACKLOG.read_text()

if idea not in text:
    print("Idea not found in backlog.")
    exit()

text = text.replace(f"[ ] {idea}", f"[x] {idea}")

BACKLOG.write_text(text)

print("Idea marked as DONE.")

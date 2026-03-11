import datetime
import subprocess
import sys

idea_text = " ".join(sys.argv[1:])

if not idea_text:
    print("Usage: python tools/capture_idea.py \"idea description\"")
    exit()

file_path = "00__CONTROL_TOWER/IDEA_BACKLOG.md"

timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

entry = f"\n### {timestamp}\n{idea_text}\n"

with open(file_path, "a") as f:
    f.write(entry)

print("\nIdea captured in IDEA_BACKLOG.md")

subprocess.run(["git", "add", file_path])
subprocess.run(["git", "commit", "-m", f"control tower: idea captured - {idea_text[:50]}"])
subprocess.run(["git", "push", "origin", "main"])

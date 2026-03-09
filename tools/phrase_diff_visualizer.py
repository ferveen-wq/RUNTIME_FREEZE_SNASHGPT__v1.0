from pathlib import Path
import subprocess

PHRASE_FILE = "00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_6_HUMAN_PHRASE_LIBRARY.md"

print("\n=== PHRASE DIFF VISUALIZATION ===\n")

try:
    diff = subprocess.check_output(
        ["git", "diff", "HEAD~1", "HEAD", "--", PHRASE_FILE],
        stderr=subprocess.DEVNULL
    ).decode("utf-8")

    if diff.strip():
        print(diff)
    else:
        print("No phrase changes detected in last commit.")

except Exception:
    print("Diff unavailable (likely first commit or shallow clone).")

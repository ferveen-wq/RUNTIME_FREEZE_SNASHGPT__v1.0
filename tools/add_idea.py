import datetime
import subprocess
import sys

BACKLOG_FILE = "00__CONTROL_TOWER/IDEA_BACKLOG.md"

def add_idea(text):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    entry = f"""

IDEA AUTO
---------

Timestamp:
{timestamp}

Description:
{text}

Status:
IDEA

"""

    with open(BACKLOG_FILE, "a") as f:
        f.write(entry)

    print("Idea added to backlog.")

    subprocess.run(["git", "add", BACKLOG_FILE])
    subprocess.run(["git", "commit", "-m", f"idea: {text[:40]}"])
    subprocess.run(["git", "push", "origin", "main"])


if __name__ == "__main__":
    idea = " ".join(sys.argv[1:])
    add_idea(idea)

import os
import subprocess
import sys

PATCH_DIR = "tools"


def run(cmd):
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        sys.exit(result.returncode)


def main():

    if len(sys.argv) < 2:
        print("Usage: python runner/apply_patch.py <patch_file>")
        sys.exit(1)

    patch_name = sys.argv[1]

    patch_path = os.path.join(PATCH_DIR, patch_name)

    if not os.path.exists(patch_path):
        print(f"Patch not found: {patch_path}")
        sys.exit(1)

    print("\n=== APPLYING PATCH ===\n")

    run(f"python {patch_path}")

    print("\n=== RUNNING GOVERNANCE ===\n")

    run("python tools/conversation_governance_check.py")
    run("python tools/phrase_risk_audit.py")
    run("python tools/runtime_guardian.py")

    print("\n=== COMMITTING PATCH ===\n")

    run("git add .")
    run(f'git commit -m "patch: {patch_name}"')

    print("\n=== PUSHING PATCH ===\n")

    run("git push origin main")

    print("\nPatch applied successfully.\n")


if __name__ == "__main__":
    main()

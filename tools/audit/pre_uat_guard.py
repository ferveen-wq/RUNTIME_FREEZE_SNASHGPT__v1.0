import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

def run(cmd):
    return subprocess.run(
        cmd,
        cwd=ROOT,
        text=True,
        capture_output=True,
    )

def fail(msg):
    print(f"[FAIL] {msg}")
    sys.exit(1)

def main():
    print("===== PRE-UAT GUARD =====")

    health = run(["python3", "tools/audit/runner_health_check.py"])
    print(health.stdout.strip())
    if health.returncode != 0:
        print(health.stderr.strip())
        fail("runner health check failed")

    prompt = ROOT / "runner" / "context_reset_prompt_active.txt"
    prompt_text = prompt.read_text(encoding="utf-8")

    forbidden_active_prompt_patterns = [
        "selected_phrase_id MUST equal ESCALATION_BLOCK_WRAP_QUOTE",
        "Approved handoff behavior for WRAP MUST reuse ESCALATION BLOCK",
        "QUALIFICATION_STATUS MUST equal READY_FOR_NEGOTIATION",
    ]

    for pattern in forbidden_active_prompt_patterns:
        if pattern in prompt_text:
            fail(f"active context reset prompt contains stale override: {pattern}")

    print("[OK] active context reset prompt has no known stale wrap override")

    status = run(["git", "status", "--short"])
    dirty_lines = [ln for ln in status.stdout.splitlines() if ln.strip()]
    if dirty_lines:
        print("\n[WARN] uncommitted files present:")
        for ln in dirty_lines:
            print(ln)
        print("[INFO] Continue only if these changes are intentional for this UAT.")

    print("\n===== UAT CASE READINESS CHECK =====")
    readiness = run(["python3", "tools/audit/pre_uat_case_readiness_check.py"])
    print(readiness.stdout.strip())
    if readiness.returncode != 0:
        print(readiness.stderr.strip())
        fail("UAT case readiness check failed")

    print("\n[OK] Pre-UAT guard passed.")

if __name__ == "__main__":
    main()

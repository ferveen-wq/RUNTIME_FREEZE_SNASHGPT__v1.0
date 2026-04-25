from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]

def fail(msg):
    print(f"[FAIL] {msg}")
    sys.exit(1)

def ok(msg):
    print(f"[OK] {msg}")

def contains(path, text):
    return text in path.read_text(encoding="utf-8", errors="ignore")

def main():
    print("===== ACTIVE ROLLOUT GUARD =====")

    active_runtime = ROOT / "00__ACTIVE_ROLLOUT_UPLOAD_SET" / "00__Runtime"
    active_uat = ROOT / "tests" / "active_rollout_uat"
    raw_runner = ROOT / "runner" / "run_active_uat_raw.py"
    active_prompt = ROOT / "runner" / "context_reset_prompt_active.txt"
    controlled = ROOT / "tools" / "audit" / "run_active_uat_controlled.sh"
    owner_map = ROOT / "tools" / "audit" / "owner_map.py"

    for p in [active_runtime, active_uat]:
        if not p.exists() or not p.is_dir():
            fail(f"missing active directory: {p}")
        ok(f"active directory exists: {p.relative_to(ROOT)}")

    for p in [raw_runner, active_prompt, controlled, owner_map]:
        if not p.exists() or not p.is_file():
            fail(f"missing required active file: {p}")
        ok(f"required file exists: {p.relative_to(ROOT)}")

    checks = [
        (raw_runner, '00__ACTIVE_ROLLOUT_UPLOAD_SET', "raw runner loads active rollout runtime"),
        (raw_runner, 'context_reset_prompt_active.txt', "raw runner uses active context prompt"),
        (controlled, 'tools/audit/pre_uat_guard.py', "controlled wrapper calls pre_uat_guard"),
        (controlled, 'runner/run_active_uat_raw.py', "controlled wrapper calls raw active runner"),
        (controlled, 'tools/audit/report_analyzer.py', "controlled wrapper calls report_analyzer"),
        (controlled, 'tests/active_rollout_uat/*', "controlled wrapper enforces active UAT folder"),
        (owner_map, 'ROOTS = ["00__ACTIVE_ROLLOUT_UPLOAD_SET"]', "owner_map defaults active-only"),
    ]

    for path, token, label in checks:
        if not contains(path, token):
            fail(label)
        ok(label)

    prompt_text = active_prompt.read_text(encoding="utf-8", errors="ignore")
    forbidden = [
        "HARD OVERRIDE",
        "selected_phrase_id MUST equal PHASE3B",
        "QUALIFICATION_STATUS MUST be READY_FOR_NEGOTIATION",
    ]

    for token in forbidden:
        if token in prompt_text:
            fail(f"active prompt contains business override: {token}")

    ok("active prompt has no known business overrides")
    print("\n[OK] Active rollout guard passed.")

if __name__ == "__main__":
    main()

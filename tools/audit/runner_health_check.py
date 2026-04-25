from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
RAW_RUNNER = ROOT / "runner" / "run_active_uat_raw.py"

def main():
    text = RAW_RUNNER.read_text(encoding="utf-8")
    failed = False

    print(f"===== RAW RUNNER HEALTH CHECK: {RAW_RUNNER} =====")

    required = {
        "supports turns": 'if "turns" in case:',
        "extracts debug": "parsed = extract_debug_and_messages(text)",
    }

    for label, snippet in required.items():
        ok = snippet in text
        print(f"{label}: {'OK' if ok else 'FAIL'}")
        if not ok:
            failed = True

    appends_assistant = (
        "conversation.append(" in text
        and '"role": "assistant"' in text
        and '"content":' in text
    )
    print(f"appends assistant output: {'OK' if appends_assistant else 'FAIL'}")
    if not appends_assistant:
        failed = True

    state_markers = [
        "STATE_SNAPSHOT",
        "PREVIOUS_TURN_DEBUG",
        "previous_turn.selected_phrase_id",
        "json.dumps(parsed[\"debug\"]",
        "json.dumps(parsed.get(\"debug\"",
    ]

    has_state_marker = any(marker in text for marker in state_markers)
    print(f"explicit next-turn state preservation: {'OK' if has_state_marker else 'FAIL'}")

    bad_report_only_marker = '"debug": parsed["debug"]' in text
    if bad_report_only_marker and not has_state_marker:
        print("report-only debug storage detected: OK for reports, NOT enough for multi-turn continuity")

    if not has_state_marker:
        print("\n[FAIL] Raw runner does not explicitly inject parsed debug/state into assistant content for next turn.")
        print("Multi-turn raw UAT is not trusted until fixed.")
        failed = True

    if failed:
        sys.exit(1)

    print("\n[OK] Raw runner health check passed.")

if __name__ == "__main__":
    main()

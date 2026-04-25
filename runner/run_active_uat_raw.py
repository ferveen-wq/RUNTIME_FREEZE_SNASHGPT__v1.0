import os
import sys
import json
import time
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
from openai import OpenAI

ROOT = Path(__file__).resolve().parents[1]
REPORTS_DIR = ROOT / "tests/reports"

MODEL = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

def load_json(p):
    return json.loads(Path(p).read_text(encoding="utf-8"))

ACTIVE_RUNTIME_DIR = ROOT / "00__ACTIVE_ROLLOUT_UPLOAD_SET" / "00__Runtime"

RUNTIME_FILES = [
    "RUNTIME_LOAD_MANIFEST.md",
    "KNOWLEDGE__RUNTIME_CORE_BUNDLE.md",
    "PHASE0_LOCK_INDEX.md",
    "PHASE0_2_LOCK_INDEX.md",
    "GLOBAL_PRODUCT_NAMING_REGISTRY_v1.0.md",
    "PRODUCT_SERVICE_CANON.md",
    "CUSTOMER_CHAT_INTAKE_RULES.md",
    "GLOBAL_VEHICLE_CLASSIFICATION_REPOSITORY.md",
    "RUNTIME_EXECUTION_FLOW.md",
    "RUNTIME_STATE_MACHINE.md",
    "PHASE3_ORCHESTRATION_WIRING_ADDENDUM.md",
    "GLOBAL_CORE_CONTEXT_PARAMETERS.md",
    "CONVERSATION_DYNAMIC_PARAMETERS.md",
    "QUALIFICATION_ENGINE.md",
    "PHASE3A_QUALIFICATION_DECISION_MATRIX.md",
    "PHASE4_6_HUMAN_PHRASE_LIBRARY.md",
    "PHASE4_8_MESSAGE_ASSEMBLY_MAP.md",
    "OUTPUT_RESPONSE_TEMPLATE.md",
]
def load_system_prompt():
    base_prompt_path = ROOT / "runner/context_reset_prompt.txt"
    base = base_prompt_path.read_text(encoding="utf-8").strip()

    runtime_parts = []
    for name in RUNTIME_FILES:
        fp = ACTIVE_RUNTIME_DIR / name
        if not fp.exists():
            raise SystemExit(f"Missing active runtime file: {fp}")
        runtime_parts.append(f"\\n\\n===== ACTIVE_RUNTIME_FILE: {name} =====\\n" + fp.read_text(encoding="utf-8").strip())

    runtime_bundle = "\\n".join(runtime_parts)

    now_bh = datetime.now(ZoneInfo("Asia/Bahrain")).strftime("%Y-%m-%d %H:%M")
    injected = (
        f"CURRENT_BAHRAIN_TIME: {now_bh} (Asia/Bahrain)\\n\\n"
        "ACTIVE ROLLOUT RUNTIME BUNDLE IS THE ONLY AUTHORITY FOR THIS TEST.\\n"
        "Do not rely on external project instructions or legacy runner assumptions.\\n"
        + runtime_bundle
        + "\\n\\n"
    )

    return base.replace("Begin.", injected + "Begin.")

def extract_debug_and_messages(text):
    debug = {}
    arabic = ""
    english = ""

    lines = text.splitlines()

    for ln in lines:
        if ln.startswith("phase:"):
            debug["phase"] = ln.split(":",1)[1].strip()
        elif ln.startswith("request_type:"):
            debug["request_type"] = ln.split(":",1)[1].strip()
        elif ln.startswith("selected_phrase_id:"):
            debug["selected_phrase_id"] = ln.split(":",1)[1].strip()
        elif ln.startswith("QUALIFICATION_STATUS:"):
            debug["QUALIFICATION_STATUS"] = ln.split(":",1)[1].strip()
        elif ln.startswith("price_ladder_state:"):
            debug["price_ladder_state"] = ln.split(":",1)[1].strip()
        elif ln.startswith("service_intent:"):
            debug["service_intent"] = ln.split(":",1)[1].strip()
        elif ln.startswith("active_service_context:"):
            debug["active_service_context"] = ln.split(":",1)[1].strip()
        elif ln.startswith("missing_fields:"):
            debug["missing_fields"] = ln.split(":",1)[1].strip()
        elif ln.startswith("phase3a_required:"):
            debug["phase3a_required"] = ln.split(":",1)[1].strip()
        elif ln.startswith("phase3a_complete:"):
            debug["phase3a_complete"] = ln.split(":",1)[1].strip()
        elif ln.startswith("phase3a_qualifier_id:"):
            debug["phase3a_qualifier_id"] = ln.split(":",1)[1].strip()

    parts = text.split("\n\n")
    if len(parts) >= 2:
        arabic = parts[-2].strip()
        english = parts[-1].strip()

    return {
        "debug": debug,
        "arabic": arabic,
        "english": english,
        "raw": text
    }

def validate_cases(cases):
    weak = []
    for case in cases:
        exp_debug = case.get("expect_debug", {}) or {}
        has_phase = "phase" in exp_debug
        has_status = "QUALIFICATION_STATUS" in exp_debug
        has_phrase = (
            "expect_selected_phrase_id" in case
            or "expect_not_selected_phrase_id" in case
        )
        if not (has_phase and has_status and has_phrase):
            weak.append(case.get("case_id", "<missing case_id>"))

    if weak:
        raise SystemExit(
            "Raw active UAT requires strict expectations "
            "(phase, QUALIFICATION_STATUS, selected phrase expectation). "
            f"Weak cases: {weak}"
        )


def check_expectations(parsed, case):
    failures = []
    debug = parsed["debug"]

    # Required checks
    exp_debug = case.get("expect_debug", {})
    for k, v in exp_debug.items():
        if str(debug.get(k)) != str(v):
            failures.append(f"{k} expected {v} got {debug.get(k)}")

    exp_sel = case.get("expect_selected_phrase_id")
    if exp_sel and debug.get("selected_phrase_id") != exp_sel:
        failures.append(f"selected_phrase_id expected {exp_sel} got {debug.get('selected_phrase_id')}")

    exp_not_sel = case.get("expect_not_selected_phrase_id")
    if exp_not_sel and debug.get("selected_phrase_id") == exp_not_sel:
        failures.append(f"selected_phrase_id forbidden {exp_not_sel}")

    selected = str(debug.get("selected_phrase_id", "")).strip()
    q_status = str(debug.get("QUALIFICATION_STATUS", "")).strip()
    ladder_state = str(debug.get("price_ladder_state", "")).strip()

    if selected.startswith("PHASE3B_") and q_status != "READY_FOR_NEGOTIATION":
        failures.append(f"CONTRADICTION: {selected} with {q_status}")

    if ladder_state.upper() in {"INITIAL", "FINAL", "FINAL_PRICE_REACHED"} and q_status != "READY_FOR_NEGOTIATION":
        failures.append(f"CONTRADICTION: price ladder used while {q_status}")

    return failures

def main():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise SystemExit("OPENAI_API_KEY not set")

    client = OpenAI(api_key=api_key)
    system_prompt = load_system_prompt()

    cases_file = os.getenv("UAT_CASES_FILE")
    if not cases_file:
        raise SystemExit("UAT_CASES_FILE not set")

    cases = load_json(cases_file)

    case_id_filter = os.getenv("CASE_ID", "").strip()
    if case_id_filter:
        cases = [c for c in cases if str(c.get("case_id", "")).strip() == case_id_filter]
        if not cases:
            raise SystemExit(f"CASE_ID not found in case file: {case_id_filter}")

    max_cases = os.getenv("MAX_CASES", "").strip()
    if max_cases:
        try:
            max_n = int(max_cases)
        except ValueError:
            raise SystemExit(f"MAX_CASES must be an integer, got: {max_cases}")
        if max_n < 1:
            raise SystemExit("MAX_CASES must be >= 1")
        cases = cases[:max_n]

    validate_cases(cases)

    print(f"RAW UAT case count: {len(cases)}")
    print(f"RAW UAT cases file: {cases_file}")
    if case_id_filter:
        print(f"RAW UAT CASE_ID filter: {case_id_filter}")
    if max_cases:
        print(f"RAW UAT MAX_CASES: {max_cases}")

    if len(cases) > 1 and os.getenv("RAW_UAT_CONFIRM", "").strip() != "YES":
        raise SystemExit(
            "Refusing multi-case raw UAT without RAW_UAT_CONFIRM=YES. "
            "Use CASE_ID or MAX_CASES for cheaper targeted runs."
        )

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    report_path = REPORTS_DIR / f"raw_uat_{ts}.json"

    results = []

    for case in cases:
        conversation = [{"role": "system", "content": system_prompt}]

        if "turns" in case:
            turns = case.get("turns") or []
            if not turns:
                raise SystemExit(f"Case has empty turns: {case.get('case_id')}")
        else:
            turns = [case["input"]]

        parsed = None
        last_user_input = None

        for user_input in turns:
            last_user_input = user_input
            conversation.append({"role": "user", "content": user_input})

            for attempt in range(5):
                try:
                    response = client.responses.create(
                        model=MODEL,
                        input=conversation
                    )
                    break
                except Exception as e:
                    if "rate_limit" not in str(e).lower() and "429" not in str(e):
                        raise
                    if attempt == 4:
                        raise
                    time.sleep(2 + attempt * 2)

            text = response.output_text
            parsed = extract_debug_and_messages(text)

            state_snapshot = {
                "phase": parsed["debug"].get("phase"),
                "request_type": parsed["debug"].get("request_type"),
                "selected_phrase_id": parsed["debug"].get("selected_phrase_id"),
                "QUALIFICATION_STATUS": parsed["debug"].get("QUALIFICATION_STATUS"),
                "price_ladder_state": parsed["debug"].get("price_ladder_state"),
                "service_intent": parsed["debug"].get("service_intent"),
                "active_service_context": parsed["debug"].get("active_service_context"),
                "missing_fields": parsed["debug"].get("missing_fields"),
                "phase3a_required": parsed["debug"].get("phase3a_required"),
                "phase3a_complete": parsed["debug"].get("phase3a_complete"),
                "phase3a_qualifier_id": parsed["debug"].get("phase3a_qualifier_id"),
            }

            conversation.append({
                "role": "assistant",
                "content": (
                    text
                    + "\n\nSTATE_SNAPSHOT_FOR_NEXT_TURN:\n"
                    + json.dumps(state_snapshot, ensure_ascii=False, sort_keys=True)
                ),
            })

        failures = check_expectations(parsed, case)

        results.append({
            "case_id": case["case_id"],
            "input": last_user_input,
            "pass": len(failures) == 0,
            "failures": failures,
            "debug": parsed["debug"],
            "arabic": parsed["arabic"],
            "english": parsed["english"],
            "raw": parsed["raw"]
        })

    report = {
        "timestamp": ts,
        "results": results
    }

    Path(report_path).write_text(json.dumps(report, indent=2), encoding="utf-8")

    passed = sum(1 for r in results if r["pass"])
    total = len(results)

    print(f"RAW UAT done. Passed={passed}, Failed={total-passed}, Total={total}")
    print(f"Report: {report_path}")

if __name__ == "__main__":
    main()

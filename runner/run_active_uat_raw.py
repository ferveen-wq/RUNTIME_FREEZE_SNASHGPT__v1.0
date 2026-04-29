import json
import os
import time
from datetime import datetime
from pathlib import Path
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
    "PRICE_LADDER_ENGINE.md",
    "SKU_SELECTION_MATRIX.md",
    "PRICE_TABLE_VAT_INCL.md",
]
def load_system_prompt():
    base_prompt_path = ROOT / "runner/context_reset_prompt_active.txt"
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
        elif ln.startswith("objection_signal:"):
            debug["objection_signal"] = ln.split(":",1)[1].strip()
        elif ln.startswith("objection_repeat_count:"):
            debug["objection_repeat_count"] = ln.split(":",1)[1].strip()
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
        elif ln.startswith("CANONICAL_MODEL:"):
            debug["CANONICAL_MODEL"] = ln.split(":",1)[1].strip()
        elif ln.startswith("VCB:"):
            debug["VCB"] = ln.split(":",1)[1].strip()
        elif ln.startswith("vehicle_year:"):
            debug["vehicle_year"] = ln.split(":",1)[1].strip()
        elif ln.startswith("CURRENT_YEAR:"):
            debug["CURRENT_YEAR"] = ln.split(":",1)[1].strip()
        elif ln.startswith("vehicle_age:"):
            debug["vehicle_age"] = ln.split(":",1)[1].strip()
        elif ln.startswith("ceramic_pricing_age_band:"):
            debug["ceramic_pricing_age_band"] = ln.split(":",1)[1].strip()
        elif ln.startswith("selected_skus:"):
            debug["selected_skus"] = ln.split(":",1)[1].strip()
        elif ln.startswith("price_source_rows:"):
            debug["price_source_rows"] = ln.split(":",1)[1].strip()
        elif ln.startswith("missing_fields:"):
            debug["missing_fields"] = ln.split(":",1)[1].strip()
        elif ln.startswith("phase3a_required:"):
            debug["phase3a_required"] = ln.split(":",1)[1].strip()
        elif ln.startswith("phase3a_complete:"):
            debug["phase3a_complete"] = ln.split(":",1)[1].strip()
        elif ln.startswith("phase3a_qualifier_id:"):
            debug["phase3a_qualifier_id"] = ln.split(":",1)[1].strip()
        elif ln.startswith("PPF_COVERAGE_INTENT:"):
            debug["PPF_COVERAGE_INTENT"] = ln.split(":",1)[1].strip()
        elif ln.startswith("PPF_DRIVING_PATTERN:"):
            debug["PPF_DRIVING_PATTERN"] = ln.split(":",1)[1].strip()
        elif ln.startswith("PPF_BRAND_INTENT:"):
            debug["PPF_BRAND_INTENT"] = ln.split(":",1)[1].strip()
        elif ln.startswith("PPF_FINISH_INTENT:"):
            debug["PPF_FINISH_INTENT"] = ln.split(":",1)[1].strip()
        elif ln.startswith("CERAMIC_GOAL:"):
            debug["CERAMIC_GOAL"] = ln.split(":",1)[1].strip()
        elif ln.startswith("CERAMIC_WASH_PATTERN:"):
            debug["CERAMIC_WASH_PATTERN"] = ln.split(":",1)[1].strip()
        elif ln.startswith("TINT_GOAL:"):
            debug["TINT_GOAL"] = ln.split(":",1)[1].strip()
        elif ln.startswith("TINT_COVERAGE:"):
            debug["TINT_COVERAGE"] = ln.split(":",1)[1].strip()
        elif ln.startswith("POLISHING_SCOPE:"):
            debug["POLISHING_SCOPE"] = ln.split(":",1)[1].strip()
        elif ln.startswith("PAINT_CONDITION_REPAINT_SCRATCH:"):
            debug["PAINT_CONDITION_REPAINT_SCRATCH"] = ln.split(":",1)[1].strip()

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

def customer_facing_text(text):
    """Return customer-facing assistant body only for content assertions.

    Excludes DEBUG_OUTPUT fields, STATE_SNAPSHOT blocks, and timestamp/color
    wrapper lines so exact price assertions are not contaminated by debug,
    state JSON, or timestamp artifacts.
    """
    body = text

    if "\n\n" in body:
        body = body.split("\n\n", 1)[1]

    if "STATE_SNAPSHOT_FOR_NEXT_TURN:" in body:
        body = body.split("STATE_SNAPSHOT_FOR_NEXT_TURN:", 1)[0]

    lines = []
    for line in body.splitlines():
        if "Timestamp:" in line:
            continue
        lines.append(line)

    return "\n".join(lines).strip()


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

        # Price-trust UAT enforcement:
        # If a case expects the pricing ladder to finish, it must validate
        # actual customer-facing price output, not debug state only.
        if str(exp_debug.get("price_ladder_state", "")).strip() == "FINAL_PRICE_REACHED":
            exp_contains = case.get("expect_contains", []) or []
            exp_not_contains = case.get("expect_not_contains", []) or []

            has_vat = any("BD VAT included" in str(x) for x in exp_contains)
            has_digit = any(any(ch.isdigit() for ch in str(x)) for x in exp_contains)

            if not (has_vat and has_digit):
                weak.append(
                    case.get("case_id", "<missing case_id>")
                    + " [price UAT requires exact numeric expect_contains + BD VAT included]"
                )

            if "price" in str(case.get("case_id", "")).lower() and not exp_not_contains:
                weak.append(
                    case.get("case_id", "<missing case_id>")
                    + " [price UAT should include expect_not_contains for known wrong prices]"
                )

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

    
    # Content validation uses customer-facing body only.
    # Excludes debug/state/timestamp artifacts from exact price assertions.
    customer_text = customer_facing_text(parsed.get("raw", ""))

    exp_contains = case.get("expect_contains", [])
    for item in exp_contains:
        if item not in customer_text:
            failures.append(f"missing expected text: {item}")

    exp_not_contains = case.get("expect_not_contains", [])
    for item in exp_not_contains:
        if item in customer_text:
            failures.append(f"forbidden text present: {item}")

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

    cases_path = Path(cases_file)
    allowed_root = Path("tests/active_rollout_uat")

    try:
        cases_path.relative_to(allowed_root)
    except ValueError:
        raise SystemExit(
            "run_active_uat_raw.py only accepts active rollout UAT files under "
            "tests/active_rollout_uat. Move this case file there before running."
        ) from None

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
            raise SystemExit(f"MAX_CASES must be an integer, got: {max_cases}") from None
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
                "objection_signal": parsed["debug"].get("objection_signal"),
                "objection_repeat_count": parsed["debug"].get("objection_repeat_count"),
                "selected_phrase_id": parsed["debug"].get("selected_phrase_id"),
                "QUALIFICATION_STATUS": parsed["debug"].get("QUALIFICATION_STATUS"),
                "price_ladder_state": parsed["debug"].get("price_ladder_state"),
                "service_intent": parsed["debug"].get("service_intent"),
                "active_service_context": parsed["debug"].get("active_service_context"),
                "CANONICAL_MODEL": parsed["debug"].get("CANONICAL_MODEL"),
                "VCB": parsed["debug"].get("VCB"),
                "vehicle_year": parsed["debug"].get("vehicle_year"),
                "CURRENT_YEAR": parsed["debug"].get("CURRENT_YEAR"),
                "vehicle_age": parsed["debug"].get("vehicle_age"),
                "ceramic_pricing_age_band": parsed["debug"].get("ceramic_pricing_age_band"),
                "selected_skus": parsed["debug"].get("selected_skus"),
                "price_source_rows": parsed["debug"].get("price_source_rows"),
                "missing_fields": parsed["debug"].get("missing_fields"),
                "phase3a_required": parsed["debug"].get("phase3a_required"),
                "phase3a_complete": parsed["debug"].get("phase3a_complete"),
                "phase3a_qualifier_id": parsed["debug"].get("phase3a_qualifier_id"),
                "PPF_COVERAGE_INTENT": parsed["debug"].get("PPF_COVERAGE_INTENT"),
                "PPF_DRIVING_PATTERN": parsed["debug"].get("PPF_DRIVING_PATTERN"),
                "PPF_BRAND_INTENT": parsed["debug"].get("PPF_BRAND_INTENT"),
                "PPF_FINISH_INTENT": parsed["debug"].get("PPF_FINISH_INTENT"),
                "CERAMIC_GOAL": parsed["debug"].get("CERAMIC_GOAL"),
                "CERAMIC_WASH_PATTERN": parsed["debug"].get("CERAMIC_WASH_PATTERN"),
                "TINT_GOAL": parsed["debug"].get("TINT_GOAL"),
                "TINT_COVERAGE": parsed["debug"].get("TINT_COVERAGE"),
                "POLISHING_SCOPE": parsed["debug"].get("POLISHING_SCOPE"),
                "PAINT_CONDITION_REPAINT_SCRATCH": parsed["debug"].get("PAINT_CONDITION_REPAINT_SCRATCH"),
            }

            conversation.append({
                "role": "assistant",
                "content": (
                    "STATE_SNAPSHOT_FOR_NEXT_TURN:\n"
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

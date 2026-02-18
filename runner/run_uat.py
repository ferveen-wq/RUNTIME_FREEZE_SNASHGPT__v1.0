import json
import os
from pathlib import Path
from datetime import datetime

from openai import OpenAI

ROOT = Path(__file__).resolve().parents[1]
PROMPT_PATH = ROOT / "runner" / "context_reset_prompt.txt"
CASES_PATH = ROOT / "tests" / "uat_cases.json"
REPORTS_DIR = ROOT / "tests" / "reports"

MODEL = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")  # change if you want


def load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8").strip()


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def safe_lower(s: str) -> str:
    return (s or "").lower()


def extract_debug_and_messages(full_text: str) -> dict:
    """
    We assume your response starts with DEBUG_OUTPUT header.
    We'll do a simple parse:
    - debug block: lines until first blank line after DEBUG_OUTPUT (best-effort)
    - arabic message: first non-debug paragraph
    - english message: next paragraph (best-effort)
    Adjust later once your OUTPUT_RESPONSE_TEMPLATE is fully stable.
    """
    lines = full_text.splitlines()
    debug = {}
    in_debug = False

    for line in lines:
        if "DEBUG_OUTPUT" in line:
            in_debug = True
            continue
        if in_debug:
            if not line.strip():
                break
            # very forgiving "key: value" parsing
            if ":" in line:
                k, v = line.split(":", 1)
                debug[k.strip()] = v.strip()

    # crude message extraction: remove debug lines, then join remaining
    cleaned = []
    for line in lines:
        if "DEBUG_OUTPUT" in line:
            continue
        if ":" in line and line.split(":", 1)[0].strip() in debug:
            continue
        cleaned.append(line)

    body = "\n".join(cleaned).strip()
    # split into paragraphs
    parts = [p.strip() for p in body.split("\n\n") if p.strip()]

    arabic = parts[0] if len(parts) >= 1 else ""
    english = parts[1] if len(parts) >= 2 else ""

    return {"debug": debug, "arabic": arabic, "english": english, "raw": full_text}


def check_expectations(result: dict, case: dict) -> list:
    failures = []
    debug = result["debug"]
    arabic = result["arabic"]
    english = result["english"]

    # Debug expectations
    for k, v in case.get("expect_debug", {}).items():
        actual = debug.get(k)
        if actual is None:
            failures.append(f"Missing debug key '{k}'")
        else:
            if str(actual).strip() != str(v).strip():
                failures.append(f"Debug '{k}' expected '{v}' but got '{actual}'")

    # Must contain checks
    exp_contains = case.get("expect_contains", {})
    for word in exp_contains.get("arabic", []):
        if safe_lower(word) not in safe_lower(arabic):
            failures.append(f"Arabic missing required word: '{word}'")
    for word in exp_contains.get("english", []):
        if safe_lower(word) not in safe_lower(english):
            failures.append(f"English missing required word: '{word}'")

    # Must not contain checks
    exp_not = case.get("expect_not_contains", {})
    for word in exp_not.get("arabic", []):
        if safe_lower(word) in safe_lower(arabic):
            failures.append(f"Arabic contains forbidden word: '{word}'")
    for word in exp_not.get("english", []):
        if safe_lower(word) in safe_lower(english):
            failures.append(f"English contains forbidden word: '{word}'")

    return failures


def main():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise SystemExit("OPENAI_API_KEY is not set. Set it and re-run.")

    client = OpenAI(api_key=api_key)

    system_prompt = load_text(PROMPT_PATH)
    cases = load_json(CASES_PATH)

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    report_path = REPORTS_DIR / f"uat_report_{ts}.json"

    report = {
        "timestamp_utc": ts,
        "model": MODEL,
        "results": []
    }

    passed = 0
    failed = 0

    for case in cases:
        user_input = case["input"]

        resp = client.responses.create(
            model=MODEL,
            input=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ],
        )

        # The SDK returns a structured object; simplest is to read output_text
        full_text = resp.output_text

        parsed = extract_debug_and_messages(full_text)
        failures = check_expectations(parsed, case)

        case_result = {
            "case_id": case.get("case_id"),
            "input": user_input,
            "pass": len(failures) == 0,
            "failures": failures,
            "debug": parsed["debug"],
            "arabic": parsed["arabic"],
            "english": parsed["english"],
            "raw": parsed["raw"]
        }

        report["results"].append(case_result)

        if case_result["pass"]:
            passed += 1
        else:
            failed += 1

    report["summary"] = {"passed": passed, "failed": failed, "total": passed + failed}

    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"UAT done. Passed={passed}, Failed={failed}, Total={passed+failed}")
    print(f"Report saved: {report_path}")

    if failed > 0:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
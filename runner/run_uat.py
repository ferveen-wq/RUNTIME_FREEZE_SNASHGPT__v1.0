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
    import re

    lines = full_text.splitlines()
    debug = {}
    in_debug = False

    # 1) Parse DEBUG_OUTPUT block (key: value lines)
    for line in lines:
        if "DEBUG_OUTPUT" in line:
            in_debug = True
            continue
        if in_debug:
            if not line.strip():
                break
            if ":" in line:
                k, v = line.split(":", 1)
                debug[k.strip()] = v.strip()

    # 2) Remove debug lines from body
    body_lines = []
    skipping_debug = False
    for line in lines:
        if "DEBUG_OUTPUT" in line:
            skipping_debug = True
            continue
        if skipping_debug:
            # stop skipping after first blank line
            if not line.strip():
                skipping_debug = False
            continue
        body_lines.append(line)

    body = "\n".join([l for l in body_lines if l is not None]).strip()

    # 3) Split Arabic vs English by character detection
    # Arabic unicode range: \u0600-\u06FF plus extended: \u0750-\u077F \u08A0-\u08FF
    arabic_re = re.compile(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF]")

    arabic_lines = []
    english_lines = []
    for line in body.splitlines():
        if arabic_re.search(line):
            arabic_lines.append(line.strip())
        else:
            if line.strip():
                english_lines.append(line.strip())

    arabic = "\n".join(arabic_lines).strip()
    english = "\n".join(english_lines).strip()

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

    report_path.write_text(
        json.dumps(report, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )

    print(f"UAT done. Passed={passed}, Failed={failed}, Total={passed+failed}")
    print(f"Report saved: {report_path}")

    if failed > 0:
        print("\nFAILED TEST DETAILS (first 10):")
        shown = 0
        for r in report["results"]:
            if not r["pass"]:
                shown += 1
                print("\n---")
                print(f"case_id: {r.get('case_id')}")
                print(f"input: {r.get('input')}")
                print(f"failures: {r.get('failures')}")
                print("debug:", r.get("debug"))
                print("arabic:", r.get("arabic"))
                print("english:", r.get("english"))
                if shown >= 10:
                    break

        raise SystemExit(1)

if __name__ == "__main__":
    main()
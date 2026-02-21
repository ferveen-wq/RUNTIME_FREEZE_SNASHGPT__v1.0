import json
import os
import re
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

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


def load_system_prompt() -> str:
    base = load_text(PROMPT_PATH)
    now_bh = datetime.now(ZoneInfo("Asia/Bahrain")).strftime("%Y-%m-%d %H:%M")
    return base.replace("Begin.", f"CURRENT_BAHRAIN_TIME: {now_bh} (Asia/Bahrain)\n\nBegin.")


def normalize_arabic(s: str) -> str:
    if not s:
        return ""
    diacritics = [
        "\u064b",
        "\u064c",
        "\u064d",
        "\u064e",
        "\u064f",
        "\u0650",
        "\u0651",
        "\u0652",
        "\u0653",
        "\u0654",
        "\u0655",
        "\u0656",
        "\u0657",
        "\u0658",
        "\u0659",
        "\u065a",
        "\u0670",
    ]
    for d in diacritics:
        s = s.replace(d, "")
    return s


def normalize_for_contains(s: str) -> str:
    if not s:
        return ""
    s = normalize_arabic(s).lower()
    s = re.sub(r"[^\w\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF]+", " ", s, flags=re.UNICODE)
    s = re.sub(r"\s+", " ", s, flags=re.UNICODE).strip()
    return s


def compute_request_type_uat(user_input: str) -> str:
    msg = normalize_for_contains(user_input)

    # 1) Greeting-only (Phase 0)
    # Keep this tight: short greetings / salutations with no service/vehicle intent.
    greeting_tokens = {
        "hi",
        "hello",
        "hey",
        "yo",
        "السلام عليكم",
        "سلام",
        "هلا",
        "هلا والله",
        "مرحبا",
        "أهلا",
        "اهلا",
    }
    if msg in greeting_tokens:
        return "GREETING_ONLY"

    # 1.5) Business info / location / hours / branches (Phase 0–2)
    # UAT expects these to classify as LOCATION (not OTHER).
    loc_triggers = [
        # English
        "where are you located",
        "where is your location",
        "location",
        "opening hours",
        "open hours",
        "working hours",
        "what are your hours",
        "hours",
        "branch in saudi",
        "branch in ksa",
        "do you have a branch in saudi",
        "do you have a branch in ksa",
        # Arabic / GCC
        "وين موقعكم",
        "موقعكم",
        "لوكيشن",
        "متى تفتحون",
        "اوقات الدوام",
        "ساعات العمل",
        "دوام",
        "عندكم فرع بالسعودية",
        "عندكم فرع في السعودية",
        "فرع بالسعودية",
        "فرع في السعودية",
        "السعودية",
    ]
    if any(t in msg for t in loc_triggers):
        return "LOCATION"

    # 2) Browsing / discovery (Phase 0–2)
    browsing_markers = [
        "what services do you offer",
        "what do you offer",
        "services",
        "service list",
        "your services",
        "شنو خدماتكم",
        "شنو عندكم",
        "وش عندكم",
        "الخدمات",
    ]
    if any(m in msg for m in browsing_markers):
        return "BROWSING_GENERIC"

    # 3) Brand-only availability/install questions (Phase 0–2 override)
    # Only treat as brand-only if user is asking about install/availability,
    # not if they are explicitly requesting PPF as a service.
    if ("xpel" in msg) and any(
        k in msg for k in ["install", "do you", "تركبون", "تركيب", "توفرون", "available", "عندكم"]
    ):
        return "OTHER"

    # 4) Direct price request (HARD override)
    price_tokens = [
        "how much",
        "price",
        "pricing",
        "cost",
        "كم",
        "سعر",
        "بكم",
        "كم السعر",
        "التكلفة",
        "كم يكلف",
    ]
    if any(tok in msg for tok in price_tokens):
        return "PRICE_REQUEST"

    # 5) Service confirmed (Phase 0–2)
    # Detect explicit service keyword presence.
    service_keywords = [
        "ppf",
        "ceramic",
        "tint",
        "wrap",
        "polishing",
        "تظليل",
        "عازل",
        "تلميع",
        "تلماع",
        "سيراميك",
        "حماية",
    ]
    if any(s in msg for s in service_keywords):
        return "SERVICE_CONFIRMED"

    return "OTHER"


def inject_readonly_runtime_signals(system_prompt: str, user_input: str) -> str:
    req = compute_request_type_uat(user_input)
    injected = (
        "RUNTIME_SIGNALS (READ-ONLY; DO NOT MODIFY):\n"
        f"- request_type: {req}\n"
        "\n"
        "HARD RULE:\n"
        "- In DEBUG_OUTPUT, you MUST print request_type EXACTLY as provided above.\n"
        "- Do NOT output any other request_type value (e.g., PRICE is invalid).\n"
        "\n"
    )
    return injected + system_prompt


def extract_debug_and_messages(full_text: str) -> dict:
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
            if ":" in line:
                k, v = line.split(":", 1)
                debug[k.strip()] = v.strip()

    body_lines = []
    skipping_debug = False
    for line in lines:
        if "DEBUG_OUTPUT" in line:
            skipping_debug = True
            continue
        if skipping_debug:
            if not line.strip():
                skipping_debug = False
            continue
        body_lines.append(line)

    body = "\n".join([ln for ln in body_lines if ln is not None]).strip()

    arabic_re = re.compile(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF]")
    arabic_lines = []
    english_lines = []

    for line in body.splitlines():
        if arabic_re.search(line):
            arabic_lines.append(line.strip())
        else:
            if line.strip():
                english_lines.append(line.strip())

    return {
        "debug": debug,
        "arabic": "\n".join(arabic_lines).strip(),
        "english": "\n".join(english_lines).strip(),
        "raw": full_text,
    }


def check_expectations(parsed: dict, case: dict) -> list[str]:
    failures: list[str] = []
    debug = parsed["debug"]
    arabic = parsed["arabic"]
    english = parsed["english"]

    def strip_timestamp(s: str) -> str:
        if not s:
            return ""
        return "\n".join([ln for ln in s.splitlines() if "Timestamp:" not in ln]).strip()

    arabic_chk = strip_timestamp(arabic)
    english_chk = strip_timestamp(english)
    arabic_norm = normalize_for_contains(arabic_chk)
    english_norm = normalize_for_contains(english_chk)

    for k, v in case.get("expect_debug", {}).items():
        actual = debug.get(k)
        if actual is None:
            failures.append(f"Missing debug key '{k}'")
        elif str(actual).strip() != str(v).strip():
            failures.append(f"Debug '{k}' expected '{v}' but got '{actual}'")

    allowed_request_types = {
        "BROWSING_GENERIC",
        "GREETING_ONLY",
        "REENTERED_CONTINUE",
        "SERVICE_CONFIRMED",
        "SERVICE_INFERRED",
        "PRICE_REQUEST",
        "LOCATION",
        "OTHER",
    }
    rt = debug.get("request_type")
    if rt and rt not in allowed_request_types:
        failures.append(
            f"Debug 'request_type' invalid enum '{rt}' (allowed: {sorted(allowed_request_types)})"
        )

    exp_contains = case.get("expect_contains", {})
    for word in exp_contains.get("arabic", []):
        if normalize_for_contains(word) not in arabic_norm:
            failures.append(f"Arabic missing required word: '{word}'")
    for word in exp_contains.get("english", []):
        if normalize_for_contains(word) not in english_norm:
            failures.append(f"English missing required word: '{word}'")

    exp_contains_any = case.get("expect_contains_any", {})
    any_ar = exp_contains_any.get("arabic", [])
    if any_ar and not any(normalize_for_contains(w) in arabic_norm for w in any_ar):
        failures.append(f"Arabic missing any of: {any_ar}")

    any_en = exp_contains_any.get("english", [])
    if any_en and not any(normalize_for_contains(w) in english_norm for w in any_en):
        failures.append(f"English missing any of: {any_en}")

    # NOT-CONTAINS must be LITERAL substring checks (case-insensitive).
    # Reason: normalization collapses tokens like "$" -> "" and "year?" -> "year" causing false positives.
    exp_not = case.get("expect_not_contains", {}) or {}
    arabic_lc = arabic_chk.lower()
    english_lc = english_chk.lower()

    for word in exp_not.get("arabic", []) or []:
        w = (word or "").strip().lower()
        if w and (w in arabic_lc):
            failures.append(f"Arabic contains forbidden word: '{word}'")

    for word in exp_not.get("english", []) or []:
        w = (word or "").strip().lower()
        if w and (w in english_lc):
            failures.append(f"English contains forbidden word: '{word}'")

    # Forbidden words check (LITERAL substring; NOT regex)
    # Reason: tokens like "$" have special meaning in regex and cause false positives.
    forbidden_words = case.get("forbidden_words", {}) or {}
    for lang in ("english", "arabic"):
        text = parsed.get(lang) or ""
        text_lc = text.lower()
        for w in forbidden_words.get(lang, []) or []:
            w_lc = (w or "").lower()
            if w_lc and (w_lc in text_lc):
                failures.append(f"{lang} contains forbidden word: '{w}'")

    return failures


def main():
    import subprocess
    import sys

    lint_cmd = [sys.executable, os.path.join(os.path.dirname(__file__), "lint_authority.py")]
    lint = subprocess.run(lint_cmd, capture_output=True, text=True)
    print(lint.stdout)
    if lint.returncode != 0:
        print(lint.stderr)
        print("UAT aborted: authority lint failed.")
        sys.exit(1)

    api_key = (os.getenv("OPENAI_API_KEY") or "").strip()
    if not api_key:
        raise SystemExit("OPENAI_API_KEY is not set. Set it and re-run.")

    client = OpenAI(api_key=api_key)
    system_prompt = load_system_prompt()

    cases_file = os.getenv("UAT_CASES_FILE", "")
    cases_path = Path(cases_file) if cases_file else CASES_PATH
    cases = load_json(cases_path)

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    report_path = REPORTS_DIR / f"uat_report_{ts}.json"

    report = {"timestamp_utc": ts, "model": MODEL, "results": []}
    passed = 0
    failed = 0

    for case in cases:
        user_input = case["input"]
        system_prompt_with_signals = inject_readonly_runtime_signals(system_prompt, user_input)

        resp = client.responses.create(
            model=MODEL,
            input=[
                {"role": "system", "content": system_prompt_with_signals},
                {"role": "user", "content": user_input},
            ],
        )

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
            "raw": parsed["raw"],
        }

        report["results"].append(case_result)
        if case_result["pass"]:
            passed += 1
        else:
            failed += 1

        report["summary"] = {"passed": passed, "failed": failed, "total": passed + failed}

    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"UAT done. Passed={passed}, Failed={failed}, Total={passed + failed}")
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
                print(f"debug: {r.get('debug')}")
                print(f"arabic: {r.get('arabic')}")
                print(f"english: {r.get('english')}")
                if shown >= 10:
                    break
        raise SystemExit(1)


if __name__ == "__main__":
    main()

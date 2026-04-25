from pathlib import Path
import json

def classify_failure(failures, debug):
    f = " ".join(failures)

    if "selected_phrase_id" in f:
        return "PHRASE_ID_MISMATCH", "Check PHASE4_8_MESSAGE_ASSEMBLY_MAP or competing route"

    if "QUALIFICATION_STATUS" in f:
        return "QUALIFICATION_STATUS_MISMATCH", "Check QUALIFICATION_ENGINE readiness logic"

    if "phase expected" in f:
        return "PHASE_LABEL_MISMATCH", "Check routing vs expectation (may not be runtime bug)"

    if "price_ladder_state" in f:
        return "PRICE_LADDER_LEAK", "Check PRICE_LADDER_ENGINE or premature pricing"

    # fallback pattern detection
    if debug.get("selected_phrase_id", "").startswith("ESCALATION"):
        return "OUTPUT_TEMPLATE_OVERRIDE", "Check OUTPUT_RESPONSE_TEMPLATE override risk"

    return "UNKNOWN", "Manual inspection required"


def main():
    reports = sorted(Path("tests/reports").glob("raw_uat_*.json"), key=lambda p: p.stat().st_mtime)
    if not reports:
        print("[ERROR] No reports found")
        return

    latest = reports[-1]
    print(f"\n===== ANALYZING: {latest} =====\n")

    data = json.loads(latest.read_text(encoding="utf-8"))

    for r in data["results"]:
        print("CASE:", r["case_id"])
        print("PASS:", r["pass"])

        if not r["pass"]:
            failure_type, suggestion = classify_failure(r["failures"], r["debug"])

            print("FAILURES:", r["failures"])
            print("DEBUG:", r["debug"])
            print("CLASSIFICATION:", failure_type)
            print("SUGGESTED NEXT STEP:", suggestion)

        print("-" * 60)


if __name__ == "__main__":
    main()

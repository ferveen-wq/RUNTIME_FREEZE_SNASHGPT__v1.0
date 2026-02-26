from pathlib import Path
import re

FILE = Path("00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_6_HUMAN_PHRASE_LIBRARY.md")

def replace_block(text: str, header: str, new_lines: list[str]) -> str:
    """
    Replace the first contiguous block that starts with `header` (exact line),
    and continues until the next '### ' header or EOF.
    Keeps the header line, replaces the content lines under it with new_lines.
    """
    pattern = rf"(^### {re.escape(header)}\s*\n)(.*?)(?=^\#\#\# |\Z)"
    m = re.search(pattern, text, flags=re.M | re.S)
    if not m:
        raise SystemExit(f"ERROR: block header not found: ### {header}")

    before = text[:m.start(2)]
    after = text[m.end(2):]
    # Ensure new content ends with newline
    new_body = "\n".join(new_lines).rstrip() + "\n\n"
    return before + new_body + after

def main():
    text = FILE.read_text(encoding="utf-8")

    # 1) Business hours
    text = replace_block(
        text,
        "BIZ_HOURS__ASK_DAY (PHASE 0–2 / BUSINESS INFO)",
        [
            "AR: دوامنا **السبت–الخميس** من **10:00 صباحًا** إلى **7:00 مساءً**. إذا تحتاج وقت ثاني خبرنا ونحاول نرتّب أحد يستقبلك. أي يوم ناوي تمر؟",
            "EN: Our hours are **Sat–Thu** **10:00am–7:00pm**. If you need another time, tell us and we’ll try to arrange someone to receive you. What day are you planning to come?",
        ],
    )

    # 2) Ceramic wash pattern qualifier (Phase 3A question)
    text = replace_block(
        text,
        "PHASE3A_Q_CERAMIC_WASH_PATTERN",
        [
            "EN: How do you usually arrange the car wash — bucket/hand wash, a brush/tunnel (automatic) wash, waterless wash, a professional wash center, or a mix?",
            "AR: شلون عادة ترتّب غسيل السيارة — غسيل يدوي/سطل، غسيل نفق/آلي (فرش/رول)، غسيل بدون ماء، مركز غسيل محترف، أو خليط؟",
        ],
    )

    # 3) C.2 Ceramic explanation + qualifier (Phase 0–2)
    text = replace_block(
        text,
        "C.2 CERAMIC EXPLANATION + QUALIFIER (PHASE 0–2)",
        [
            "EN: Ceramic coating is like skincare for your car’s paint. It keeps the finish glossy, makes washing easier, and helps the car stay looking newer for longer. To guide you correctly, what’s the car model and year?",
            "AR:",
        ],
    )

    # 4) Multi service intent safe (Phase 0–2)
    text = replace_block(
        text,
        "MULTI_SERVICE_INTENT_SAFE (PHASE 0–2)",
        [
            "EN: Sure — we can take them one by one and keep it simple. What’s the car model and year?",
            "AR: أكيد — نقدر ناخذهم واحد واحد وبكل بساطة. شنو موديل السيارة وأي سنة؟",
        ],
    )

    FILE.write_text(text, encoding="utf-8")
    print("OK: patched", FILE)

if __name__ == "__main__":
    main()

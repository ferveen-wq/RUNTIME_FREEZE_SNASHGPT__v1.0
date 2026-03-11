from pathlib import Path

p = Path("00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_6_HUMAN_PHRASE_LIBRARY.md")
s = p.read_text(encoding="utf-8")

needle = (
    "### C.2 CERAMIC EXPLANATION + QUALIFIER (PHASE 0–2)\n\n"
    "EN: Ceramic coating is like skincare for your car’s paint. It keeps the finish glossy, makes washing easier, and helps the car stay looking newer for longer. To guide you correctly, what’s the car model and year?\n"
    "AR:\n"
)

replacement = (
    "### C.2 CERAMIC EXPLANATION + QUALIFIER (PHASE 0–2)\n\n"
    "EN: Ceramic coating is like skincare for your car’s paint. It keeps the finish glossy, makes washing easier, and helps the car stay looking newer for longer. To guide you correctly, what’s the car model and year?\n"
    "AR: السيراميك مثل العناية ببشرة طلاء السيارة. يعطي لمعة ثابتة، ويسهّل الغسيل، ويساعد السيارة تظل شكلها أحدث لفترة أطول. عشان أوجهك صح، شنو موديل السيارة وأي سنة؟\n"
)

if needle not in s:
    raise SystemExit("ABORT: expected C.2 block (with empty AR) not found exactly. No changes applied.")

s = s.replace(needle, replacement)
p.write_text(s, encoding="utf-8")
print("OK: patched", p)

from pathlib import Path

p = Path("00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_6_HUMAN_PHRASE_LIBRARY.md")
s = p.read_text(encoding="utf-8")

repls = {
  # L.1 V1/V2/V3
  "EN (V1): To guide you correctly, what’s the car model and year?":
    "EN (V1): Sure — to guide you correctly, what’s the car model and year?",
  "AR (V1): عشان أوجهك صح، شنو موديل السيارة وأي سنة؟":
    "AR (V1): أكيد — عشان أوجهك صح، شنو موديل السيارة وأي سنة؟",

  "EN (V2): Quick check — what’s the car model and year?":
    "EN (V2): Just a quick check — what’s the car model and year?",
  "AR (V2): سؤال سريع — شنو موديل السيارة وأي سنة؟":
    "AR (V2): بس سؤال سريع — شنو موديل السيارة وأي سنة؟",

  "EN (V3): Last detail I need: car model and year?":
    "EN (V3): Last detail I need — what’s the car model and year?",
  "AR (V3): آخر معلومة أحتاجها: موديل السيارة وأي سنة؟":
    "AR (V3): آخر معلومة أحتاجها — موديل السيارة وأي سنة؟",

  # Loose MODEL_ONLY / YEAR_ONLY lines in that same section
  "EN: What’s the exact car model?":
    "EN: Sure — what’s the exact car model?",
  "AR: شنو موديل السيارة بالضبط؟":
    "AR: أكيد — شنو موديل السيارة بالضبط؟",

  # YEAR_ONLY header block
  "EN: What’s the model year?":
    "EN: Sure — what’s the model year?",
  "AR: شنو سنة الموديل؟":
    "AR: أكيد — شنو سنة الموديل؟",
}

missing = [k for k in repls.keys() if k not in s]
if missing:
    raise SystemExit("ABORT: did not find expected lines:\n- " + "\n- ".join(missing))

for k, v in repls.items():
    s = s.replace(k, v)

p.write_text(s, encoding="utf-8")
print("OK: patched", p)

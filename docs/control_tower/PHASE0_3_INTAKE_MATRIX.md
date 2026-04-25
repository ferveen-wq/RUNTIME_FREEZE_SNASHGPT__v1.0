# PHASE 0–3 INTAKE MATRIX

## STATUS LEGEND
- ⬜ NOT TESTED
- 🟨 IN PROGRESS
- 🟩 STABLE
- 🟥 FAILING
- 🟦 MONITORED

---

## 1. LANGUAGE INTAKE

| Case | Example | Status |
|------|--------|--------|
| Arabic input | "كم سعر التظليل" | ⬜ |
| English input | "price for ceramic" | ⬜ |
| Mixed input | "ceramic كم سعر" | ⬜ |
| Slang / short | "ppf?" | ⬜ |

---

## 2. SERVICE RECOGNITION

| Case | Example | Status |
|------|--------|--------|
| PPF explicit | "ppf camry 2022" | ⬜ |
| Ceramic explicit | "ceramic altima" | ⬜ |
| Tint / alias | "تظليل" | ⬜ |
| Polishing | "polish scratches" | ⬜ |
| General vague | "car protection" | ⬜ |

---

## 3. NON-SERVICE MESSAGES

| Case | Example | Status |
|------|--------|--------|
| Job inquiry | "في وظائف؟" | ⬜ |
| Marketing | "عندكم عروض؟" | ⬜ |
| Random | "وين موقعكم؟" | ⬜ |

---

## 4. VEHICLE DATA HANDLING

| Case | Example | Status |
|------|--------|--------|
| Full correct | "camry 2022" | ⬜ |
| Missing model | "toyota 2022" | ⬜ |
| Missing year | "camry" | ⬜ |
| Wrong format | "كامري توتو" | ⬜ |
| Arabic alias | "كامري 2022" | ⬜ |

---

## 5. MULTI-TURN CONTINUATION

| Case | Example | Status |
|------|--------|--------|
| Follow-up short | "yes" | ⬜ |
| Add info later | "2022" | ⬜ |
| Correction | "no corolla" | ⬜ |

---

## 6. EARLY PRICE PRESSURE

| Case | Example | Status |
|------|--------|--------|
| Immediate price ask | "كم السعر" | ⬜ |
| Repeated push | "price???" | ⬜ |
| Objection early | "غالي" | ⬜ |

---

## 7. ROUTING CONTROL

| Case | Example | Status |
|------|--------|--------|
| Stay in Phase 0–3 | normal intake | ⬜ |
| Avoid Phase 4 jump | no pricing early | ⬜ |
| Correct service routing | no mixing services | ⬜ |

---

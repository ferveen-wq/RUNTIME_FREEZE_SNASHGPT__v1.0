# PHASE 5.1 — CLOSING STATE MACHINE (AUTHORITATIVE) — v1.0 (DRAFT)

## Design rules
- Deterministic: same input → same state decision.
- Low-pressure by default.
- Never loop endlessly. Respect follow-up caps and stop rules.
- This file defines STATES + TRANSITIONS only.
- Customer wording is referenced by TEMPLATE IDs (Phase 5.5).

---

## State definitions

### S0 — ACTIVE_CONVERSATION
Normal flow. Customer is engaging, asking, responding, or clarifying.

### S1 — READY_TO_CLOSE
We have answered and the last message indicates closure readiness (e.g., "ok", "thanks", confirmation).

### S2 — BOOKING_INTENT
Customer shows intent to book or proceed (explicitly or implicitly).

### S3 — NEEDS_HUMAN
We must hand over to a human operator.

### S4 — FOLLOW_UP_PENDING
Customer said later / will confirm, or went silent after progress.

### S5 — CLOSED_POLITE
We end politely with a clear next step or open door.

### S6 — STOP_NO_MORE_MESSAGES
Hard stop. Do not continue.

---

## Trigger definitions (authoritative)

### STOP signals → (S6 immediate)
Trigger if customer message contains:
- "stop", "don’t message", "unsubscribe", "leave me alone"
Arabic examples: "وقف", "لا ترسل", "لا تكلمني", "لا تواصل"

### HUMAN REQUEST → (S3 candidate)
Trigger if customer message contains:
- "agent", "human", "call me", "someone call", "manager"
Arabic examples: "موظف", "إنسان", "اتصل علي", "أبي أكلم أحد", "مدير"

### COMPLAINT / ANGER → (S3 candidate)
Trigger if:
- Customer expresses dissatisfaction, distrust, anger, threats, refund disputes
Arabic examples: "نصب", "خدمة سيئة", "مو راضي", "شكوى", "أبي فلوسي"

### CONFUSION LOOP → (S3 candidate)
Trigger if BOTH are true:
- We asked a clear question OR provided a clear next step
- Customer response shows confusion / mismatch OR repeats the same question
- This happens for **2 consecutive cycles**
Definition of a cycle:
- Assistant asks/answers → customer confusion/repeat → assistant clarifies → customer confusion/repeat

### YES / BOOKING signals → (S2 candidate)
Trigger if customer message shows intent like:
- "book", "schedule", "come today", "available", "send someone", "confirm", "yes"
Arabic examples: "احجز", "موعد", "اليوم", "أكيد", "تمام", "خلاص", "أكد"

Also trigger if:
- Customer shares location + time window together (even without saying “book”).

### LATER signals → (S4 candidate)
Trigger if customer message contains:
- "later", "tomorrow", "next week", "I’ll confirm", "busy", "remind me"
Arabic examples: "بعدين", "بكرة", "الأسبوع الجاي", "بأكد", "مشغول", "ذكرني"

### NO / NOT INTERESTED → (S5 candidate)
Trigger if customer message contains:
- "no", "not interested", "cancel", "stop asking"
Arabic examples: "لا", "مو مهتم", "إلغاء", "ما أبي"

---

## Transition priority (apply in this order)
If multiple triggers match, apply:

1) STOP → S6
2) HUMAN REQUEST or COMPLAINT/ANGER → S3
3) CONFUSION LOOP → S3
4) YES / BOOKING → S2
5) LATER → S4
6) NO / NOT INTERESTED → S5
7) Else remain in current state (usually S0)

---

## State transitions

### From S0 — ACTIVE_CONVERSATION
- If STOP → S6
- If HUMAN REQUEST / COMPLAINT → S3
- If CONFUSION LOOP → S3
- If YES/BOOKING → S2
- If LATER → S4
- If NO → S5
- If conversation naturally finishes (thanks/ok) → S1

### From S2 — BOOKING_INTENT
Goal: confirm booking details quickly.
- If STOP → S6
- If HUMAN REQUEST / COMPLAINT → S3
- If booking cannot be completed via chat (missing critical info after 2 tries) → S3
- If customer switches to later → S4
- If booking confirmed (details confirmed) → S5
- Else remain S2

### From S3 — NEEDS_HUMAN
- If STOP → S6
- After sending handover acknowledgement → S5

### From S4 — FOLLOW_UP_PENDING
- If STOP → S6
- If customer re-engages → S0 or S2 (based on triggers)
- If follow-up attempts exhausted → S5

### From S1 — READY_TO_CLOSE
- If user asks new question → S0
- Else → S5

### From S5 — CLOSED_POLITE
- If user re-engages → S0 or S2
- Else stay closed

### From S6 — STOP_NO_MORE_MESSAGES
- No transitions. End.

---

## Output mapping (template IDs only)
- Booking next step: TPL_BOOKING_*
- Later / follow-up: TPL_LATER_* and TPL_SILENCE_*
- Human takeover: TPL_HUMAN_*
- Close polite: TPL_CLOSE_*
- Stop confirmation: TPL_STOP_*
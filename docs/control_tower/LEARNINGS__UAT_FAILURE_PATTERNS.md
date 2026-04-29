UAT FAILURE LEARNING SNAPSHOT

Purpose:
Reusable patterns observed from real UAT failures.
Used before running new UATs.

---

1) PHASE LABEL VS PHRASE CONTRADICTION

- selected_phrase_id correct
- phase incorrect

Classification:
Debug contract instability

Example:
PHASE5_* phrase but phase = PHASE_4

---

2) PHASE3B PRICE REPEAT AFTER FINAL_PRICE_REACHED

- price_ladder_state = FINAL_PRICE_REACHED
- user says "expensive"
- system repeats PHASE3B_* instead of Phase 4

Classification:
Objection detection / transition instability

---

3) OBJECTION SIGNAL NOT CLASSIFIED

- "expensive" → sometimes becomes UNKNOWN_OR_AMBIGUOUS

Expected:
PRICE_TOO_HIGH

Impact:
Blocks Phase 4 routing

---

4) DETERMINISM FAILURE PATTERN

- 1x PASS does NOT mean stable
- 3x run required
- 2/3 = instability → DO NOT PATCH

---

5) RULE

DO NOT PATCH:
- If behavior is intermittent
- If routing works but debug/state drifts
- If issue appears in only 1/3 runs

PATCH ONLY:
- When deterministic and owner confirmed


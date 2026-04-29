
ISSUE_017 — Phase3B Price Repeat After Price (Tint)

STATUS:

MONITORED / NOT PATCHABLE

PROBLEM:

After price is shown (price_ladder_state = FINAL_PRICE_REACHED),

customer says "expensive" → system sometimes repeats Phase3B price instead of moving to Phase 4.

EXPECTED:

- phase = PHASE_4

- selected_phrase_id = PHASE4_TINT_PRICE_PRESSURE_L1

ACTUAL (intermittent):

- phase = PHASE_3

- selected_phrase_id = PHASE3B_TINT_RANGE

- objection_signal = UNKNOWN_OR_AMBIGUOUS

EVIDENCE:

- 3x determinism run → 2 PASS / 1 FAIL

- Failed run shows price repeat instead of objection handling

CLASSIFICATION:

Instruction / execution instability

NOT deterministic runtime bug yet

OWNERS (to inspect later):

- CUSTOMER_CHAT_INTAKE_RULES.md

- OBJECTION_RESOLUTION_ENGINE.md

- PHASE4_8_MESSAGE_ASSEMBLY_MAP.md

- PRICE_LADDER_ENGINE.md

RULE:

Do NOT patch until deterministic reproduction is proven


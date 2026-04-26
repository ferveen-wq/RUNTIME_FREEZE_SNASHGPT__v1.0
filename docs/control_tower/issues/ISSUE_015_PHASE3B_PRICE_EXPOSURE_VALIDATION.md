## ISSUE_015 — Phase 3B Price Exposure Validation

Goal:
Validate that Phase 3B does not only select the PHASE3B_* transition phrase, but also exposes actual approved price/range through PRICE_LADDER_ENGINE.

Observed:
- Phase 3A → Phase 3B bridge was validated.
- However, actual price/range exposure from PRICE_LADDER_ENGINE has not been separately validated.
- Phase 4 objection testing became premature because customer objection requires confirmed prior price exposure.

Expected:
- After qualification is complete and customer requests price:
  - selected_phrase_id may use PHASE3B_* transition phrase
  - PRICE_LADDER_ENGINE must expose approved price/range
  - price_ladder_state must reach FINAL_PRICE_REACHED only after actual price/range is shown

Scope:
- PPF
- Ceramic
- Tint
- Polishing

Status:
OPEN — must validate before continuing Phase 4 objection UAT

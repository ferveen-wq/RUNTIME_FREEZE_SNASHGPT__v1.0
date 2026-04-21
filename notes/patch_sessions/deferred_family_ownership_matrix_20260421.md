# Deferred Family Ownership Matrix — 2026-04-21

## Purpose
Convert the forensic findings into a clean working ownership map before any further runtime patching.

## Real-life customer families

### A. Thinking / timing later
Examples:
- let me think
- later
- next month
- after salary
- I'll confirm later

Working owner:
- Primary: Phase 3 orchestration (PIM timing blockers)
- Mid-late routing: Objection Resolution Engine via READINESS_STALL
- Late follow-up / open-door: Phase 5 closing family

Not primary owner:
- Phase 7 education snippets

---

### B. Third-party approval / authority shift
Examples:
- I need to ask my wife
- let me check with my husband
- I need to ask family
- I need to check with my friend
- I need manager approval

Working owner:
- Primary: Objection Resolution Engine via AUTHORITY_SHIFT
- Late follow-up / pause / handover: Phase 5 closing family

Not primary owner:
- Phase 7 education snippets
- Phase 0-2 service explanation

---

### C. Car unavailable / timing blocked by logistics
Examples:
- car is in garage
- car is in workshop
- I did not receive the car yet
- car is not with me

Working owner:
- Primary: Phase 3 orchestration via PIM_CAR_NOT_AVAILABLE
- Late follow-up if conversation is parked: Phase 5 closing family

Not primary owner:
- generic objection deepen phrases
- Phase 7 education snippets

---

### D. Travelling / unavailable / out of country
Examples:
- I am travelling
- out of country now
- busy these days
- will come back later

Working owner:
- Primary: Phase 3 orchestration via PIM_TRAVELLING
- Late follow-up if conversation is parked: Phase 5 closing family

Not primary owner:
- generic silence routing by default
- Phase 7 education snippets

---

## Current observed drift from runner evidence
Evidence:
- tests/reports/uat_report_20260421_140227.json

Observed drift:
- THINKING sometimes lands as SILENCE_AFTER_PRICE
- PARTNER_APPROVAL is unstable across EN vs AR
- TRAVELLING / CAR_UNAVAILABLE / AFTER_SALARY drift across silence, deepen, and wrong service phrases
- one Arabic partner-approval case drifted back to Phase 0-2 ceramic explanation

## Control decision
- Do NOT patch runtime from this matrix alone
- Use this matrix as the authority baseline for the next reassignment step
- Next patch lane must be ownership reconciliation, not phrase repair

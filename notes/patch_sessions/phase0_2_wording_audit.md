# PHASE 0–2 WORDING AUDIT

Status: inspection only  
Scope: wording + routing correctness (no patch yet)

---

## Case 1 — BMW X5 2206 PPF

Expected:
- Detect invalid year
- Stay in Phase 0–2
- Ask to correct year ONLY

Actual:
- Phase: 3
- READY_FOR_NEGOTIATION
- PHASE3B_PPF_RANGE used

Assessment:
- Over-advanced state
- Likely routing drift

Verdict: DEFECT

---

## Case 2 — Jetour T5 2024 ceramic

Expected:
- Year already known
- Model unclear → ask model clarification ONLY

Actual:
- Asked to confirm year again

Assessment:
- Violates carry-forward rule (year must not be re-asked)

Verdict: DEFECT

---

## Case 3 — BMW 2022 PPF

Expected:
- Missing model → ask model ONLY
- Stay Phase 0–2

Actual:
- Entered Phase 3B pricing-style response

Assessment:
- Qualification bypass
- Phase jump

Verdict: DEFECT

---

## Case 4 — X5 2022 ceramic

Expected:
- Depends on repo rule:
  - If X5 is safe alias → acceptable
  - If ambiguous → must clarify

Actual:
- Treated as BMW X5

Assessment:
- Likely acceptable (X5 exists as canonical model)

Verdict: ACCEPT (pending alias policy confirmation)

---

## Case 5 — PPF or ceramic not sure

Expected:
- Clarify service intent (one question)
- No recommendation framing

Actual:
- Entered recommendation-style response

Assessment:
- Violates Phase 0–2 comparison restriction

Verdict: DEFECT

---

## Case 6 — Arabic vague service

Expected:
- Same as above → clarify service OR vehicle

Actual:
- Jumped to vehicle qualification

Assessment:
- Acceptable but not optimal
- Lower severity

Verdict: MINOR DRIFT

---

## Case 7 — Invoice + location

Expected:
- Detect post-service support
- Route to human/admin support
- Do not mix with normal biz info flow

Actual:
- Only answered location

Assessment:
- Violates post-service support rule

Verdict: DEFECT

---

## SUMMARY

Defects:
- Case 1 (year typo → phase jump)
- Case 2 (year re-ask)
- Case 3 (model missing → price path)
- Case 5 (comparison → recommendation)
- Case 7 (support ignored)

Acceptable:
- Case 4 (alias normalization)

Minor:
- Case 6

Conclusion:
- Phase 0–2 structurally stable
- Requires targeted wording/routing fixes before freeze
- No broad patch required


## Due diligence conclusion

Findings after authority + wiring inspection:

1. Support routing phrase exists in PHASE4_6_HUMAN_PHRASE_LIBRARY.md
2. YEAR_ONLY phrase exists and Assembly YEAR_ONLY stop exists
3. Comparison phrases and comparison clarifier phrases exist
4. Business info hard override exists early in Assembly
5. No post_service_support hard override was found in Assembly before business info routes

Interpretation:
- Support defect is primarily an Assembly precedence issue
- Invalid-year defect is primarily a Qualification output-shape issue
- Comparison drift is likely precedence / route-selection drift, not missing phrase content
- Broad patch is not justified
- Minimal likely patch scope:
  - QUALIFICATION_ENGINE.md
  - PHASE4_8_MESSAGE_ASSEMBLY_MAP.md


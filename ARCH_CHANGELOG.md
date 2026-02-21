# ARCH_CHANGELOG.md

## Format (required)
- Date:
- Files:
- Changed:
- Why:
- UAT:

---

## Entries

- Date: 2026-02-21
- Files: MULTIPLE
- Changed: Updated UAT runner and context reset prompt during UAT stabilization / tooling hardening
- Why: Prevent patch drift and ensure deterministic UAT + consistent prompt behavior
- UAT: UAT_CASES_FILE=tests/uat_cases.json python runner/run_uat.py

- Date: 2026-02-21
- Files: MULTIPLE
- Changed: Replaced VEHICLE_DETAILS_PROVIDED with SERVICE_CONFIRMED in SERVICE_CONFIRMED_CARRY_FORWARD
- Why: Avoid non-canonical request_type enum; preserve routing integrity
- UAT: Phase0_2_surface_suite (run_uat.py to be executed next)
tail -n 30 ARCH_CHANGELOG.md

- Date: 2026-02-21
- Files: tests/uat_cases.json
- Changed: Replaced minimal UAT file with Phase 0–2 surface suite
- Why: Lock Phase 0–2 routing and qualification behavior before Phase 3B work
- UAT: python runner/run_uat.py

- Date: 2026-02-21
- Files: PHASE4_6_HUMAN_PHRASE_LIBRARY.md, runner/context_reset_prompt.txt
- Changed: Removed non-canonical services (e.g., VLT, interior detailing) from L.2 browsing overview. Added HARD acronym rule to prevent invented acronyms in Phase 0–2.
- Why: Browsing UAT exposed contamination where the model introduced VLT without user input. This patch locks Phase 0–2 service surface to canonical services only.
- UAT: tests/uat_cases.json → p0_browsing_generic_services (Passed 6/6)

Date: 2026-02-21
- Files: tests/uat_cases.json
- Changed: Added SAFE/AMBIGUOUS/digits-only vehicle alias Phase 0–2 UAT coverage
- Why: Protect vehicle repo rules (no guessing) + prevent regressions
- UAT: UAT_CASES_FILE=tests/uat_cases.json python runner/run_uat.py

- Date: 2026-02-21
- Files: MULTIPLE
- Changed: Phase 0–2 stabilization guardrails + UAT harness hardening (request_type enums, JSON validation, Phase 0–2 regression coverage).
- Why: Prevent patch drift and ensure Phase 0–2 routing remains stable (greeting/browsing/service-confirmed/price-hold/vehicle alias behavior).
- UAT: UAT_CASES_FILE=tests/uat_cases.json python runner/run_uat.py

	Date: 2026-02-21
- Files: MULTIPLE
- Changed: Added phrase-authority-gate (pre-commit) + checker script to prevent duplicate (AUTHORITATIVE) blocks in PHASE4_6_HUMAN_PHRASE_LIBRARY.md.
- Why: Prevent multiple “official SOP” script blocks from causing inconsistent routing and customer responses (patch drift control).
- UAT: pre-commit run phrase-authority-gate (and UAT_CASES_FILE=tests/uat_cases.json python runner/run_uat.py)
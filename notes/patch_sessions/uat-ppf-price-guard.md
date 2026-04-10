# PATCH SESSION

Patch stream: uat-ppf-price-guard

Patch type:
- supporting patch only

Problem observed:
- PPF price-ready UAT could pass while still allowing bad generated outputs
- Drift included:
  - cross-service leakage in PPF pricing
  - repeated coverage clarification
  - generic booking / warranty / options follow-ups
  - free-generation behavior when Route E phrase selection was not enforced in the harness

Why runtime was not patched:
- locked runtime authority was inspected
- PHASE3B_PPF_RANGE exists and Route E already points to it
- issue was isolated to tooling / harness control rather than runtime authority text

Target files:
- runner/context_reset_prompt.txt
- tests/uat_cases.json
- notes/patch_sessions/uat-ppf-price-guard.md

What this patch does:
- tightens runner prompt control for PPF price-ready flow
- forces PHASE3B_PPF_RANGE selection in the harness for the verified PPF price-ready case
- blocks extra post-phrase follow-up questions in that flow
- adds a strict no-drift regression case for BMW X5 2025 full PPF price-ready behavior

Validation run:
- python runner/run_uat.py --cases tests/uat_cases.json
- result: Passed=17, Failed=0, Total=17
- verified:
  - selected_phrase_id = PHASE3B_PPF_RANGE
  - no extra booking/details/options question in strict case
  - Arabic and English blocks both present

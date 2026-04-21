# GAP-TR-004 — Router-only narrowed working note (2026-04-20)

## Scope
Phase 5 polishing L1 misrouting into PPF

## What was tested
- Duplicate polishing authority block existed in:
  - runner/context_reset_prompt.txt
- Duplicate block removed (lines 952–1029)
- Focused UAT run:
  UAT_CASES_FILE="tests/uat/phase5_polish_verbatim_strict_v1.json" python runner/run_uat.py

## Result
- Passed: 1
- Failed: 2

### Failures
1. polish_phase5_expectation_verbatim_strict
   → expected: PHASE5_POLISH_EXPECTATION_DEEPEN_L1
   → actual:   PHASE5_PPF_PRICE_GAP_DEEPEN_L1

2. polish_phase5_exit_fork_verbatim_strict
   → expected: PHASE5_POLISH_EXIT_FORK_L3
   → actual:   PHASE5_PPF_EXIT_FORK_L3

### Pass
- polish_phase5_narrow_verbatim_strict
  → correct: PHASE5_POLISH_NARROW_L2

## Conclusion
- Duplicate polishing block was NOT the root cause
- Active defect remains in:
  runner/context_reset_prompt.txt
- Specifically inside:
  PHASE 5 SERVICE-OWNER ROUTER

## Observed Behavior Pattern
- objection_repeat_count == 2 → correct routing (polish)
- objection_repeat_count == 1 → misroutes to PPF
- objection_repeat_count >= 3 → misroutes to PPF

→ indicates partial override or priority conflict at router level

## Constraints (DO NOT VIOLATE)
- Do NOT add new polishing authority blocks
- Do NOT modify phrase library
- Do NOT widen scope beyond router
- Single authority must remain:
  PHASE 5 SERVICE-OWNER ROUTER

## Next Step
- Patch ONLY the router block
- Ensure polishing branch fully overrides PPF routing
- Validate ONLY with focused polish UAT pack

## Evidence
- tests/reports/uat_report_20260420_050331.json

---

## Follow-up confirmation after gap-register review

Gap register confirmation:
- `docs/master_architecture/08_ARCHITECTURE_GAP_REGISTER.md` already records:
  - `GAP-TR-004 — PHASE5 POLISH L1 MISROUTING INTO PPF`
  - broader Phase 5 non-PPF collapse history
  - duplicate-authority risk from additional prompt-bridge patching
  - cross-service contamination / precedence leak interpretation

Restored-checkpoint validation:
- runtime restored to checkpoint commit baseline
- focused trusted polish run still reproduces:
  - `polish_phase5_expectation_verbatim_strict`
  - actual `selected_phrase_id = PHASE5_PPF_PRICE_GAP_DEEPEN_L1`

Interpretation:
- this is a known unresolved defect family, not a new discovery
- duplicate polishing authority was not root cause
- explicit L1 workaround exists but is not boundary-safe yet
- issue should remain classified as:
  - confirmed unresolved
  - owner = `runner/context_reset_prompt.txt`
  - defect type = cross-service precedence / router leak

Control decision:
- do NOT continue ad-hoc patch looping in this session
- keep restored checkpoint baseline
- defer next fix attempt until a tighter owner-isolated patch plan is prepared

Evidence:
- `tests/reports/uat_report_20260420_140738.json`
- `docs/master_architecture/08_ARCHITECTURE_GAP_REGISTER.md`

# RUNTIME PROJECT TEST INVENTORY — 2026-04-23

## Purpose
Track what is currently working in the clean runtime project, separately from UAT/governance evidence.

## Results

### PPF
1. Input:
   ppf camry 2022 front
   Result:
   - PASS
   - coverage not re-asked
   - driving-pattern question asked
   Classification:
   - CORE-SAFE

2. Input sequence:
   ppf camry 2022 front
   city
   Result:
   - FAIL
   - system asked optional comparison-focus question instead of moving to price-ready
   Classification:
   - EDGE ISSUE
   Reading:
   - narrow PPF Phase 3A overflow / Q3 mis-trigger

### Ceramic
3. Input:
   ceramic camry 2022
   Result:
   - PASS
   - CERAMIC_GOAL asked correctly
   Classification:
   - CORE-SAFE

4. Input sequence:
   ceramic camry 2022
   long term protection
   Result:
   - PASS
   - CERAMIC_WASH_PATTERN asked correctly
   Classification:
   - CORE-SAFE

## Rule
- Runtime-project results must not be mixed with runner/UAT outcomes without explicit comparison.


## PATCH ATTEMPT — PPF Q3 OVERFLOW

Patch target:
- QUALIFICATION_ENGINE.md
- tightened grouping for optional PPF_COMPARISON_FOCUS trigger

Result:
- Q3 misfire no longer appeared in the narrow UAT lane
- but the case still failed
- new observed failure:
  - coverage was re-asked instead of moving to price-ready

Conclusion:
- patch removed one visible symptom but did not resolve the true completion / carry-through defect
- do not continue qualification-engine patching until runtime-signal completion enforcement is audited



## CARRY-THROUGH AUDIT RESULT — PPF PRICE-READY

Finding:
- completed PPF qualifiers are present in runtime signals:
  - PPF_COVERAGE_INTENT
  - PPF_DRIVING_PATTERN
- runner prompt clearly says completed service-specific keys must not re-open Phase 3A
- however direct next-step bridge is only explicitly strong for request_type == PRICE_REQUEST
- narrow failing case used request_type == SERVICE_CONFIRMED

Conclusion:
- remaining defect is now classified as prompt-bridge completion enforcement gap
- not a pure qualification-engine defect
- next safe patch target should be runner/context_reset_prompt.txt


## UAT / RUNNER BRIDGE READING — PPF NARROW LANE

Summary:
- clean runtime project showed:
  - PPF first-turn front capture behaved correctly
  - ceramic upstream qualifiers behaved correctly
- narrow UAT / runner lane did not stay aligned with the same runtime reading

Observed:
- one patch attempt removed optional Q3 misfire but exposed coverage re-ask
- next bridge patch attempt over-corrected and forced early price jump on first turn
- this indicates runner/context_reset_prompt.txt is not a stable rollout-truth surface for this narrow lane

Control decision:
- classify this lane as runner/UAT bridge drift
- do not treat current narrow UAT bridge behavior as runtime patch authority
- do not upload runtime changes to assistants from this bridge evidence
- use clean runtime-project behavior as the current rollout-reading surface

Rollout reading:
- PPF core runtime lane remains usable for controlled progression
- narrow carry-through defect is not closed in UAT bridge lane
- further work here belongs to tooling / bridge stabilization, not immediate runtime-file patching

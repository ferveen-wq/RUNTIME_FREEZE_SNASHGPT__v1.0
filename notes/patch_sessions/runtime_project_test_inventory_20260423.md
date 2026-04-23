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

# RUNTIME PROJECT REVALIDATION TRACKER

Purpose:
Track the current Project UAT rollout validation using the uploaded runtime file set.

Rule:
- Project UAT behavior is the current rollout truth.
- UAT runner is secondary.
- Governance/control docs are decision support, not runtime behavior.
- Do not patch during smoke testing unless the issue is a blocker.

Status meanings:
- PASS = behavior acceptable for rollout
- FAIL = blocker or clear flow defect
- POLISH = usable, but needs later tone/style cleanup
- HOLD = needs investigation before action

Issue types:
- Flow
- Missing context
- Wrong service
- Wrong price
- Extra question
- Style/tone
- Language order
- Governance/source wiring

## Current Upload Set Reading

Current Project UAT source set:
- runtime behavior files uploaded
- engines uploaded
- parameters/repositories uploaded
- phrase/message assembly uploaded
- heavy governance/audit files excluded unless explicitly runtime-safe

Known decision:
- Do not upload governance-heavy files that trigger audit/refusal behavior.
- Do not load Phase 5 closing/handover files during Phase 0–4 validation unless Phase 5 testing starts.

## Phase Revalidation Board

| Phase | Test Area | Status | Notes |
|---|---|---|---|
| Phase 0–2 | Intake / service detection / vehicle capture | PENDING | Start here |
| Phase 3A | Qualification questions | PENDING | After Phase 0–2 |
| Phase 3B | Price release after qualification | PENDING | After Phase 3A |
| Phase 4 | Objection handling | PENDING | Expensive / compare / later |
| Phase 5 | Closing / handover | HOLD | Only after Phase 0–4 stable |
| Phase 6 | Service canon support | PENDING | Check no canon overtalk |

## Test Log

| ID | Phase | Input | Expected | Actual | Status | Issue Type | Action |
|---|---|---|---|---|---|---|---|
| PENDING | Phase 0–2 |  |  |  |  |  |  |

## Rules During Testing

1. Log results first.
2. Do not patch from one isolated failure unless it is a blocker.
3. Style issues go to POLISH, not immediate patch.
4. Flow blockers only:
   - wrong service
   - wrong price
   - skipped required qualifier
   - price too early
   - context lost
   - invention/audit refusal in customer chat
5. After each phase, decide:
   - continue
   - fix blocker
   - hold

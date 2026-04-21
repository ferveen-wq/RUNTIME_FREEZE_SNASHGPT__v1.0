# Family A Evidence Index — 2026-04-20

## Family
Phase 5 / cross-service / router-precedence collapse family

## Active members
- GAP-TR-004
- GAP-TR-006

## Historical related members
- GAP-031
- GAP-030
- GAP-029
- GAP-028

## Stable truths
- GAP-TR-004 is the current active Phase 5 polishing L1 misroute
- GAP-TR-006 is a separate active Phase 4 ceramic → PPF leak
- ceramic Phase 5 trusted pack has passed in trusted mode
- polish Phase 5 may be improved locally, but boundary safety is not yet proven
- PPF narrow L2 wording issue is non-runtime
- duplicate-authority removal was not root cause for GAP-TR-004

## Historical conclusions that are superseded
- broad “all non-PPF Phase 5 collapse” framing
- ceramic and polishing treated as one unresolved live defect without narrowing
- duplicate polishing authority treated as root cause

## Relevant evidence files
- docs/master_architecture/08_ARCHITECTURE_GAP_REGISTER.md
- notes/patch_sessions/gap_tr004_router_only_working_note_20260420.md
- notes/patch_sessions/gap_family_map_20260420.md
- notes/patch_sessions/gap_tr_operational_map_20260420.md
- notes/evidence_audits/tier_revalidation/TIER3_PPF_PHASE5_BRANCH_COLLAPSE_20260419.md
- notes/evidence_audits/tier_revalidation/TIER3_PPF_NARROW_CONTRACT_MISMATCH_20260419.md
- notes/evidence_audits/tier_revalidation/TIER3_CERAMIC_PHASE5_VERBATIM_PASS_20260419.md
- notes/evidence_audits/tier_revalidation/TIER3_POLISH_PHASE5_VERBATIM_PASS_20260419.md

## Relevant reports
- tests/reports/uat_report_20260420_140738.json
- tests/reports/uat_report_20260420_140055.json
- tests/reports/uat_report_20260420_140309.json
- tests/reports/uat_report_20260420_140322.json
- tests/reports/uat_report_20260420_140348.json

## Relevant commits
- e26fff8 — runtime: fix phase5 ceramic and polish service-owner routing
- 87b02c3 — gap-tr004: router priority patch partial improvement (2/3 pass, L1 still leaking)
- 9f11082 — runner: restore ppf phase5 branch routing and record narrow-l2 contract mismatch
- 4410efd — phase5: add polishing negotiated objection routing and bridge guards
- bc0bb60 — phase5: fix ceramic verbatim render lock + remove PPF leakage + enforce phase3B→phase5 continuity

## Known unsafe / non-final patch patterns
- adding parallel authority blocks
- patching prompt bridge without owner isolation
- treating focused improvement as boundary-safe fix
- reopening superseded broad non-PPF collapse frames as active truth

## Likely owner lanes
- GAP-TR-004:
  - runner/context_reset_prompt.txt
  - Phase 5 service-owner router
- GAP-TR-006:
  - likely Phase 4 mapping / phrase-selection authority
  - should not be assumed identical to GAP-TR-004 owner without proof

## Do-not-repeat rules
- do not treat Family A as brand-new for each member
- do not patch GAP-TR-006 with Phase 5 router assumptions
- do not mix runtime defects with test-contract defects
- do not use historical broad collapse claims as current control truth

## Safe next move
- keep GAP-TR-004 and GAP-TR-006 under the same family umbrella
- investigate them with separate owner isolation
- use this file before any new Family A patch planning

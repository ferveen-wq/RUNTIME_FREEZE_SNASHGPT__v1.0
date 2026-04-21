# GAP-032 Blocker Note — 2026-04-20

## Decision

Further Phase 5 routing edits are blocked until repeat-count source of truth is chosen.

## Why

Current evidence confirms a contract mismatch across authorities:

- OBJECTION_RESOLUTION_ENGINE:
  - 0 = first occurrence
  - 1 = second occurrence
  - 2 = third occurrence or more

- PHASE4_8_MESSAGE_ASSEMBLY_MAP:
  - <= 1 = L1
  - 2 = L2
  - >= 3 = L3

- Current UAT packs:
  - 1 = L1
  - 2 = L2
  - 3 = L3

## What today proved

- Phase 5 ownership cleanup was useful
- competing side selectors were real
- GAP-TR-004 polish L1 target now passes under central-owner cleanup

But remaining Phase 5 failures still point to unresolved repeat-count contract mismatch:
- ceramic L2 hold failure
- PPF L2 hold failure
- earlier L3 instability history

## Control decision

Do NOT continue local router patching as if it is the final fix.

Treat:
- GAP-032 as active blocker for further Phase 5 routing reconciliation
- ownership-shape cleanup as partial progress only
- repeat-count authority selection as the next required planning step

## Next required decision

Choose one single source-of-truth model for objection_repeat_count:

Option A:
- 0 = first
- 1 = second
- 2 = third+

Option B:
- 1 = first
- 2 = second
- 3 = third+

After that:
- align objection engine
- align assembly map
- align runtime prompt
- align UAT packs
- then rerun Phase 5 validation

## Related evidence

- docs/master_architecture/08_ARCHITECTURE_GAP_REGISTER.md
- notes/evidence_audits/tier_revalidation/TIER3_PPF_NARROW_CONTRACT_MISMATCH_20260419.md
- notes/patch_sessions/gap_tr004_patch_plan_v1_20260420.md
- tests/reports/uat_report_20260420_195715.json
- tests/reports/uat_report_20260420_195729.json

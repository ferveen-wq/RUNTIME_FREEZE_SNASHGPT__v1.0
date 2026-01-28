# PHASE 0 LOCK INDEX (AUTHORITATIVE)

This file is the single source of truth for all Phase 0 locks.
All engines, runtime orchestration, and audits must reference this file only.

---

## PHASE 0 — INITIAL MANIFEST & RUNTIME CORE LOCK

Date: 2026-01-05  
Phase: 0  
Status: LOCKED  

Locked Artifacts:
- MANIFEST.md
- RUNTIME_CORE_BUNDLE.md

Notes:
- Runtime execution order finalized
- Core bundle stabilized
- No structural drift allowed without Phase 0 unlock

---

## PHASE 0 — PRODUCT & SERVICE AUTHORITY LOCK

Date: 2026-01-08  
Phase: 0  
Version: 1.0  
Status: LOCKED  

Locked Artifacts:
- PRODUCT_SERVICE_CANON.md
- GLOBAL_PRODUCT_NAMING_REGISTRY_v1.0.md
- GLOBAL_VEHICLE_CLASSIFICATION_REPOSITORY.md
- PHASE_0__GOVERNANCE.ini

Integrity Notes:
- ROOF_ONLY PPF is an approved coverage variant
- Dedicated ROOF_PPF SKUs are intentionally not required at Phase 0
- Manual confirmation or ladder mapping is permitted
- No contradiction exists between Canon and Naming Registry

Change Note:

- 2026-01-10 — RUNTIME_STATE_MACHINE.md bumped to v1.0.1 (Phase 4 terminal governance integration)
  - Added FINAL_CONVERSATION_STATE + AUTOMATION_TERMINATED_FLAG + HANDOVER_REQUIRED_FLAG governance fields
  - Added mapping rules from Phase 4 terminal states → CONVERSATION_STATUS
  - Added enforcement in ACTIVE: block engines when CLOSED/TERMINATED; stop on handover
 - Added NEW SESSION rule for customer re-engagement after termination (Phase 4 governed)
  - Reason: prevent zombie sessions and enforce Phase 4 finality (no automation resume)
  - Phase 0 locked — Product & Service authority finalized.
  - No further service drift allowed without explicit Phase 0 unlock.

Authority:
- Phase 0 is final authority for services, naming, and eligibility
- All downstream engines must comply
---

## PHASE 4 — CLOSING & HANDOVER (REFERENCE ONLY)

Date: 2026-01-10  
Phase: 4  
Status: LOCKED  

Reference Notes:
- Phase 4 governs FINAL conversation states only
- Automation termination is irreversible within a session
- Human handover is enforced and final
- Detailed lock record exists in PHASE4_LOCK_INDEX.md

Authority:
- Phase 4 changes require Phase 0 approval
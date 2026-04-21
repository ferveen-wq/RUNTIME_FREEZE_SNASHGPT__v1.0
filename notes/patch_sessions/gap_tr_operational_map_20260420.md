# GAP-TR Operational Map — 2026-04-20

## GAP-TR-004
Family:
- Family A — router / precedence / cross-service collapse

Current status:
- OPEN
- active planning target

Failure type:
- runtime routing defect
- Phase 5 service-family ownership leak

Observed behavior:
- polishing L1 misroutes into `PHASE5_PPF_PRICE_GAP_DEEPEN_L1`

Likely owner:
- `runner/context_reset_prompt.txt`
- specifically `PHASE 5 SERVICE-OWNER ROUTER`

Related historical gaps:
- GAP-031
- GAP-030
- GAP-029
- GAP-028

Evidence:
- `tests/uat/phase5_polish_verbatim_strict_v1.json`
- `tests/reports/uat_report_20260420_140738.json`
- `notes/patch_sessions/gap_tr004_router_only_working_note_20260420.md`

Known non-root / non-final attempts:
- duplicate polishing authority removal was not root cause
- explicit L1 workaround improved focused result but was not boundary-safe

Do not repeat:
- do not add parallel polishing authority blocks
- do not widen scope beyond router without owner proof
- do not treat old broad non-PPF collapse frames as active truth

Safe next move:
- owner-isolated router planning only
- no runtime patch until boundary-safe plan is defined

---

## GAP-TR-005
Family:
- Family C — phase/debug mismatch

Current status:
- OPEN

Failure type:
- phase boundary violation
- debug/phase inconsistency

Observed behavior:
- ceramic brand fixation escalates to Phase 5 phrase while debug phase remains 0

Likely owner:
- phase boundary / assembly / debug contract interaction
- not yet proven as same owner as Family A

Related historical gaps:
- possible overlap with GAP-028 / GAP-027 / GAP-026

Evidence:
- `tests/uat/phase4_ceramic_brand_fixation_strict_v2.json`

Do not repeat:
- do not classify as pure cross-service leak without phase-boundary proof

Safe next move:
- isolate phase/debug owner separately from router-precedence family

---

## GAP-TR-006
Family:
- Family A — router / precedence / cross-service collapse

Current status:
- OPEN

Failure type:
- runtime mapping / phrase selection defect
- cross-service leakage

Observed behavior:
- ceramic price resistance routes to `PHASE4_PPF_PRICE_PRESSURE_L1`

Likely owner:
- phase 4 service-family mapping / precedence layer

Related historical gaps:
- Family A historical set
- especially earlier ceramic→PPF leakage traces

Evidence:
- `tests/uat/phase4_ceramic_price_resistance_strict_v2.json`

Do not repeat:
- do not treat as same exact patch shape as GAP-TR-004 without phase-specific owner proof

Safe next move:
- investigate as Family A related, but keep Phase 4 owner isolation separate from Phase 5 router work

---

## GAP-TR-007
Family:
- Signal classification family

Current status:
- OPEN

Failure type:
- objection mapping / signal classification defect

Observed behavior:
- PPF technical question routes to brand fixation lane

Likely owner:
- objection classification / signal mapping layer

Evidence:
- `tests/uat/phase4_ppf_technical_sensitivity_strict_v2.json`

Do not repeat:
- do not treat as router-precedence defect unless later evidence proves that

Safe next move:
- isolate objection-signal mapping owner before runtime patching

---

## Family-wide control rules

### Family A
Includes:
- GAP-TR-004
- GAP-TR-006
- historical related: GAP-031 / GAP-030 / GAP-029 / GAP-028

Shared pattern:
- cross-service collapse
- service-family precedence instability
- local patching may improve one lane without being boundary-safe

Rule:
- do not reopen historical family members as new isolated defects
- use them as evidence only

### Family C
Includes:
- GAP-TR-005

Rule:
- keep separate from router-precedence work until owner is proven shared

### Signal-classification family
Includes:
- GAP-TR-007

Rule:
- keep separate from router and phase-boundary defects

---

## Non-runtime exclusions
- PPF narrow L2 wording issue = test-contract mismatch
- Phase4 PPF silence request_type issue = debug contract only


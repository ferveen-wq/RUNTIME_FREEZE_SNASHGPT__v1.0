# RUNTIME PATCH CANDIDATES — DEFERRED UNTIL DUE DILIGENCE

Status: documentation phase only
Date: 2026-04-13
Rule: do not patch locked runtime files yet.
Purpose: capture confirmed runtime patch candidates identified during architecture documentation, without creating premature or duplicate runtime edits.

---

## 1. Current working mode

We are currently:
- documenting architecture
- confirming ownership boundaries
- aligning runtime vs assistant-facing layers
- recording evidence-backed runtime gaps

We are NOT currently:
- patching locked runtime logic
- introducing new runtime authority
- resolving implementation details without due diligence

---

## 2. Confirmed runtime patch candidate

### Primary candidate
- `00__LOCKED__UPLOAD_SET/00__Runtime/CUSTOMER_CHAT_INTAKE_RULES.md`

### Why it is a candidate
The file accepts screenshots, pasted chats, short messages, and text-converted voice notes,
but it does not yet explicitly enumerate assistant-fed operational updates strongly enough,
despite supporting evidence elsewhere in runtime and contract materials.

### Evidence already found
Supporting references indicate the architecture expects intake/runtime awareness for:
- confirmed call / visit / WhatsApp audio summary containing customer response
- assistant-only notes vs valid customer-signal updates
- wrong transcript / mixed identity handling
- returning customer re-entry
- new car / new service re-entry
- post-service support intake-only routing
- pasted history without state rollback

Supporting files already identified:
- `00__LOCKED__UPLOAD_SET/00__Runtime/RUNTIME_EXECUTION_FLOW.md`
- `00__LOCKED__UPLOAD_SET/01__Engines/SILENCE_HANDLING_ENGINE.md`
- `00__LOCKED__UPLOAD_SET/PHASE 0–2 — SINGLE SOURCE OF TRUTH (CONTRACT + ADDENDUM + FILE MAP).md`
- `00__LOCKED__UPLOAD_SET/discussions on contract 0-2 updates`
- `docs/master_architecture/05_ASSISTANT_OPERATING_MODEL.md`
- `docs/master_architecture/09_ASSISTANT_INTELLIGENCE_LAYER.md`

---

## 3. Candidate runtime gaps to verify later

### 3.1 Assistant-fed operational updates
Possible missing explicit intake acceptance / treatment for:
- call notes with confirmed customer response
- visit notes with confirmed customer response
- WhatsApp audio summaries
- assistant-entered operational status updates tied to actual customer interaction

### 3.2 Identity integrity / wrong-window protection
Possible intake wording gap for:
- wrong transcript pasted into wrong customer window
- mixed identity / mixed ownership paste
- assistant note contamination vs customer signal

### 3.3 Re-entry handling
Possible intake wording gap for:
- returning customer continuation
- new car / new service as clean new context
- silence re-entry without unsafe rollback

### 3.4 Post-service support
Possible intake wording gap for:
- invoice
- complaint
- maintenance
- records / video / support requests
where behavior must remain intake-only + handoff

---

## 4. Patch rule

Do NOT patch any locked runtime file until all of the below are complete:
1. confirm target file role
2. inspect surrounding section
3. check whether equivalent logic already exists nearby
4. confirm no duplicate or competing authority will be created
5. define validation method before patching

---

## 5. Likely validation path later

Expected validation before runtime patch:
- targeted grep review
- local diff inspection
- authority cross-check against:
  - `RUNTIME_LOAD_MANIFEST.md`
  - `KNOWLEDGE__RUNTIME_CORE_BUNDLE.md`
  - `RUNTIME_EXECUTION_FLOW.md`
  - `CUSTOMER_CHAT_INTAKE_RULES.md`
  - `QUALIFICATION_ENGINE.md`
- UAT/manual verification only after minimal scoped patch

---

## 6. Current conclusion

Documentation first was the correct sequence.

Runtime patching is deferred intentionally to avoid:
- duplicate authority
- wrong-file patching
- patch-on-patch drift
- mixing architecture clarification with implementation edits


## Deferred candidate — Wrap authority redesign

Reason deferred:
- Avoid runtime drift from bridge-only fixes.
- Wrap currently has mixed authority across decision matrix, qualification engine, pricing ladder, and assembly routing.

Required before patch:
1. Finalize business decision:
   - full automation vs qualification + handoff
2. Resolve authority conflict:
   - WRAP_SCOPE in PHASE3A_QUALIFICATION_DECISION_MATRIX.md
   - full-vehicle-only rule in QUALIFICATION_ENGINE.md
3. Reuse existing approved handoff/callback pattern if wrap is moved to manual follow-up
4. Only after authority alignment:
   - patch assembly map
   - patch prompt bridge
   - patch/add tests

Current safe state:
- Stop wrap runtime expansion here.
- Keep existing validated evidence only.

## Wrap decision finalized

Chosen path:
- Qualification + manual handoff after finish/basic price-stage

Do next:
1. align authority files to one-way wrap flow
2. prevent deep wrap automation beyond approved handoff point
3. reuse one approved handoff pattern only
4. validate with dedicated wrap UAT after authority patching

## Wrap runtime blockage after handoff alignment

Blocked state:
- WRAP_FINISH provided in runtime_signals is still not honored reliably
- Runtime re-asks PHASE3A_Q_WRAP_FINISH
- Approved handoff behavior does not trigger

Rule:
- Do not continue blind prompt/bridge patching for wrap in this branch without deeper runtime execution analysis


--------------------------------------------------
TEMP GAP REGISTER — PHASE 0–3 (EVIDENCE-ONLY)
--------------------------------------------------

Purpose:
- Capture ONLY gaps derived from real evidence (chat pages, UAT, runtime behavior)
- No invention
- No compression assumptions
- No architecture decisions here

Rules:
- Every gap MUST be backed by evidence
- Do NOT merge with original gap register yet
- Do NOT update runtime files from this document directly
- This file is TEMPORARY working memory

--------------------------------------------------
HARNESS GAPS
--------------------------------------------------

HARNESS_001 — Fake-green loop / unreliable fail detection
Source:
- 11 apr.txt (strict_raw introduction cluster)
Evidence:
- strict_raw added to expose real failures
- earlier UAT passes not trustworthy
Impact:
- runtime patches were based on incorrect signals

HARNESS_002 — Report / debug inconsistency
Source:
- UAT reports (phase mismatch, price_ladder_state anomalies)
Evidence:
- phase mismatch (Phase 5 vs Phase 3B)
- invalid ladder state values
Impact:
- misinterpretation of runtime behavior

HARNESS_003 — Stateless multi-turn behavior
Source:
- 11 apr.txt (multi-turn harness discussion)
Evidence:
- each turn treated as fresh
- no true conversation continuity
Impact:
- Phase 4 testing unreliable

--------------------------------------------------
RUNTIME GAPS
--------------------------------------------------

RUNTIME_001 — Phase 0–2 not fully runtime-proven
Source:
- SECTION 05A evidence
Evidence:
- described as UAT-aligned but not pure runtime proof
- partially stabilized via harness
Impact:
- possible hidden dependency on harness

RUNTIME_002 — Deferred behavioral logic
Source:
- Phase 0–2 uncertainty lines
Evidence:
- question-friction handling deferred
- pricing discipline incomplete
- adaptive qualification not finalized
Impact:
- may affect later phase transitions

--------------------------------------------------
ALIGNMENT GAPS
--------------------------------------------------

ALIGN_001 — Runtime vs Harness vs Production mismatch
Source:
- Phase 3 harness vs runtime discussion
Evidence:
- harness shaping behavior
- production model stateless-by-design
Impact:
- risk of implementing non-production logic

--------------------------------------------------
COVERAGE GAPS
--------------------------------------------------

COVERAGE_001 — Service validation was PPF-led
Source:
- Phase 3 checkpoint discussion
Evidence:
- initial stabilization focused on PPF
- later non-PPF sweep required
Impact:
- initial Phase 3 completeness overstated

--------------------------------------------------
STATUS
--------------------------------------------------

- TEMP WORKING DOCUMENT
- NOT FINAL
- NOT YET VALIDATED AGAINST:
  - original gap register
  - runtime authority files
  - full architecture

Next Step:
- Continue extracting remaining pages
- Add ONLY evidence-backed gaps
- Do NOT modify architecture yet


--------------------------------------------------
ADDITIONAL GAPS — SOURCE: 9 APR
--------------------------------------------------

Rules:
- Add ONLY if gap is NEW (not already listed)
- Must be backed by evidence
- Do NOT rephrase existing gaps
- Do NOT merge or clean yet

Gap format to follow:

GAP_ID — Short title
Gap class:
- HARNESS / RUNTIME / ALIGNMENT / COVERAGE

Source:
- 9 apr.txt

Evidence:
- (exact observation from page)

Impact:
- (what breaks or becomes unreliable)

Status:
- TEMP (not validated)



GAP_9APR_001 — Patch evidence threshold repeatedly not met
Gap class:
- ALIGNMENT

Source:
- 9 apr.txt

Evidence:
- repeated “do not patch yet”
- repeated “do not patch from memory”
- repeated “do not patch runtime when a supporting patch is enough”

Impact:
- 9 Apr findings cannot be promoted directly into architecture/runtime decisions without later confirmation

Status:
- TEMP (not validated)

---

GAP_9APR_002 — Harness / runner trust too weak for clean defect attribution
Gap class:
- HARNESS

Source:
- 9 apr.txt

Evidence:
- `runner/run_uat.py` repeatedly treated as contamination / observability risk
- runner invocation and smoke-pack trust questioned
- harness could reveal or suppress the same issue depending on constraints

Impact:
- apparent runtime defects on 9 Apr may partly be harness-shaped, reducing confidence in direct runtime patching

Status:
- TEMP (not validated)

---

GAP_9APR_003 — Runtime suspects narrowed but not proven
Gap class:
- RUNTIME

Source:
- 9 apr.txt

Evidence:
- repeated inspection around:
  - `QUALIFICATION_ENGINE.md`
  - `PHASE4_8_MESSAGE_ASSEMBLY_MAP.md`
  - `PRICE_LADDER_ENGINE.md`
- repeated conclusions not to patch engine / assembly yet

Impact:
- 9 Apr identifies suspect files, but does not by itself prove final runtime ownership of the defect

Status:
- TEMP (not validated)

---

GAP_9APR_004 — PPF Phase 3A / YEAR_ONLY / precedence issue family under due diligence
Gap class:
- COVERAGE

Source:
- 9 apr.txt

Evidence:
- repeated references to:
  - `YEAR_ONLY`
  - PPF Phase 3A routing
  - phrase-block / precedence / support-override inspection

Impact:
- possible early instability signal for Phase 0–2 / Phase 3 handoff, but still not final on 9 Apr

Status:
- TEMP (not validated)


---

GAP_9APR_005 — PPF Phase 3A visible defect localized toward phrase-layer drift
Gap class:
- RUNTIME

Source:
- 9 apr.txt

Evidence:
- `QUALIFICATION_ENGINE.md` still selected `PHASE3A_Q_PPF_COVERAGE_INTENT` first
- `PHASE4_8_MESSAGE_ASSEMBLY_MAP.md` still routed that qualifier verbatim
- repeated historical conclusion: observed drift likely sat in phrase wording, not first in engine/routing

Impact:
- visible customer-facing Phase 3A defect may be misdiagnosed as engine or routing failure when the historical evidence was narrowing toward phrase-layer drift

Status:
- TEMP (not validated)

---

GAP_9APR_006 — PPF qualifier wording shape drift from older approved 3-way coverage question
Gap class:
- COVERAGE

Source:
- 9 apr.txt

Evidence:
- repeated references to:
  - older explicit 3-way coverage qualifier
  - narrowed / drifted qualifier wording
  - phrase-block-only inspection and patch direction

Impact:
- customer-facing qualifier may lose the intended full/front/deciding coverage path clarity even while engine/routing keys remain stable

Status:
- TEMP (not validated)

---

GAP_9APR_007 — YEAR_ONLY / precedence discussion present but not yet proven as same root cause
Gap class:
- ALIGNMENT

Source:
- 9 apr.txt

Evidence:
- `YEAR_ONLY` and precedence lines appeared in the same investigation area
- but strongest 9 Apr conclusion still localized the exact PPF defect elsewhere

Impact:
- risk of over-merging adjacent qualification/preference issues into one false root cause

Status:
- TEMP (not validated)



--------------------------------------------------
ADDITIONAL GAPS — SOURCE: 6 APR
--------------------------------------------------

Rules:
- Add ONLY if gap is NEW (not already listed)
- Must be backed by evidence
- Do NOT rephrase existing gaps
- Do NOT merge or clean yet


GAP_6APR_001 — Testing-context noise mixed with runtime investigation
Gap class:
- ALIGNMENT

Source:
- 6 apr.txt

Evidence:
- repeated inside-project vs outside-project testing guidance
- project-context heaviness discussion
- fresh-chat vs same-chat testing method shaping outputs

Impact:
- 6 Apr observations cannot be treated uniformly as runtime evidence without separating testing-environment effects

Status:
- TEMP (not validated)

---

GAP_6APR_002 — Early patch restraint before runtime proof
Gap class:
- ALIGNMENT

Source:
- 6 apr.txt

Evidence:
- repeated “do not patch yet”
- repeated “audit first / inspect first / log first”
- repeated “not approved for rollout patch yet”

Impact:
- 6 Apr findings require later confirmation before any promotion into real architecture decisions

Status:
- TEMP (not validated)

---

GAP_6APR_003 — Assembly surface already suspected as higher-risk than blind engine patching
Gap class:
- RUNTIME

Source:
- 6 apr.txt

Evidence:
- qualification principles described as mostly correct already
- repeated inspection focus on PHASE4_8_MESSAGE_ASSEMBLY_MAP.md
- early concern that assembly may over-explain or override cleaner qualifier flow

Impact:
- early root-cause suspicion points more toward assembly/routing behavior than immediate engine rewrites

Status:
- TEMP (not validated)

---

GAP_6APR_004 — YEAR_ONLY / one-question / qualifier discipline already present as runtime expectation
Gap class:
- COVERAGE

Source:
- 6 apr.txt

Evidence:
- YEAR_ONLY shown as authoritative one-question route
- exactly one qualifier per turn emphasized
- Phase 3A / Phase 3B qualifier discipline surfaced early

Impact:
- later deviations must be checked against this earlier recorded control expectation

Status:
- TEMP (not validated)



--------------------------------------------------
ADDITIONAL GAPS — SOURCE: 2 APR
--------------------------------------------------

Rules:
- Add ONLY if gap is NEW (not already listed)
- Must be backed by evidence
- Do NOT rephrase existing gaps
- Do NOT merge or clean yet



GAP_2APR_001 — Memory recovery depended on chat reconstruction before file-truth re-anchoring
Gap class:
- ALIGNMENT

Source:
- 2apr.txt

Evidence:
- uploaded historical pages were used to reconstruct working method and continuity
- latest-date / file-truth discipline had to be re-established explicitly

Impact:
- risk of rebuilding from chat memory unless runtime/governance files are re-anchored first

Status:
- TEMP (not validated)

---

GAP_2APR_002 — Phase 8 / Phase 9 existed, but orchestration state was only partially reconstructed
Gap class:
- COVERAGE

Source:
- 2apr.txt

Evidence:
- repo-history references showed real Phase 8 / Phase 9 files and commits
- page still described higher orchestration / integration as partial

Impact:
- later-phase architecture can be overstated if repo-history existence is mistaken for full active integration

Status:
- TEMP (not validated)

---

GAP_2APR_003 — Deferred / log-first discipline was necessary to prevent patch-on-patch corruption
Gap class:
- ALIGNMENT

Source:
- 2apr.txt

Evidence:
- repeated defer/log-first/do-not-patch language
- deferred items explicitly tied to ledger/backlog/runtime tracking

Impact:
- unlogged discussions from early pages cannot be promoted safely into architecture decisions

Status:
- TEMP (not validated)

---

GAP_2APR_004 — Authority boundaries were known early, but later docs must still verify active ownership
Gap class:
- RUNTIME

Source:
- 2apr.txt

Evidence:
- qualification → routing → assembly → formatting separation
- single-writer / reader discipline discussed explicitly

Impact:
- later architecture docs must verify active runtime ownership instead of assuming discussion-level ownership is fully wired

Status:
- TEMP (not validated)


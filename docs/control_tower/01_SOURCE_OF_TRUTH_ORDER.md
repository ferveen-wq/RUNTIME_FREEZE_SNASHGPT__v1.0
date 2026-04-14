# 01_SOURCE_OF_TRUTH_ORDER.md

Status: DRAFT
Purpose: Define the order of authority when sources conflict, so the project can continue without memory dependence or duplicate authority.
Scope: Control-tower conflict resolution only. This file does not define runtime behavior itself.

---

## 1. Core Rule

When two sources conflict, the higher-authority source wins.

Chat memory, long-page recollection, or partial reconstruction must never override written project evidence.

---

## 2. Authority Layers

### Layer A — Runtime Behavior Truth (Highest for system behavior)

Use for:
- actual runtime behavior
- routing
- phase flow
- ownership
- state
- message construction
- communication constraints

Primary sources include:
- active runtime files
- runtime authority files
- locked upload-set runtime doctrine

Derived supporting sources:
- architecture docs built from runtime authority

Rule:
- If runtime behavior is in question, runtime-wired files win over all governance, testing, chat-level interpretation, and derived architecture summaries.
- If an architecture doc conflicts with a runtime-wired file, the runtime-wired file wins.

---

### Layer B — Change / Patch Status Truth

Use for:
- whether work is discussed
- whether work is approved
- whether work is patched
- whether work is validated
- whether work is merged
- whether work is deferred

Primary sources:
- `00__LOCKED__UPLOAD_SET/00__Runtime/RUNTIME_CHANGE_LEDGER.md`
- `00__LOCKED__UPLOAD_SET/00__Runtime/PATCH_PROTOCOL.md`
- `00__LOCKED__UPLOAD_SET/00__Runtime/PHRASE_GOVERNANCE_STANDARD.md`

Rule:
- Patch status must come from ledger/protocol/governance records, not from memory or discussion.

---

### Layer C — Governance Enforcement / Audit Support

Use for:
- validation
- audit support
- changelog checks
- phrase authority checks
- runtime diff detection
- architecture scans
- audit wrappers

Primary sources include:
- `.github/workflows/governance*.yml`
- `runner/*`
- `tools/audit/*`
- `tools/control_tower.py`

Rule:
- These files support enforcement and verification.
- They do not by themselves replace runtime authority or patch-status authority.

---

### Layer D — Human Governance / Re-Anchoring

Use for:
- work queues
- behavioral risk logging
- UAT pack inventory
- re-anchoring future sessions
- human governance continuity

Primary sources include:
- `00__LOCKED__UPLOAD_SET/00__Runtime/SNASHGPT_MASTER_GOVERNANCE.md`
- `docs/control_tower/00_FOUNDATION_EVIDENCE.md`
- later control-tower operating docs

Rule:
- These sources are governance-supporting and memory-reducing.
- They are not runtime-wired behavior sources unless explicitly proven otherwise.

---

### Layer E — Historical Reconstruction / Chat Evidence (Lowest)

Use for:
- recovering prior decisions
- locating forgotten workflows
- reconstructing intent behind prior work
- finding evidence not yet normalized into docs

Primary sources include:
- historical chat-page exports
- temp extracts
- reconstruction notes
- discussion summaries

Rule:
- Historical reconstruction may inform investigation.
- It must not become final authority until written evidence is verified and promoted.

---

## 3. Conflict Resolution Rules

### 3.1 Runtime vs Governance
If runtime-wired behavior conflicts with human governance notes:
- runtime-wired behavior wins

### 3.2 Ledger vs Discussion
If ledger status conflicts with chat discussion:
- ledger wins

### 3.3 Protocol vs Assumption
If protocol/governance file says patching cannot proceed:
- patch must stop, even if discussion suggests otherwise

### 3.4 Audit Tool vs Authority File
If an audit tool suggests a concern:
- investigate using runtime/governance authority files
- do not treat the tool output alone as final doctrine

### 3.5 Reconstruction vs Written Evidence
If reconstructed memory conflicts with written evidence:
- written evidence wins

---

## 4. Operational Use

Use this file before:
- drafting new control-tower docs
- promoting temp findings into architecture docs
- assigning patch ownership
- deciding whether an issue is runtime, harness, or governance
- resuming work after long chat gaps

---

## 5. Hard Prohibitions

Do not:
- treat chat memory as official state
- treat discussion as patched status
- treat helper tooling as runtime authority
- let human governance notes override runtime behavior
- create a second authority for behavior already owned elsewhere

---

## 6. Current Verified Examples

Verified from current project evidence:
- runtime behavior truth belongs to active runtime/authority files
- patch/change truth belongs to ledger + protocol + phrase governance
- `tools/control_tower.py` is audit/support tooling, not runtime authority
- `SNASHGPT_MASTER_GOVERNANCE.md` is human governance / re-anchoring, not runtime-wired behavior
- historical reconstruction is useful, but only after verification and promotion

---

## 7. Status Note

This file is derived from:
- `docs/control_tower/00_FOUNDATION_EVIDENCE.md`

It should be revised only when stronger written evidence changes the authority hierarchy.

--------------------------------------------------
PROMOTION TRACKER
--------------------------------------------------

Purpose:
- Track every item promoted from TEMP evidence into real architecture docs
- Prevent duplicate entry, silent compression, and memory-based patching

Rules:
- No item may be promoted without:
  - source temp section
  - reconciliation row
  - target doc
  - duplicate check
  - confidence
- If partially promoted, record that clearly
- If rejected/deferred, record that too

--------------------------------------------------
COLUMNS
--------------------------------------------------

| Tracker ID | Temp Source | Reconciliation Row | Target Doc | Topic | Action | Duplicate Check | Confidence | Status | Notes |
|---|---|---|---|---|---|---|---|---|---|

--------------------------------------------------
ENTRIES
--------------------------------------------------

| PROMO_003 | SECTION 08A / GAP_2APR_004 | ROW_011 | 02_OWNERSHIP_MODEL.md | Runtime authority boundaries remain above UAT / harness behavior | INSERTED | DONE | HIGH | PROMOTED | Added under UAT / Loading Boundary |
| PROMO_004 | SECTION 05B / COVERAGE_001 + ROW_003 | ROW_003 | 04_PHASE_ARCHITECTURE.md | Phase 3 qualifier-first / one-question / ordered gating already present | NO CHANGE | DONE | HIGH | REVIEWED-NO-INSERT | Existing file already covers required architecture truth; UAT/history details not promoted here |
| PROMO_001 | SECTION 05A + 08A | ROW_014 | 01_SYSTEM_OPERATING_MODEL.md | File-truth over memory / chat reconstruction discipline | INSERTED | DONE | HIGH | PROMOTED | Inserted under Runtime Operating Position |
| PROMO_005 | ROW_003, ROW_005, ROW_006, ROW_007, ROW_009, ROW_012 | RECON REVIEW | 08_ARCHITECTURE_GAP_REGISTER.md | Reconciled gap candidates reviewed against existing real gap register | NO CHANGE | DONE | HIGH | REVIEWED-NO-INSERT | Candidates are either harness-only, needs-runtime-check, history/coverage, or overlap existing gaps; keep in temp files for now |
| PROMO_006 | ROW_011 + ROW_013 | REVIEW | 06_MESSAGE_CONSTRUCTION_MODEL.md | Phrase / assembly / formatter boundaries already sufficiently captured | NO CHANGE | DONE | HIGH | REVIEWED-NO-INSERT | Existing file already covers required construction authority; no extra UAT/runtime note needed here |
| PROMO_007 | ROW_011 + ROW_013 + ROW_014 | REVIEW | 03_STATE_MODEL.md | Session continuity must come from explicit carried-forward context, not hidden memory | INSERTED | DONE | HIGH | PROMOTED | Added under Session Re-Engagement Rule |
| PROMO_008 | ROW_011 + ROW_013 + ROW_014 | REVIEW | 07_COMMUNICATION_RULES.md | Customer-facing communication rules already sufficiently capture one-question, no-invention, and production-vs-test fallback behavior | NO CHANGE | DONE | HIGH | REVIEWED-NO-INSERT | Existing file already covers required communication constraints; no extra architecture note needed here |
| PROMO_009 | ROW_011 + ROW_014 | REVIEW | 05_ASSISTANT_OPERATING_MODEL.md | Assistants must rely on explicit context only, not hidden memory or reconstructed assumptions | INSERTED | DONE | HIGH | PROMOTED | Added under Screenshot and Pasted Chat Discipline |
| PROMO_002 | SECTION 05B + 08A | ROW_013 | 01_SYSTEM_OPERATING_MODEL.md | Runtime vs test / harness distinction | INSERTED | DONE | HIGH | PROMOTED | Inserted under Runtime Operating Position |

--------------------------------------------------
STATUS
--------------------------------------------------

- WORKING TRACKER
- USE BEFORE EVERY NEW ARCHITECTURE ENTRY

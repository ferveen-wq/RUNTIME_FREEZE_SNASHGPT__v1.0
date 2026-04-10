# PATCH SESSION

Patch stream: phase3a-ppf-coverage

Problem observed:
- PPF Phase 3A coverage question drifted from the older explicit coverage-shape wording.
- Current phrase no longer explicitly offered front protection, while engine normalization and decision matrix still expected coverage-first branching.

Evidence:
- current PHASE3A_Q_PPF_COVERAGE_INTENT phrase differed from pre-2026-02-26 baseline
- decision matrix still defined whole car / front-impact-areas / still deciding
- qualification engine still selected PHASE3A_Q_PPF_COVERAGE_INTENT first
- assembly map still routed the Phase 3A qualifier verbatim from phrase library
- focused UAT after patch showed coverage-led behavior, not usage-first

Target file:
- 00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_6_HUMAN_PHRASE_LIBRARY.md

File role:
- supporting patch

Why this file owned the issue:
- routing and engine behavior already pointed to the same Phase 3A qualifier
- the observed drift was in the wording of the phrase block itself
- phrase wording was no longer aligned with decision matrix normalization expectations

Existing logic checked:
- PHASE4_6_HUMAN_PHRASE_LIBRARY.md
- PHASE3A_QUALIFICATION_DECISION_MATRIX.md
- PHASE4_8_MESSAGE_ASSEMBLY_MAP.md
- QUALIFICATION_ENGINE.md
- RUNTIME_CHANGE_LEDGER.md

Validation run:
- direct selector script: passed
- targeted diff review: clean
- focused UAT pack: passed
- report checked manually: coverage-led behavior confirmed

Notes:
- Keep this patch isolated as phrase-layer restoration only
- Do not mix later price-path issues into this patch stream


## Price Trace Contract Missing — 2026-04-27

Finding:
- Runtime correctly describes pricing chain:
  CANONICAL_MODEL → VCB → SKU → PRICE_TABLE
- But DEBUG_OUTPUT does NOT expose:
  - CANONICAL_MODEL
  - VCB
  - selected_skus
  - price_source_rows

Impact:
- UAT can only validate final price text, not the source path
- False positives possible (Camry passed without proof)
- Failures (Civic) cannot be traced to exact break point

Architecture Decision:
- Add mandatory price trace fields to DEBUG_OUTPUT
- Do NOT proceed with further pricing UAT until trace is visible

Required fields:
- CANONICAL_MODEL
- VCB
- selected_skus
- price_source_rows

Status:
- BLOCKER for rollout-quality pricing validation


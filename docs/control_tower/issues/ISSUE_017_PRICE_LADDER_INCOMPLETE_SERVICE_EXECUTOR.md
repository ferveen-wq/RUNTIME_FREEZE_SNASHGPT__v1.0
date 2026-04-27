# ISSUE_017 — PRICE_LADDER_ENGINE incomplete service executor

## Pattern Name
Pricing Engine Service Execution Gap

## Observation
PRICE_LADDER_ENGINE.md has pricing discipline, output format rules, and terminal state rules, but it only has explicit executable pricing paths for:
- WRAP
- ROOF_PPF_BLACK_GLOSS

It does not clearly implement executable SKU → price lookup paths for:
- PPF full body
- Ceramic
- Tint
- Polishing

## Evidence
- PPF front was fixed only after adding a special SKU output contract.
- PPF full body initially returned transition-only wording before assembly enforcement.
- Ceramic remains IN_PROGRESS and does not expose price.
- Tint exposes price but leaves price_ladder_state as IN_PROGRESS.
- Polishing exposes price correctly, likely through model inference rather than a fully declared ladder execution path.

## Actual Risk
UAT may pass or partially pass because the model infers pricing from loaded tables, not because the pricing engine has deterministic service execution logic.

## Expected Architecture
- SKU_SELECTION_MATRIX selects SKU(s).
- PRICE_TABLE_VAT_INCL provides approved prices.
- PRICE_LADDER_ENGINE reads selected SKU(s), renders approved price/range, and sets price_ladder_state correctly.
- PHASE4_8_MESSAGE_ASSEMBLY_MAP merges ladder output into customer response.

## Required Fix Direction
Add a generic selected-SKU input/output contract between SKU_SELECTION_MATRIX and PRICE_LADDER_ENGINE, or explicitly implement service pricing paths in PRICE_LADDER_ENGINE without duplicating SKU authority.

## Status
OPEN — must resolve before Phase 4 objection validation and before rollout price trust.

## Decision — 2026-04-27

Resolution direction:
- Do NOT patch SKU_SELECTION_MATRIX as executor.
- Do NOT patch PRICE_TABLE_VAT_INCL.
- Do NOT automate wrap pricing in this rollout.
- Implement missing supported-service execution paths inside PRICE_LADDER_ENGINE.md for:
  - PPF
  - Ceramic
  - Tint
  - Polishing

Reason:
- Architecture states PRICE_LADDER_ENGINE reads SKU_SELECTION_MATRIX and PRICE_TABLE_VAT_INCL.
- PRICE_LADDER_ENGINE is the only writer of price_ladder_state.
- Current engine only has explicit execution for wrap / roof PPF.
- Standard service pricing is currently relying on model inference, which is unsafe for rollout.

Boundary:
- SKU_SELECTION_MATRIX remains SKU-order authority.
- PRICE_TABLE_VAT_INCL remains numeric price authority.
- PRICE_LADDER_ENGINE must not redefine SKU defaults or invent prices.
- Wrap remains specialist handover only for current rollout.

## Pattern Note — Authority Drift Risk

This issue exposed a wider Phase 0–3 rollout risk:
- Architecture may correctly define ownership, but runtime implementation may be incomplete.
- Missing implementation can tempt patches in the wrong file.
- Files must remain clean:
  - SKU_SELECTION_MATRIX = SKU ordering only
  - PRICE_TABLE_VAT_INCL = numeric prices only
  - PRICE_LADDER_ENGINE = price execution + price_ladder_state
  - PHASE4_8_MESSAGE_ASSEMBLY_MAP = routing/render enforcement only

Before rollout:
- Audit Phase 0–3 for similar documented-but-not-executed bridge contracts.

## Pause Point / Open Work

Do not proceed to Phase 4 objection UAT until:
1. PRICE_LADDER_ENGINE service execution bridge is implemented.
2. Recent Phase 3B pricing patches are reconciled:
   - KEEP / MODIFY / REMOVE
3. Multi-service Phase 3B pricing UAT passes with output validation.
4. Exact expected price/range assertions are added.

This issue must remain OPEN until the above is complete.

## Failed Attempt Note — 2026-04-27

Attempted generic PRICE_LADDER_ENGINE bridge improved rendering/state behavior but did not produce exact price trust.

Observed after exact UAT assertions:
- Ceramic still selected wrong age/SKU path and produced forbidden values.
- PPF / tint / polishing also showed signs of VCB or SKU leakage in raw outputs.
- Therefore the current uncommitted PRICE_LADDER_ENGINE patch must NOT be committed as trusted runtime.

Next required approach:
- Stop wording-only / generic enforcement patches.
- Define exact deterministic SKU path per service before next UAT:
  - vehicle_model -> vehicle_segment
  - service qualifiers -> selected_skus
  - selected_skus + vehicle_segment -> exact prices
- Only then patch runtime.

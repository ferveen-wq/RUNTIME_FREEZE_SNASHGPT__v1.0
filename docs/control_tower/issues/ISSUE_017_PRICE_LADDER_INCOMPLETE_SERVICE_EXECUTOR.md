# ISSUE_017 — PRICE_LADDER_ENGINE incomplete service executor

## Pattern Name
Pricing Engine Service Execution Gap

## Status
FUNCTIONALLY RESOLVED FOR ACTIVE PHASE3B LANES / MONITORED — updated 2026-04-30

## Current resolution reading
The original risk was valid: Phase3B pricing could appear to pass from phrase selection or model inference while selected_skus / price_source_rows were incomplete.

As of 2026-04-30, active Phase3B price lanes have functional evidence:

- PPF front:
  - selected_skus = [PPF_FRONT_GLOBAL]
  - price_source_rows = PPF_FRONT_GLOBAL / VCB_2 / PRICE 295
  - no full-body leakage in strengthened anti-leak test
- Ceramic:
  - selected_skus = [CERAMIC_1Y, CERAMIC_3Y]
  - price_source_rows = 100 / 130 for VCB_2
- Tint:
  - selected_skus = [TINT_NANO_CERAMIC, TINT_XPEL_XR_PLUS]
  - price_source_rows = 130 / 220
- Polishing:
  - Route E polishing execution lock added
  - runner contradiction guards added
  - FINAL_PRICE_REACHED with selected_skus=[] now fails

## Current architecture reading
- SKU_SELECTION_MATRIX remains SKU-order authority.
- PRICE_TABLE_VAT_INCL remains numeric price authority.
- PRICE_LADDER_ENGINE remains price execution authority: it must emit/validate selected_skus from SKU_SELECTION_MATRIX, derive price_source_rows from selected_skus, and set price_ladder_state.
- PHASE4_8_MESSAGE_ASSEMBLY_MAP enforces Route E execution but does not calculate SKU.
- Runner parses and validates; it is not pricing authority.

## Remaining monitored risk
- 1x functional pass is not equal to 3x deterministic stability.
- Model/runtime compliance instability previously appeared in polishing.
- Continue to require exact selected_skus and non-empty price_source_rows for any pricing UAT.
- Do not accept phrase_id + visible price as a true pass.

## Control decision
- No further runtime patch is required from this issue unless fresh active raw evidence shows:
  - selected_skus empty/missing with FINAL_PRICE_REACHED
  - price_source_rows contains unselected SKUs
  - wrong service SKU leakage
  - forbidden price/range rendering
- Move forward to M5 with monitored pricing discipline.

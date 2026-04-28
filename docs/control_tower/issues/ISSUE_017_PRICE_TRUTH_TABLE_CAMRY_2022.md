# ISSUE 017 — Camry 2022 Phase 3B Price Truth Table

Vehicle:
- Toyota Camry 2022
- vehicle_segment = VCB_2

## Expected Price Paths

### PPF full body / highway
Source:
- SKU_SELECTION_MATRIX.md → VCB_2 DEFAULT HIGHWAY
- selected_skus = GLOBAL_SIGNATURE_10Y + GLOBAL_ELITE_8Y
- PRICE_TABLE_VAT_INCL.md VCB_2:
  - GLOBAL_ELITE_8Y = 790
  - GLOBAL_SIGNATURE_10Y = 880

Expected customer output:
- 790 to 880 BD VAT included

### Ceramic
Source:
- vehicle_year 2022 in 2026 = age 4
- age band = AGE_3_6_YEARS
- SKU_SELECTION_MATRIX.md → CERAMIC_1Y + CERAMIC_3Y
- PRICE_TABLE_VAT_INCL.md VCB_2:
  - CERAMIC_1Y = 100
  - CERAMIC_3Y = 130

Expected customer output:
- 100 to 130 BD VAT included

### Tint full
Source:
- PRICE_TABLE_VAT_INCL.md VCB_2:
  - TINT_NANO_CERAMIC = 110
  - TINT_XPEL_XR_PLUS = 220

Expected customer output:
- 110 to 220 BD VAT included

### Polishing exterior
Source:
- PRICE_TABLE_VAT_INCL.md VCB_2:
  - POLISH_SILVER = 50

Expected customer output:
- 50 BD VAT included

## Rule
No further Phase 3B price UAT should run unless runtime patch directly enforces these exact paths.

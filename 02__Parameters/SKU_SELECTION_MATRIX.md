# SKU_SELECTION_MATRIX.md

Purpose (HARD):
- This file is the ONLY authority for “which SKU should be shown” (ordering + ladders).
- Engines MUST NOT invent, reorder, or substitute SKUs outside what is listed here.
- Uses ONLY SKU IDs that exist in GLOBAL_PRODUCT_NAMING_REGISTRY_v1.0.md.

Scope (current):
- PPF only (CITY/HIGHWAY × VCB_1/2/3 × BRAND_INTENT DEFAULT/XPEL)

Row contract (HARD):
- Each row MUST define:
  - DEFAULT (A)
  - SECOND (B)
  - UPLADDER
  - DOWNLADDER
- Do NOT add extra variants.
- If a row is missing, engine must ask 1 clarifier OR fall back to a safe default rule (but must NOT guess new SKUs).

Enums:
- VEHICLE_CLASS_BAND: VCB_1 | VCB_2 | VCB_3
- DRIVING_PROFILE: CITY | HIGHWAY
- BRAND_INTENT: DEFAULT | XPEL

Format (LOCKED):
- Keep as a table (easy to diff + review).

---

## PPF — SKU Selection Matrix

| VEHICLE_CLASS_BAND | DRIVING_PROFILE | BRAND_INTENT | DEFAULT (A) | SECOND (B) | UPLADDER | DOWNLADDER |
|---|---|---|---|---|---|---|
| VCB_1 | CITY | DEFAULT | TBD | TBD | TBD | TBD |
| VCB_1 | HIGHWAY | DEFAULT | TBD | TBD | TBD | TBD |
| VCB_1 | CITY | XPEL | TBD | TBD | TBD | TBD |
| VCB_1 | HIGHWAY | XPEL | TBD | TBD | TBD | TBD |
| VCB_2 | CITY | DEFAULT | TBD | TBD | TBD | TBD |
| VCB_2 | HIGHWAY | DEFAULT | TBD | TBD | TBD | TBD |
| VCB_2 | CITY | XPEL | TBD | TBD | TBD | TBD |
| VCB_2 | HIGHWAY | XPEL | TBD | TBD | TBD | TBD |
| VCB_3 | CITY | DEFAULT | TBD | TBD | TBD | TBD |
| VCB_3 | HIGHWAY | DEFAULT | TBD | TBD | TBD | TBD |
| VCB_3 | CITY | XPEL | TBD | TBD | TBD | TBD |
| VCB_3 | HIGHWAY | XPEL | TBD | TBD | TBD | TBD |

Notes:
- “DEFAULT (Global)” = BRAND_INTENT DEFAULT.
- If customer explicitly requests matte: selection is handled separately as:
  - DEFAULT → GLOBAL_MATTE_10Y
  - XPEL → XPEL_STEALTH_10Y
  (Do NOT mix matte into the rows above unless you want a dedicated matte matrix later.)

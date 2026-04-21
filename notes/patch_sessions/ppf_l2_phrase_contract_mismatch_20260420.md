# PPF L2 Phrase Contract Mismatch — 2026-04-20

## Finding

`PHASE5_PPF_NARROW_L2` in `00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_6_HUMAN_PHRASE_LIBRARY.md`
contains forbidden price wording that the strict UAT pack rejects.

## Evidence

Phrase block contains:

- EN: "If the price feels a bit high..."
- AR: "إذا السعر حاسس إنه مرتفع شوي..."

Strict pack forbids:

- english: `price`
- arabic: `سعر`

## Conclusion

This is not a Phase 5 router-selection defect.

This is a contract mismatch between:
- locked phrase-library content
- strict UAT expectation

## Classification

- test / phrase contract mismatch
- not runtime routing
- not repeat-count issue
- not central-router ownership issue

## Safe next step

Do not patch router for this failure.

Choose one of these intentionally:
1. keep phrase as business truth and relax strict pack
2. keep strict pack and rewrite locked phrase through phrase-governance path

Until that choice is made:
- treat this case as non-routing residual mismatch

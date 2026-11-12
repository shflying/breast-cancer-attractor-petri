# Results Summary

## Combined Transition Matrix (240 pairs)

| From \ To | Low | Mid | High |
|-----------|-----|-----|------|
| Low | 0.561 | 0.317 | 0.122 |
| Mid | 0.429 | 0.286 | 0.286 |
| High | 0.296 | 0.284 | 0.420 |

## Standard Chemotherapy Subset (GSE32603)

| From \ To | Low | Mid | High |
|-----------|-----|-----|------|
| Low | 0.393 | 0.607 | 0.000 |
| Mid | 0.500 | 0.214 | 0.286 |
| High | 0.296 | 0.444 | 0.259 |

## Simulation Comparison (500 runs)

| Next State | Full Cohort | Standard Chemo |
|------------|-------------|----------------|
| Low | 231 | 206 |
| Mid | 145 | 210 |
| High | 124 | 84 |

## Key Finding

Standard chemotherapy shows stronger Low → Mid movement and weaker High retention compared with the mixed full cohort.

## Attractor Domains (I-SPY2 pCR)

- Strong: High immune (mean pCR ~0.31)
- Moderate: Mid immune (mean pCR ~0.12)
- Weak: Low immune (mean pCR ~0.06)

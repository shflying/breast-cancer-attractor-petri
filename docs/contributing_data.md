# Contributing Data

This project currently relies on publicly available GEO datasets and the I-SPY2 trial for pCR probabilities. The model improves with more paired, treatment-annotated samples.

## What Data Is Useful

| Priority | Data Type | Why It Helps | Minimum Requirements |
|----------|-----------|--------------|----------------------|
| High | Paired pre/post gene expression | Improves transition matrix | Same patient, before and after treatment |
| High | Known treatment regimen | Allows regimen-specific transitions | Chemotherapy, targeted, immunotherapy, or endocrine |
| High | pCR or RCB label | Links state to outcome | Binary pCR or RCB class |
| Medium | Multiple time points | Enables multi-step Petri net | T1, T2, T3, or residual |
| Medium | Subtype annotation | Stratified analysis | HR, HER2, or molecular subtype |

## Currently Used Datasets

| Dataset | Pairs | Treatment Info | Response | Notes |
|---------|-------|----------------|----------|-------|
| GSE32603 (I-SPY1) | 69 | F1/F2/FS codes | RCB, pCR | Main standard chemo source |
| GSE122630 | 25 | Neoadjuvant chemo (unspecified) | — | NEO trial |
| GSE114403 | 43 | Bevacizumab vs control | — | — |
| GSE309004 | 16 | — | NR vs response | — |
| GSE147271 | 28 | Tamoxifen | — | Endocrine |
| GSE32072 | 21 | Pre/post NAC | — | — |
| I-SPY2 | — | Multiple arms | pCR | Used for pCR probabilities |

## How to Contribute

1. **Public GEO datasets**: Open an issue with the GSE accession and a short description.
2. **Processed data**: Submit a pull request with a CSV in `data/processed/` following the format below.
3. **New analysis**: Open an issue or PR with code in `src/`.

### Preferred CSV Format for Paired Scores

```csv
patient,timepoint,immune,estrogen,proliferation,treatment,response
P001,pre,8.2,9.1,7.5,AC+T,pCR
P001,post,9.1,8.4,6.2,AC+T,pCR
```

## Data We Cannot Accept

- Identifiable patient information
- Data under restrictive licenses that prohibit redistribution
- Unpaired samples without clear patient linkage

## Questions

Open an issue or contact the maintainers.

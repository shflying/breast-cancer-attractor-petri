# Datasets Used in This Study

This document lists the public datasets used to build the transition matrix and attractor analysis, with download links and processing notes.

## Summary

| Dataset | Pairs | Platform | Treatment | Download |
|---------|-------|----------|-----------|----------|
| GSE32603 (I-SPY1) | 69 | GPL14668 | F1/F2/FS (chemo codes) | [GEO](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE32603) |
| GSE122630 | 25 | Ion AmpliSeq | Neoadjuvant chemo | [GEO](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE122630) |
| GSE114403 | 43 | NanoString | Bevacizumab vs control | [GEO](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE114403) |
| GSE309004 | 16 | — | — | [GEO](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE309004) |
| GSE147271 | 28 | Agilent | Tamoxifen | [GEO](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE147271) |
| GSE32072 | 21 | GPL96 | Pre/post NAC | [GEO](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE32072) |
| I-SPY2 (pCR) | — | — | Multiple arms | Used for pCR probabilities only |
| GSE280902 | 0 | — | — | Examined, excluded (baseline only) |
| GSE240671 | — | — | — | Partially processed, not yet integrated |

**Total paired samples: 240** (after filtering)

## Download Instructions

### GEO Series Matrix (recommended)

For each GSE accession, download:

1. **Series Matrix**: `https://ftp.ncbi.nlm.nih.gov/geo/series/GSEnnn/GSExxxxx/matrix/`
2. **Family SOFT**: for sample characteristics
3. **Platform annotation**: if probe-to-gene mapping is needed

Example for GSE32603:

```
https://ftp.ncbi.nlm.nih.gov/geo/series/GSE32nnn/GSE32603/matrix/GSE32603_series_matrix.txt.gz
https://ftp.ncbi.nlm.nih.gov/geo/series/GSE32nnn/GSE32603/soft/GSE32603_family.soft.gz
```

### Platform Annotations

Probe-to-gene mapping requires platform annotation files:

| Platform | Dataset | Annotation File | Download |
|----------|---------|-----------------|----------|
| GPL14668 | GSE32603 | GPL14668_family.soft.gz | [GEO](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GPL14668) |
| GPL96 | GSE32072 | GPL96.annot.gz | [GEO](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GPL96) |
| GPL28292 | GSE147271 | GPL28292_family.soft.gz | [GEO](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GPL28292) |

**Note**: 
- GSE122630 uses Ensembl IDs (mapped via biomaRt or gene symbol conversion)
- GSE114403 (NanoString) and GSE309004 already use gene symbols
- GPL files are large; only download the annotation when probe mapping is needed

## Processing Pipeline

Processing scripts are in [docs/processing/](processing/).

### 1. Parse Series Matrix

```bash
cd docs/processing
python parse_series_matrix.py --input GSE32603_series_matrix.txt.gz --output samples.csv
```

### 2. Map Probes to Genes

```bash
python map_probes.py --expr expression.csv --annot GPL14668_family.soft.gz --output mapped.csv
```

### 3. Compute Immune Scores

```bash
python compute_scores.py --input mapped.csv --output scores.csv
```

### 4. Build Transition Matrix

```bash
python build_transitions.py --scores scores.csv --output transitions.csv
```

See [processing/README.md](processing/README.md) for details.

## Notes

- **I-SPY2**: Used only for pCR probabilities by state and arm. Raw expression data not redistributed.
- **Treatment heterogeneity**: Most datasets lack detailed regimen information. GSE32603 F1/FS codes are used as a proxy for standard chemotherapy.
- **Platform differences**: Scores are discretized independently per dataset before merging counts.

## Contributing New Datasets

See [contributing_data.md](contributing_data.md) for requirements and preferred format.

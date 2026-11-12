# Dataset Processing Scripts

This directory contains scripts for processing the GEO datasets used in this study.
## Structure

```
processing/
├── README.md
├── parse_series_matrix.py    # Parse GEO Series Matrix files
├── map_probes.py              # Map probe IDs to gene symbols
├── compute_scores.py          # Compute immune signature scores
└── build_transitions.py       # Build transition matrices from paired samples
```

## Usage

These scripts are templates based on the analysis pipeline. Adapt paths and parameters for your local environment.

### 1. Parse Series Matrix

```bash
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

## Notes

- Original analysis scripts (c-*.py, f-*.py) are available from the project maintainer
- These templates capture the core logic for reproducibility
- Platform-specific annotation files must be downloaded separately (see datasets.md)

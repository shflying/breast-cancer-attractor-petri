# Breast Cancer Attractor + Petri Net Decision Model

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Status: Research Prototype](https://img.shields.io/badge/status-research%20prototype-orange.svg)]()

An Attractor and Petri Net-Based Decision Framework for Breast Cancer Therapy.A research prototype that models breast cancer treatment response using **immune state attractors** and a **two-step stochastic Petri net**. The framework is designed for any treatment setting (neoadjuvant, adjuvant, or other) where paired pre/post gene expression data are available.

## Key Idea

**Attractor + Petri Net** is the core contribution:

- **Attractors** identify clinically meaningful immune states (Strong / Moderate / Weak) by combining transition dynamics with pCR rates
- **Petri net** models how patients move between states under different treatments
- Together they support treatment recommendation and trajectory prediction

## Current Results

See [docs/showcase](docs/showcase/) for visual summaries of the transition matrix, attractor domains, and simulation outcomes.

## Roadmap

See [docs/roadmap.md](docs/roadmap.md) for current status, near-term priorities, and how to contribute.

## Current Status

| Component | Status | Notes |
|-----------|--------|-------|
| Immune signature | Working | 8 genes: CD8A, CD3D, GZMA, GZMB, PRF1, IFNG, CXCL9, CXCL10 |
| Transition matrix | Working | 240 paired samples from multiple GEO datasets |
| Attractor analysis | Working | Clinical score = 0.7×pCR + 0.3×transition strength |
| Two-step Petri net | Working | Step 1: pCR probability; Step 2: immune state transition |
| Recommendation function | Working | Returns recommended arm + expected pCR + attractor domain |
| Standard chemo subset | Exploratory | GSE32603 F1/FS codes as proxy |

## Quick Start

```python
import pandas as pd
from src.attractor import get_attractor_summary
from src.recommend import recommend

# Load transition matrix
trans = pd.read_csv("data/processed/combined_transition_matrix_v7.csv", index_col=0)

# Compute attractor summary
summary = get_attractor_summary(trans, {"High": 0.308, "Mid": 0.115, "Low": 0.059})
print(summary)

# Get recommendation
result = recommend("High", "Low", trans_prob=trans)
print(result)
```

## Installation

```bash
git clone https://github.com/shflying/breast-cancer-attractor-petri.git
cd breast-cancer-attractor-petri
pip install pandas numpy matplotlib seaborn
```

## Project Structure

```
breast-cancer-attractor-petri/
├── README.md
├── LICENSE
├── docs/
│   ├── method.md                 # Methods description
│   ├── datasets.md               # Dataset download links
│   ├── contributing_data.md      # How to contribute data
│   ├── results_summary.md        # Key results
│   ├── showcase/                 # Visual results
│   │   ├── README.md
│   │   ├── transition_heatmap.png
│   │   ├── attractor_domains.png
│   │   └── simulation_distribution.png
│   └── processing/               # Dataset processing scripts
│       ├── parse_series_matrix.py
│       ├── map_probes.py
│       ├── compute_scores.py
│       └── build_transitions.py
├── data/processed/               # Processed transition matrices
├── scripts/
│   └── generate_showcase_figures.py  # Generate figures in docs/showcase/
├── src/
│   ├── signature.py              # Immune signature computation
│   ├── transition.py             # Transition matrix building
│   ├── attractor.py              # Attractor analysis
│   ├── petri_net.py              # Two-step Petri net simulation
│   └── recommend.py              # Recommendation function
└── reports/                      # Analysis reports
```

## Data

Processed transition matrices and simulation outputs are in `data/processed/`.

**We need more data.** Especially:
- Paired pre/post-treatment gene expression
- Known treatment regimen (chemotherapy, targeted, immunotherapy)
- Response labels (pCR, residual, RCB)

See [docs/contributing_data.md](docs/contributing_data.md) for how to contribute.

## Datasets Used

| Dataset | Pairs | Platform | Notes |
|---------|-------|----------|-------|
| GSE32603 (I-SPY1) | 69 | GPL14668 | F1/F2/FS treatment codes |
| GSE122630 | 25 | Ion AmpliSeq | NEO trial |
| GSE114403 | 43 | NanoString | Bevacizumab vs control |
| GSE309004 | 16 | — | Baseline / Follow-up |
| GSE147271 | 28 | Agilent | Tamoxifen |
| GSE32072 | 21 | GPL96 (Affymetrix) | Pre/post NAC |
| I-SPY2 | — | — | pCR probabilities only (not used for transitions) |

**Total paired samples in transition matrix: ~240**

**Platform annotations used for probe-to-gene mapping**:
- GPL14668 (GSE32603)
- GPL96 (GSE32072)
- GPL28292 (GSE147271)

See [docs/datasets.md](docs/datasets.md) for download links and processing notes.

**Note**: GSE280902 was examined but excluded (only baseline samples, no pairs). GSE240671 was partially processed but not yet fully integrated.

## Authors and Collaborators

| Role | Name | Affiliation | Contact |
|------|------|-------------|---------|
| Principal Investigator / Lead Author |SHUAI,WENXIN | [Institution] | open_shfr@sina.com |
| Collaborator/CO-Lead Author | Flying Rock | Independent Researcher | open_sh_fr@outlook.com|

### Rights and Attribution

- **Code**: Licensed under the MIT License. Copyright (c) 2026 [(SHUAI,WENXIN )and(Flying Rock)]. See [LICENSE](LICENSE).
- **Documentation and analysis results**: Copyright (c) 2026 (SHUAI,WENXIN) and (Flying Rock). May be reused with attribution.
- **Public datasets** (GSE32603, GSE122630, GSE114403, GSE309004, GSE147271, GSE32072, I-SPY2, etc.): Remain under the original licenses and terms of their providers (GEO / NCBI). Users must comply with the original data use policies.
- **Citation**: Please cite this repository and the original datasets when using the code, methods, or results.

## Citation

If you use this work, please cite:

```bibtex
@software{breast_cancer_attractor_petri,
  title = {Breast Cancer Attractor + Petri Net Model},
  author = {(SHUAI,WENXIN) and (Flying Rock)},
  year = {2026},
  url = {https://github.com/shflying/breast-cancer-attractor-petri},
  note = {Research prototype}
}
```

Also cite the original datasets (I-SPY2, GSE32603, GSE122630, etc.).

## Contributing

Contributions are welcome, especially:
- New paired pre/post-treatment datasets
- Treatment regimen annotations
- Response labels (pCR, RCB)

See [docs/contributing_data.md](docs/contributing_data.md).

## License

- **Code**: MIT License. Copyright (c) 2026 [(SHUAI,WENXIN) and (Flying Rock)] . See [LICENSE](LICENSE).
- **Documentation and derived results**: Copyright (c) 2026 [(SHUAI,WENXIN) and (Flying Rock) . Reuse with attribution.
- **Source datasets**: Remain under their original licenses (GEO / NCBI). See individual dataset pages for terms.

## Disclaimer

This is a **research prototype**, not a clinical tool. Results should not be used for treatment decisions without validation and clinical review.

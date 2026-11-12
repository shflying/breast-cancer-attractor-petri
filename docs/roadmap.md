# Community Roadmap

This roadmap outlines the current status, near-term priorities, and longer-term directions for the Breast Cancer Attractor + Petri Net project. It is intended to help potential contributors understand where the project is and where contributions are most useful.

**Last updated**: November 2026  
**Status**: Research prototype

## Current Status (v0.1 – Research Prototype)

Completed:

- 8-gene immune signature (CD8A, CD3D, GZMA, GZMB, PRF1, IFNG, CXCL9, CXCL10)
- Transition matrix from ~240 paired pre/post samples across multiple GEO datasets
- Clinical attractor domains (Strong / Moderate / Weak) combining transition strength and pCR rates
- Two-step stochastic Petri net (Step 1: pCR probability; Step 2: immune state transition)
- Recommendation function returning recommended treatment arm, expected pCR, and attractor domain
- Showcase figures and documentation
- Standard chemotherapy subset exploration (GSE32603)

## Near-Term Priorities (next 3–6 months)

### 1. Expand paired data (highest priority)
- Integrate additional paired pre/post-treatment datasets
- Finish processing of partially examined datasets (e.g., GSE240671)
- Prefer datasets with known treatment regimen and response labels (pCR, RCB)

### 2. Improve treatment specificity
- Move from mixed-cohort transition matrix toward regimen-specific matrices where sample size allows
- Better annotation of treatment arms (chemotherapy, targeted, immunotherapy, endocrine)

### 3. Multi-step and longitudinal modeling
- Incorporate datasets with more than two time points
- Extend Petri net from two-step to multi-step trajectories

### 4. Validation and robustness
- Cross-dataset validation of transition probabilities
- Sensitivity analysis of attractor thresholds and signature gene sets

## Medium-Term Directions (6–12 months)

- **Colored Petri net**: multi-dimensional tokens (immune × estrogen × proliferation)
- **Hybrid Petri net**: continuous signature scores + discrete treatment events
- **Timed Petri net**: incorporate timing of treatment and biopsy intervals
- Attractor analysis using alternative methods (e.g., Lyapunov-style stability on continuous scores)
- Interactive visualization or simple web demo of the recommendation function
- Comparison with standard clinical baselines

## Longer-Term Vision

- A reusable framework for modeling treatment-induced state transitions in cancer (and potentially other diseases)
- Community-contributed datasets with standardized pre/post format
- Validated recommendation support tool (research use only)
- Publications describing the attractor + Petri net approach

## How to Contribute

We especially welcome:

| Contribution type | Why it helps | Where to start |
|-------------------|--------------|----------------|
| New paired pre/post datasets | Improves transition matrix reliability | [contributing_data.md](contributing_data.md) |
| Treatment regimen annotations | Enables regimen-specific modeling | Issue or pull request with sample metadata |
| Response labels (pCR, RCB) | Links states to clinical outcome | Same as above |
| Code improvements | Cleaner simulation, better tests, new Petri net variants | `src/` and issues |
| Documentation | Clearer methods, tutorials, translations | `docs/` |
| Validation ideas | Robustness checks, alternative signatures | Discussions or issues |

See [contributing_data.md](contributing_data.md) for data format requirements.

## Version Milestones (tentative)

| Version | Goal | Target |
|---------|------|--------|
| v0.1 | Current research prototype | Done |
| v0.2 | Additional datasets + regimen-specific matrix | 3–6 months |
| v0.3 | Multi-step Petri net + improved validation | 6–12 months |
| v1.0 | Stable API + documented validation | TBD |

## Communication

- Open issues on GitHub for bugs, feature requests, or dataset suggestions
- Discussions for broader ideas (new Petri net variants, alternative attractor definitions)
- Pull requests for code, documentation, or new processed datasets

---

This roadmap is a living document. Feedback and contributions are welcome.

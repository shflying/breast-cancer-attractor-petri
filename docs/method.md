# Method

## Immune Signature

Eight genes associated with cytotoxic immune activity:

**CD8A, CD3D, GZMA, GZMB, PRF1, IFNG, CXCL9, CXCL10**

Score = log2(mean expression of available genes + 1)

## State Discretization

Immune scores are divided into three levels using tertiles (1/3 and 2/3 quantiles):

- **Low**: score ≤ Q1
- **Mid**: Q1 < score ≤ Q2
- **High**: score > Q2

## Transition Matrix

From paired pre/post samples:

1. Compute immune score at both time points
2. Discretize to Low / Mid / High
3. Build crosstab of (pre_level → post_level)
4. Normalize rows to obtain transition probabilities

## Attractor Analysis

A key component of this work. Attractors are defined by combining:

1. **Transition strength**: P(→High) − P(→Low) from the transition matrix
2. **Clinical pCR rate**: Mean pCR by immune level from I-SPY2

**Clinical score** = 0.7 × pCR + 0.3 × transition_strength

| Domain | Clinical Score | Interpretation |
|--------|----------------|----------------|
| Strong | ≥ 0.15 | Higher pCR, immunotherapy preferred |
| Moderate | 0 to 0.15 | Intermediate benefit |
| Weak | < 0 | Limited treatment benefit |

See `src/attractor.py` for implementation.

## Two-Step Petri Net

- **Places**: Immune states (Low/Mid/High) × Estrogen states, plus pCR and Residual
- **Transitions**: Treatment arms (from I-SPY2)
- **Step 1**: Look up empirical pCR probability for (state, arm)
- **Step 2**: Sample next immune state from the transition matrix

## Recommendation Function

Input: immune level (+ optional estrogen level, optional transition matrix)
Output: recommended arm, expected pCR, attractor domain, clinical score

The attractor domain informs the recommendation and is returned as part of the output.

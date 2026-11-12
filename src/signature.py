"""Immune signature  calculation."""


import numpy as np
import pandas as pd

IMMUNE_GENES = ["CD8A", "CD3D", "GZMA", "GZMB", "PRF1", "IFNG", "CXCL9", "CXCL10"]

def compute_immune_score(expr: pd.DataFrame, genes=None) -> pd.Series:
    """Compute immune signature from expression matrix (genes × samples)."""
    genes = genes or IMMUNE_GENES
    available = [g for g in genes if g in expr.index]
    if not available:
        return pd.Series(np.nan, index=expr.columns)
    return np.log2(expr.loc[available].mean(axis=0) + 1)

def discretize(scores: pd.Series, q1=None, q2=None) -> pd.Series:
    """Discretize scores into Low / Mid / High."""
    if q1 is None or q2 is None:
        q1, q2 = scores.quantile([1/3, 2/3])
    def level(x):
        if pd.isna(x):
            return np.nan
        if x <= q1:
            return "Low"
        elif x <= q2:
            return "Mid"
        else:
            return "High"
    return scores.apply(level)

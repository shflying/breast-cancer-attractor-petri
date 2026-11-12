"""Transition  matrix construction."""


import pandas as pd
import numpy as np

def build_transition_matrix(pre: pd.Series, post: pd.Series) -> pd.DataFrame:
    """Build normalized transition probability matrix from pre/post levels."""
    df = pd.DataFrame({"pre": pre, "post": post}).dropna()
    ct = pd.crosstab(df["pre"], df["post"])
    ct = ct.reindex(index=["Low", "Mid", "High"], columns=["Low", "Mid", "High"], fill_value=0)
    prob = ct.div(ct.sum(axis=1), axis=0).fillna(0)
    return prob

def merge_transition_counts(count_list: list) -> pd.DataFrame:
    """Sum multiple count matrices and normalize."""
    total = sum(count_list)
    total = total.reindex(index=["Low", "Mid", "High"], columns=["Low", "Mid", "High"], fill_value=0)
    return total.div(total.sum(axis=1), axis=0).fillna(0)

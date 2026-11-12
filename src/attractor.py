"""Attractor analysis for  breast cancer immune states.

Combines transition dynamics  with clinical pCR rates to define
attractor  domains (Strong / Moderate / Weak).
"""


import pandas as pd
import numpy as np

def transition_attractor_strength(trans_prob: pd.DataFrame) -> pd.Series:
    """
    Compute attractor strength from transition matrix.
    Strength = P(→High) - P(→Low)
    Positive values indicate tendency toward High immune state.
    """
    strength = {}
    for state in trans_prob.index:
        p_high = trans_prob.loc[state, "High"] if "High" in trans_prob.columns else 0
        p_low = trans_prob.loc[state, "Low"] if "Low" in trans_prob.columns else 0
        strength[state] = p_high - p_low
    return pd.Series(strength, name="transition_strength")

def clinical_attractor_score(pcr_by_immune: dict, trans_strength: pd.Series,
                             pcr_weight: float = 0.7) -> pd.DataFrame:
    """
    Combine pCR rate with transition strength.
    clinical_score = pcr_weight * pCR + (1 - pcr_weight) * transition_strength
    """
    rows = []
    for immune in ["High", "Mid", "Low"]:
        pcr = pcr_by_immune.get(immune, 0)
        t_strength = trans_strength.get(immune, 0)
        score = pcr_weight * pcr + (1 - pcr_weight) * t_strength
        rows.append({
            "immune_level": immune,
            "mean_pcr": pcr,
            "transition_strength": t_strength,
            "clinical_score": score
        })
    return pd.DataFrame(rows).set_index("immune_level")

def classify_attractor_domain(clinical_score: float) -> str:
    """Classify attractor domain based on clinical score."""
    if clinical_score >= 0.15:
        return "Strong"
    elif clinical_score >= 0.0:
        return "Moderate"
    else:
        return "Weak"

def get_attractor_summary(trans_prob: pd.DataFrame, pcr_by_immune: dict) -> pd.DataFrame:
    """
    Full attractor analysis.
    
    Parameters
    ----------
    trans_prob : DataFrame
        Transition probability matrix (rows: from, columns: to)
    pcr_by_immune : dict
        Mean pCR rate by immune level, e.g. {"High": 0.308, "Mid": 0.115, "Low": 0.059}
    
    Returns
    -------
    DataFrame with columns: mean_pcr, transition_strength, clinical_score, domain
    """
    t_strength = transition_attractor_strength(trans_prob)
    summary = clinical_attractor_score(pcr_by_immune, t_strength)
    summary["domain"] = summary["clinical_score"].apply(classify_attractor_domain)
    return summary

# Default pCR rates from I-SPY2 (can be overridden)
DEFAULT_PCR_BY_IMMUNE = {
    "High": 0.308,
    "Mid": 0.115,
    "Low": 0.059
}

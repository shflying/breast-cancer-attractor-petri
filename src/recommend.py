"""Recommendation  function  integrating attractor analysis."""



import pandas as pd
import numpy as np
from attractor import get_attractor_summary, DEFAULT_PCR_BY_IMMUNE

def recommend(immune_level: str, estrogen_level: str = "Mid",
              pcr_table: pd.DataFrame = None,
              trans_prob: pd.DataFrame = None) -> dict:
    """
    Recommend treatment arm based on immune and estrogen levels.
    Integrates attractor domain from transition dynamics and pCR rates.
    
    Returns dict with recommended_arm, expected_pcr, attractor_domain, clinical_score, note
    """
    state = f"{immune_level}_{estrogen_level}"
    
    # Compute attractor domain if transition matrix provided
    if trans_prob is not None:
        summary = get_attractor_summary(trans_prob, DEFAULT_PCR_BY_IMMUNE)
        domain = summary.loc[immune_level, "domain"] if immune_level in summary.index else "Unknown"
        clinical_score = summary.loc[immune_level, "clinical_score"] if immune_level in summary.index else 0
    else:
        # Fallback based on immune level alone
        if immune_level == "High":
            domain = "Strong"
            clinical_score = 0.205
        elif immune_level == "Mid":
            domain = "Moderate"
            clinical_score = 0.025
        else:
            domain = "Weak"
            clinical_score = -0.091

    # Note based on domain
    if domain == "Strong":
        note = "Strong attractor: higher pCR rate, immunotherapy preferred"
    elif domain == "Moderate":
        note = "Moderate attractor: intermediate benefit expected"
    else:
        note = "Weak attractor: limited treatment benefit expected"

    # Recommendation logic
    if immune_level == "High" and estrogen_level in ["Low", "Mid"]:
        arm = "Paclitaxel + Pembrolizumab"
        expected = 0.667
    elif immune_level == "Low":
        arm = "Paclitaxel + Ganetespib"
        expected = 0.143
    else:
        arm = "Paclitaxel"
        expected = 0.17

    return {
        "state": state,
        "recommended_arm": arm,
        "expected_pcr": round(expected, 3),
        "attractor_domain": domain,
        "clinical_score": round(clinical_score, 3),
        "note": note
    }

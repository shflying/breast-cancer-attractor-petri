"""Compute immune  signature scores from expression data."""


import pandas as pd
import numpy as np
import argparse
import sys
sys.path.insert(0, "../../src")
from signature import compute_immune_score, discretize

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Gene expression matrix CSV")
    parser.add_argument("--output", default="scores.csv", help="Output scores CSV")
    args = parser.parse_args()
    
    expr = pd.read_csv(args.input, index_col=0)
    scores = compute_immune_score(expr)
    levels = discretize(scores)
    
    result = pd.DataFrame({
        "sample": scores.index,
        "immune": scores.values,
        "immune_level": levels.values
    })
    result.to_csv(args.output, index=False)
    print(f"Computed scores for {len(result)} samples")
    print(result["immune_level"].value_counts())

if __name__ == "__main__":
    main()

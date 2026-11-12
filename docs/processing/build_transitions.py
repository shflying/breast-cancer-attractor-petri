"""Build transition matrices from paired pre/post samples."""


import pandas as pd
import argparse
import sys
sys.path.insert(0, "../../src")
from transition import build_transition_matrix

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--scores", required=True, help="Scores CSV with sample, immune_level, patient, timepoint")
    parser.add_argument("--output", default="transitions.csv", help="Output transition matrix")
    args = parser.parse_args()
    
    scores = pd.read_csv(args.scores)
    
    # Identify pre and post samples
    # Assumes columns: patient, timepoint, immune_level
    pre = scores[scores["timepoint"].isin(["pre", "T1", "Baseline"])]
    post = scores[scores["timepoint"].isin(["post", "T4", "FollowUp", "TS"])]
    
    # Match by patient
    merged = pre.merge(post, on="patient", suffixes=("_pre", "_post"))
    
    if len(merged) == 0:
        print("No paired samples found")
        return
    
    trans = build_transition_matrix(
        merged["immune_level_pre"],
        merged["immune_level_post"]
    )
    trans.to_csv(args.output)
    print(f"Built transition matrix from {len(merged)} pairs")
    print(trans)

if __name__ == "__main__":
    main()

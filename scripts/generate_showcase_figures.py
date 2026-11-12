"""
Generate core  showcase figures for the project.
Run from project  root: python scripts/generate_showcase_figures.py
"""


import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

output_dir = Path("docs/showcase")
output_dir.mkdir(parents=True, exist_ok=True)

sns.set_style("whitegrid")
plt.rcParams["font.size"] = 11
plt.rcParams["axes.titlesize"] = 13

# ============================================================
# 1. Transition Matrix Heatmap (normalized to probability)
# ============================================================
trans_raw = pd.read_csv("data/processed/combined_transition_matrix_v7.csv", index_col=0)

# Normalize rows to probabilities
trans = trans_raw.div(trans_raw.sum(axis=1), axis=0)

fig, ax = plt.subplots(figsize=(6, 5))
sns.heatmap(
    trans,
    annot=True,
    fmt=".3f",
    cmap="YlOrRd",
    vmin=0,
    vmax=0.7,
    square=True,
    cbar_kws={"label": "Transition Probability"},
    ax=ax,
)
ax.set_title("Immune State Transition Matrix\n(Combined, n≈240 paired samples)")
ax.set_xlabel("Next Immune Level")
ax.set_ylabel("Current Immune Level")
fig.tight_layout()
plt.savefig(output_dir / "transition_heatmap.png", dpi=150, bbox_inches="tight")
plt.close()
print("Saved: transition_heatmap.png")

# ============================================================
# 2. Attractor Domain Scores
# ============================================================
pcr_by_level = {"High": 0.308, "Mid": 0.115, "Low": 0.059}
strength = (trans["High"] - trans["Low"]).to_dict()

attract_scores = {}
for level in ["Low", "Mid", "High"]:
    attract_scores[level] = 0.7 * pcr_by_level[level] + 0.3 * strength[level]

def domain_label(score):
    if score > 0.15:
        return "Strong"
    elif score > 0:
        return "Moderate"
    else:
        return "Weak"

levels = ["Low", "Mid", "High"]
scores = [attract_scores[l] for l in levels]
domains = [domain_label(s) for s in scores]
colors = {"Strong": "#2ecc71", "Moderate": "#f39c12", "Weak": "#e74c3c"}
bar_colors = [colors[d] for d in domains]

fig, ax = plt.subplots(figsize=(7, 5))
bars = ax.bar(levels, scores, color=bar_colors, edgecolor="black", linewidth=0.8, width=0.6)
ax.axhline(0, color="gray", linestyle="--", linewidth=0.8)
ax.set_ylabel("Clinical Attract Score")
ax.set_title("Attractor Domains by Immune Level\n(0.7×pCR + 0.3×transition strength)")
ax.set_ylim(-0.5, 0.5)

for bar, domain, score in zip(bars, domains, scores):
    height = bar.get_height()
    y_pos = height / 2
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        y_pos,
        f"{domain}\n({score:.3f})",
        ha="center",
        va="center",
        fontsize=10,
        color="white" if abs(score) > 0.15 else "black",
        fontweight="bold",
    )

fig.tight_layout()
plt.savefig(output_dir / "attractor_domains.png", dpi=150, bbox_inches="tight")
plt.close()
print("Saved: attractor_domains.png")

# ============================================================
# 3. Simulation Distribution
# ============================================================
sim_files = [
    "data/processed/two_step_simulation_std_chemo.csv",
    "data/processed/two_step_simulation_v6.csv",
]
sim = None
for f in sim_files:
    if Path(f).exists():
        sim = pd.read_csv(f)
        break

if sim is not None and "next_immune" in sim.columns:
    dist = sim["next_immune"].value_counts().reindex(["Low", "Mid", "High"]).fillna(0)
    dist_pct = dist / dist.sum() * 100

    fig, ax = plt.subplots(figsize=(6, 4.5))
    bars = ax.bar(
        dist_pct.index,
        dist_pct.values,
        color=["#3498db", "#9b59b6", "#e67e22"],
        edgecolor="black",
        linewidth=0.8,
        width=0.6,
    )
    ax.set_ylabel("Percentage (%)")
    ax.set_xlabel("Next Immune Level")
    ax.set_title(f"Simulated Post-Treatment Immune Distribution\n(n={len(sim)} simulations)")
    ax.set_ylim(0, max(dist_pct.values) * 1.2)

    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height + 1.5,
            f"{height:.1f}%",
            ha="center",
            va="bottom",
            fontsize=11,
        )

    fig.tight_layout()
    plt.savefig(output_dir / "simulation_distribution.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("Saved: simulation_distribution.png")
else:
    print("Simulation file not found. Skipping figure 3.")

print("\nDone. Figures saved to docs/showcase/")

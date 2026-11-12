"""Two-step  stochastic Petri net simulation."""


import pandas as pd
import numpy as np

class TwoStepPetriNet:
    def __init__(self, pcr_prob: pd.DataFrame, immune_trans: pd.DataFrame):
        """
        pcr_prob: DataFrame with columns [state, arm, p_pcr]
        immune_trans: DataFrame indexed by immune level, columns Low/Mid/High
        """
        self.pcr_prob = pcr_prob
        self.immune_trans = immune_trans

    def step(self, state: str, arm: str) -> dict:
        match = self.pcr_prob[(self.pcr_prob["state"] == state) & (self.pcr_prob["arm"] == arm)]
        p_pcr = match["p_pcr"].values[0] if len(match) > 0 else np.nan

        immune = state.split("_")[0]
        if immune in self.immune_trans.index:
            probs = self.immune_trans.loc[immune].values
            probs = probs / probs.sum()
            next_immune = np.random.choice(self.immune_trans.columns, p=probs)
        else:
            next_immune = "Mid"

        return {
            "initial_state": state,
            "arm": arm,
            "pcr_prob_step1": p_pcr,
            "next_immune": next_immune
        }

    def simulate(self, n: int = 500, states=None, arms=None, seed=42) -> pd.DataFrame:
        if states is None:
            states = self.pcr_prob["state"].unique()
        if arms is None:
            arms = self.pcr_prob["arm"].unique()
        np.random.seed(seed)
        results = []
        for _ in range(n):
            state = np.random.choice(states)
            arm = np.random.choice(arms)
            results.append(self.step(state, arm))
        return pd.DataFrame(results)

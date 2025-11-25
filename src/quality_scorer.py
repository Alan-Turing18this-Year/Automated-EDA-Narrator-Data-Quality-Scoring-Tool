# QualityScorer
# src/quality_scorer.py
from typing import Dict
import numpy as np

class QualityScorer:
    def __init__(self, eda_results: Dict, df_len: int):
        self.eda = eda_results
        self.df_len = df_len
        self.scores = {}

    def missing_score(self):
        missing = self.eda.get('missing', {})
        # average missing percentage across columns
        pcts = [v['pct'] for v in missing.values()] if missing else [0]
        mean_pct = np.mean(pcts)
        score = max(0, 100 - mean_pct)  # simplistic
        self.scores['missing'] = round(float(score), 2)
        return self.scores['missing']

    def duplicates_score(self):
        dups = self.eda.get('duplicates', 0)
        pct = (dups / max(1, self.df_len)) * 100
        score = max(0, 100 - pct * 2)  # penalise duplicates a bit more
        self.scores['duplicates'] = round(float(score), 2)
        return self.scores['duplicates']

    def outliers_score(self):
        out = self.eda.get('outliers', {})
        if not out:
            score = 100.0
        else:
            total_out = sum(out.values())
            pct = (total_out / max(1, self.df_len)) * 100
            score = max(0, 100 - pct * 1.5)
        self.scores['outliers'] = round(float(score), 2)
        return self.scores['outliers']


    def balance_score(self):
        # simple heuristic: if any categorical pct > 90% penalise
        missing = self.eda.get('missing', {})
        # No categorical detection here for brevity; return neutral
        self.scores['balance'] = 90.0
        return self.scores['balance']

    def overall_score(self):
        weights = {'missing': 0.35, 'duplicates': 0.15, 'outliers': 0.25, 'balance': 0.25}
        # ensure sub-scores exist
        for k in weights:
            if k not in self.scores:
                getattr(self, f"{k}_score")()
        total = sum(self.scores[k] * weights[k] for k in weights)
        self.scores['overall'] = round(float(total), 2)
        return self.scores['overall']

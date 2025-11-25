# src/quality_scorer.py

import pandas as pd

class QualityScorer:
    def __init__(self, eda_results, df_len):
        self.eda = eda_results
        self.df_len = df_len
        self.scores = {}

    # Example scoring methods
    def missing_score(self):
        missing_count = self.eda['missing'].sum()
        total = self.df_len * len(self.eda['missing'])
        score = max(0, 100 - (missing_count / total * 100))
        self.scores['missing'] = round(score, 2)

    def duplicates_score(self):  # RENAMED from duplicate_score -> duplicates_score
        duplicate_count = self.eda['duplicates']
        score = max(0, 100 - (duplicate_count / self.df_len * 100))
        self.scores['duplicates'] = round(score, 2)

    def outliers_score(self):
        outliers_count = self.eda['outliers'].sum()
        total = self.df_len * len(self.eda['outliers'])
        score = max(0, 100 - (outliers_count / total * 100))
        self.scores['outliers'] = round(score, 2)

    def balance_score(self):
        # Simplified example: give full score
        self.scores['balance'] = 90.0

    def overall_score(self):
        # Loop over all metrics and call corresponding methods
        for k in ['missing', 'duplicates', 'outliers', 'balance']:
            getattr(self, f"{k}_score")()
        # Calculate overall
        overall = sum(self.scores.values()) / len(self.scores)
        self.scores['overall'] = round(overall, 2)

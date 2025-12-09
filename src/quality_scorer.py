# Encapsulation + methods
# src/quality_scorer.py
"""
QualityScorer module for computing weighted data quality metrics.

This module evaluates different aspects of dataset quality using
EDA outputs, including:
- Missing value quality
- Duplicate row quality
- Outlier impact
- Balance score (placeholder)
It also computes a final weighted overall quality score.
"""

import numpy as np

class QualityScorer:
    """
    Class for computing multiple data quality scores based on EDA results.

    Attributes:
        _eda (dict): Protected dictionary of EDA results (missing, duplicates, outliers).
        _df_len (int): Number of rows in the dataset.
        scores (dict): Stores individual metric scores and final overall score.
    """

    def __init__(self, eda_results, df_len):
        """
        Initialize the QualityScorer with EDA results and dataset length.

        Args:
            eda_results (dict): Output dictionary from the EDAAnalyzer modules.
            df_len (int): Total number of rows in the dataset.
        """
        self._eda = eda_results
        self._df_len = df_len
        self.scores = {}

    def missing_score(self):
        """
        Compute the quality score based on missing value percentages.

        Returns:
            float: Score between 0 and 100 (higher = better quality).
        """
        missing = self._eda.get('missing', {})
        pct = [v['pct'] for v in missing.values()] if missing else [0]
        self.scores['missing'] = max(0, 100 - np.mean(pct))
        return self.scores['missing']

    def duplicate_score(self):
        """
        Compute the quality score based on duplicate rows.

        Returns:
            float: Score between 0 and 100 (higher = better).
        """
        dups = self._eda.get('duplicates', 0)
        pct = (dups / max(1, self._df_len)) * 100
        self.scores['duplicates'] = max(0, 100 - pct * 2)
        return self.scores['duplicates']

    def outlier_score(self):
        """
        Compute the quality score based on number of detected outliers.

        Returns:
            float: Score between 0 and 100 (higher = better).
        """
        out = self._eda.get('outliers', {})
        total = sum(out.values()) if out else 0
        pct = (total / max(1, self._df_len)) * 100
        self.scores['outliers'] = max(0, 100 - pct * 1.5)
        return self.scores['outliers']

    def balance_score(self):
        """
        Placeholder scoring for dataset balance.

        Returns:
            float: Score representing balance (currently fixed at 90.0).
        """
        self.scores['balance'] = 90.0
        return self.scores['balance']

    def overall_score(self):
        """
        Compute a weighted overall data quality score using:
            - Missing score (35%)
            - Duplicate score (15%)
            - Outlier score (25%)
            - Balance score (25%)

        Ensures all component metrics are computed before combining.

        Returns:
            float: Final weighted quality score between 0 and 100.
        """
        # Ensure all individual scores are computed
        for metric in ['missing', 'duplicates', 'outliers', 'balance']:
            if metric not in self.scores:
                getattr(self, f"{metric}_score")()

        weights = {
            'missing': 0.35,
            'duplicates': 0.15,
            'outliers': 0.25,
            'balance': 0.25
        }

        self.scores['overall'] = sum(self.scores[m] * w for m, w in weights.items())
        return self.scores['overall']

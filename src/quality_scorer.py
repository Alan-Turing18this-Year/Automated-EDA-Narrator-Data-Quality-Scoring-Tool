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
        _weights (dict): User-defined weights for each metric in overall score calculation.
        scores (dict): Stores individual metric scores and final overall score.
    """

    # Default weights as a class variable
    DEFAULT_WEIGHTS = {
        'missing': 0.35,
        'duplicates': 0.15,
        'outliers': 0.25,
        'balance': 0.25
    }

    def __init__(self, eda_results, df_len, weights=None):
        """
        Initialize the QualityScorer with EDA results and dataset length.

        Args:
            eda_results (dict): Output dictionary from the EDAAnalyzer modules.
            df_len (int): Total number of rows in the dataset.
            weights (dict, optional): Custom weights for metrics. 
                Keys: 'missing', 'duplicates', 'outliers', 'balance'
                Values must sum to 1.0. Defaults to None (uses default weights).
        
        Raises:
            ValueError: If custom weights don't sum to 1.0 or contain invalid keys.
        """
        self._eda = eda_results
        self._df_len = df_len
        self.scores = {}
        
        # Set weights with validation
        if weights is None:
            self._weights = self.DEFAULT_WEIGHTS.copy()
        else:
            self._validate_weights(weights)
            self._weights = weights.copy()

    def _validate_weights(self, weights):
        """
        Validate that custom weights are properly formatted.

        Args:
            weights (dict): User-provided weights dictionary.

        Raises:
            ValueError: If weights are invalid.
        """
        required_keys = set(self.DEFAULT_WEIGHTS.keys())
        provided_keys = set(weights.keys())
        
        # Check for missing or extra keys
        if provided_keys != required_keys:
            missing = required_keys - provided_keys
            extra = provided_keys - required_keys
            error_msg = []
            if missing:
                error_msg.append(f"Missing keys: {missing}")
            if extra:
                error_msg.append(f"Extra keys: {extra}")
            raise ValueError(
                f"Invalid weight keys. {' '.join(error_msg)}. "
                f"Required keys: {required_keys}"
            )
        
        # Check if weights sum to 1.0 (with small tolerance for floating point)
        weight_sum = sum(weights.values())
        if not (0.99 <= weight_sum <= 1.01):
            raise ValueError(
                f"Weights must sum to 1.0, but got {weight_sum:.4f}. "
                f"Provided weights: {weights}"
            )
        
        # Check if all weights are non-negative
        if any(w < 0 for w in weights.values()):
            raise ValueError("All weights must be non-negative.")

    def get_weights(self):
        """
        Get the current weights being used for scoring.

        Returns:
            dict: Copy of current weights dictionary.
        """
        return self._weights.copy()

    def set_weights(self, weights):
        """
        Update the weights used for overall score calculation.

        Args:
            weights (dict): New weights dictionary.

        Raises:
            ValueError: If weights are invalid.
        """
        self._validate_weights(weights)
        self._weights = weights.copy()
        
        # Recalculate overall score if it was already computed
        if 'overall' in self.scores:
            self.overall_score()

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

    def duplicates_score(self):
        """
        Compute the quality score based on duplicate rows.

        Returns:
            float: Score between 0 and 100 (higher = better).
        """
        dups = self._eda.get('duplicates', 0)
        pct = (dups / max(1, self._df_len)) * 100
        self.scores['duplicates'] = max(0, 100 - pct * 2)
        return self.scores['duplicates']

    def outliers_score(self):
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
        Compute a weighted overall data quality score using configured weights.

        Default weights:
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

        # Calculate weighted overall score using current weights
        self.scores['overall'] = sum(
            self.scores[m] * self._weights[m] 
            for m in self._weights.keys()
        )
        return self.scores['overall']

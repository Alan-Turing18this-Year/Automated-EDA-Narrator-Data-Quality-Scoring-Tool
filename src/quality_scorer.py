# Encapsulation + methods
import numpy as np

class QualityScorer:
    """
    Class for calculating data quality scores.

    Attributes:
        _eda (dict): EDA results used for scoring.
        _df_len (int): Number of rows in the dataset.
        scores (dict): Stores calculated scores.
    """

    def __init__(self, eda_results, df_len):
        """
        Initialize QualityScorer.

        Args:
            eda_results (dict): EDA results from analyzers.
            df_len (int): Number of rows in dataset.
        """
        self._eda = eda_results
        self._df_len = df_len
        self.scores = {}

    def missing_score(self):
        """Compute score based on missing values."""
        # implementation
        return self.scores.get('missing', 0)

    def duplicate_score(self):
        """Compute score based on duplicate rows."""
        return self.scores.get('duplicates', 0)

    def outlier_score(self):
        """Compute score based on numeric outliers."""
        return self.scores.get('outliers', 0)

    def balance_score(self):
        """Compute score based on class balance (categorical)."""
        return self.scores.get('balance', 0)

    def overall_score(self):
        """
        Compute overall weighted data quality score.

        Returns:
            float: Overall score.
        """
        return self.scores.get('overall', 0)


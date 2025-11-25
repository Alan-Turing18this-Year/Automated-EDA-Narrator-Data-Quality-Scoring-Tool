# Base class + inheritance + polymorphism
# src/eda_analyzer.py
"""
EDAAnalyzer module for performing exploratory data analysis (EDA) on datasets.

Provides base and specialized analyzers for numeric and categorical columns
of a pandas DataFrame, generating summary statistics for each type of data.
"""

import pandas as pd
import numpy as np

class EDAAnalyzer:
    """
    Base class for exploratory data analysis (EDA).

    Attributes:
        _df (pd.DataFrame): Protected DataFrame to analyze.
        results (dict): Dictionary to store analysis results.
    """

    def __init__(self, df):
        """
        Initialize the EDAAnalyzer with a DataFrame.

        Args:
            df (pd.DataFrame): Input DataFrame for analysis.
        """
        self._df = df
        self.results = {}

    def run_all(self):
        """
        Base method for EDA analysis (to be overridden in child classes).

        Returns:
            dict: Dictionary containing summary statistics of the DataFrame.
        """
        return {"summary": self._df.describe().to_dict()}


class NumericAnalyzer(EDAAnalyzer):
    """
    Performs EDA specifically on numeric columns of a DataFrame.
    """

    def run_all(self):
        """
        Generate summary statistics for numeric columns.

        Returns:
            dict: Dictionary containing summary statistics for numeric columns.
        """
        num = self._df.select_dtypes(include=[np.number])
        self.results['summary'] = num.describe().to_dict()
        return self.results


class CategoricalAnalyzer(EDAAnalyzer):
    """
    Performs EDA specifically on categorical columns of a DataFrame.
    """

    def run_all(self):
        """
        Generate summary statistics for categorical columns.

        Returns:
            dict: Dictionary containing summary statistics for categorical columns.
        """
        cat = self._df.select_dtypes(include=['object'])
        self.results['summary'] = cat.describe(include='all').to_dict()
        return self.results



# DataLoader
# src/loader.py
import pandas as pd
from typing import Optional

class DataLoader:
    def __init__(self, path: str, sample_n: Optional[int] = 5):
        self.path = path
        self.sample_n = sample_n
        self.df = None

    def load(self) -> pd.DataFrame:
        self.df = pd.read_csv(self.path)
        return self.df

    def peek(self):
        if self.df is None:
            raise RuntimeError("Data not loaded yet.")
        return self.df.head(self.sample_n)

    def detect_types(self):
        if self.df is None:
            raise RuntimeError("Data not loaded yet.")
        return self.df.dtypes.to_dict()

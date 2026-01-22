import pandas as pd
from pathlib import Path


class CSVHistoricalFeed:
    def __init__(self, data_path):
        self.data_path = Path(data_path)
        self.df = None
        self.pointer = 0

    def load(self, filename):
        file_path = self.data_path / filename

        if not file_path.exists():
            raise FileNotFoundError(f"Data file not found: {file_path}")

        self.df = pd.read_csv(file_path)
        self.df["datetime"] = pd.to_datetime(self.df["datetime"])
        self.df = self.df.sort_values("datetime").reset_index(drop=True)
        self.pointer = 0

    def stream(self):
        while self.pointer < len(self.df):
            candle = self.df.iloc[self.pointer]
            self.pointer += 1
            yield candle

import time
import pandas as pd
from pathlib import Path
from inputs.live_feed import LiveFeed


class SimulatedLiveFeed(LiveFeed):
    def __init__(self, data_path, filename, delay=1):
        self.file_path = Path(data_path) / filename
        self.delay = delay
        self.df = None

    def connect(self):
        self.df = pd.read_csv(self.file_path)
        self.df["datetime"] = pd.to_datetime(self.df["datetime"])
        self.df = self.df.sort_values("datetime").reset_index(drop=True)

    def stream(self):
        for _, candle in self.df.iterrows():
            time.sleep(self.delay)
            yield candle

from inputs.csv_feed import CSVHistoricalFeed
from strategies.indicators.vwap import VWAP
from strategies.vwap_signal import VWAPSignal
from strategies.position_manager import PositionManager


class SymbolEngine:
    def __init__(self, symbol, data_path, filename):
        self.symbol = symbol
        self.feed = CSVHistoricalFeed(data_path)
        self.feed.load(filename)

        self.vwap = VWAP()
        self.signal_engine = VWAPSignal()
        self.position_manager = PositionManager()

    def run(self):
        print(f"\n===== Scanning {self.symbol} =====")

        for candle in self.feed.stream():
            current_vwap = self.vwap.update(candle)
            signal = self.signal_engine.generate(
                candle["close"],
                current_vwap
            )

            print(
                self.symbol,
                candle["datetime"],
                "| Close:", round(candle["close"], 2),
                "| VWAP:", round(current_vwap, 2),
                "| Signal:", signal
            )

            self.position_manager.on_candle(candle, signal)

from inputs.csv_feed import CSVHistoricalFeed
from strategies.indicators.vwap import VWAP
from strategies.vwap_signal import VWAPSignal
from strategies.position_manager import PositionManager


def to_float(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


class SymbolEngine:
    def __init__(
        self,
        symbol,
        data_path,
        filename,
        news_provider,
        sl_pct,
        tgt_pct
    ):
        self.symbol = symbol
        self.feed = CSVHistoricalFeed(data_path)
        self.feed.load(filename)

        self.vwap = VWAP()
        self.signal_engine = VWAPSignal()
        self.position_manager = PositionManager(sl_pct, tgt_pct)
        self.news_provider = news_provider

    def get_trades(self):
        return self.position_manager.trades

    def run(self):
        print(f"\n===== Scanning {self.symbol} =====")

        for candle in self.feed.stream():

            close_price = to_float(candle["close"])
            if close_price is None:
                continue  # skip bad candle safely

            current_vwap = self.vwap.update(candle)

            signal = None
            if current_vwap is not None:
                signal = self.signal_engine.generate(
                    close_price,
                    current_vwap
                )

            trade_date = candle["datetime"].date()
            negative_news = self.news_provider.has_negative_news(
                self.symbol,
                trade_date
            )

            # Block BUY on negative news
            if signal == "BUY" and negative_news:
                print(
                    self.symbol,
                    candle["datetime"],
                    "| BUY BLOCKED due to NEGATIVE NEWS"
                )
                signal = None

            if signal or self.position_manager.position != "FLAT":
                print(
                    self.symbol,
                    candle["datetime"],
                    "| Close:", round(float(candle["close"]), 2),
                    "| VWAP:", round(current_vwap, 2) if current_vwap else None,
                    "| Signal:", signal
                )

            self.position_manager.on_candle(candle, signal)
        print(f"===== Finished {self.symbol} =====")
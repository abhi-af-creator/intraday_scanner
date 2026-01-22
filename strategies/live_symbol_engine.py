from strategies.indicators.vwap import VWAP
from strategies.vwap_signal import VWAPSignal
from strategies.position_manager import PositionManager


class LiveSymbolEngine:
    def __init__(self, symbol, feed, news_provider, sl_pct, tgt_pct,broker):
        self.symbol = symbol
        self.feed = feed
        self.news_provider = news_provider

        self.vwap = VWAP()
        self.signal_engine = VWAPSignal()
        self.position_manager = PositionManager(sl_pct, tgt_pct, broker=broker, symbol=symbol)

    def run(self):
        print(f"\n🔴 LIVE MODE: {self.symbol}")

        self.feed.connect()

        for candle in self.feed.stream():
            current_vwap = self.vwap.update(candle)
            signal = self.signal_engine.generate(
                candle["close"], current_vwap
            )

            trade_date = candle["datetime"].date()
            if signal == "BUY" and self.news_provider.has_negative_news(
                self.symbol, trade_date
            ):
                print(self.symbol, candle["datetime"], "BUY BLOCKED (NEWS)")
                signal = None

            print(
                self.symbol,
                candle["datetime"],
                "| Close:", round(candle["close"], 2),
                "| VWAP:", round(current_vwap, 2),
                "| Signal:", signal
            )

            self.position_manager.on_candle(candle, signal)

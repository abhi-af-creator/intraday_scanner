from config import DATA_PATH
from inputs.csv_feed import CSVHistoricalFeed
from strategies.indicators.vwap import VWAP
from strategies.vwap_signal import VWAPSignal
from strategies.position_manager import PositionManager


def main():
    print("Intraday scanner initialized successfully!\n")

    feed = CSVHistoricalFeed(DATA_PATH)
    feed.load("TEST_STOCK_5min_2025.csv")

    vwap = VWAP()
    signal_engine = VWAPSignal()
    position_manager = PositionManager()

    print("Replaying market data with VWAP & signals:\n")

    for candle in feed.stream():
        current_vwap = vwap.update(candle)
        signal = signal_engine.generate(candle["close"], current_vwap)

        print(
            candle["datetime"],
            "| Close:", round(candle["close"], 2),
            "| VWAP:", round(current_vwap, 2),
            "| Signal:", signal
        )
        position_manager.on_candle(candle, signal)
        #if signal:
        #    position_manager.on_signal(
        #        signal,
        #        candle["close"],
        #        candle["datetime"]
        #    )


if __name__ == "__main__":
    main()

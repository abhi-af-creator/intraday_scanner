from config import DATA_PATH
from inputs.simulated_live_feed import SimulatedLiveFeed
from inputs.no_news import NoNewsProvider
from strategies.live_symbol_engine import LiveSymbolEngine
from inputs.composite_news import CompositeNewsProvider



SL = 0.005
TARGET = 0.01


def main():
    news_provider = CompositeNewsProvider()

    feed = SimulatedLiveFeed(
        DATA_PATH,
        "TEST_STOCK_5min_2025.csv",
        delay=1
    )

    engine = LiveSymbolEngine(
        "TEST_STOCK",
        feed,
        news_provider,
        SL,
        TARGET
    )

    engine.run()


if __name__ == "__main__":
    main()

from config import DATA_PATH
from inputs.simulated_live_feed import SimulatedLiveFeed
from inputs.no_news import NoNewsProvider
from strategies.live_symbol_engine import LiveSymbolEngine
from execution.zerodha import ZerodhaBroker


API_KEY = "YOUR_API_KEY"
ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"

SL = 0.005
TARGET = 0.01


def main():
    broker = ZerodhaBroker(
        api_key=API_KEY,
        access_token=ACCESS_TOKEN,
        paper=True   # 🔴 PAPER MODE
    )

    feed = SimulatedLiveFeed(
        DATA_PATH,
        "TEST_STOCK_5min_2025.csv",
        delay=1
    )

    engine = LiveSymbolEngine(
        "TEST_STOCK",
        feed,
        NoNewsProvider(),
        SL,
        TARGET,
        broker
    )

    engine.run()


if __name__ == "__main__":
    main()

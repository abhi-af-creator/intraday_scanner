from config import DATA_PATH, SYMBOLS
from strategies.symbol_engine import SymbolEngine
from strategies.performance import PerformanceAnalyzer
from inputs.no_news import NoNewsProvider


TRAIN_START = "2025-09-01"
TRAIN_END   = "2025-09-30"
TEST_START  = "2025-10-01"
TEST_END    = "2025-10-31"

BEST_SL  = 0.005   # from STEP 14
BEST_TGT = 0.01


def run_walk_forward():
    news_provider = NoNewsProvider()

    print("\n🔁 WALK-FORWARD TEST (OUT-OF-SAMPLE)")
    print("=" * 45)

    performance = PerformanceAnalyzer()

    for symbol in SYMBOLS:
        filename = f"{symbol}_5min_2025.csv"

        engine = SymbolEngine(
            symbol,
            DATA_PATH,
            filename,
            news_provider,
            BEST_SL,
            BEST_TGT
        )

        # Reload feed with TEST period only
        engine.feed.load(
            filename,
            start_date=TEST_START,
            end_date=TEST_END
        )

        engine.run()
        performance.add_trades(engine.get_trades())

    performance.report()


if __name__ == "__main__":
    run_walk_forward()

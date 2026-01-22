from config import DATA_PATH, SYMBOLS
from strategies.symbol_engine import SymbolEngine
from strategies.performance import PerformanceAnalyzer
from inputs.composite_news import CompositeNewsProvider


SL_PCT = 0.005
TGT_PCT = 0.01


def main():
    print("Intraday multi-stock scanner started 🚀")

    engines = []
    performance = PerformanceAnalyzer()
    news_provider = CompositeNewsProvider()

    for symbol in SYMBOLS:
        filename = f"{symbol}_5min_2025.csv"

        engine = SymbolEngine(
            symbol,
            DATA_PATH,
            filename,
            news_provider,
            SL_PCT,
            TGT_PCT
        )
        engines.append(engine)

    for engine in engines:
        engine.run()
        performance.add_trades(engine.get_trades())

    performance.report()


if __name__ == "__main__":
    main()

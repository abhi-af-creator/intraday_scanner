from config import DATA_PATH, SYMBOLS
from strategies.symbol_engine import SymbolEngine
from strategies.performance import PerformanceAnalyzer
from inputs.mock_news import MockNewsProvider
from inputs.composite_news import CompositeNewsProvider





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
            news_provider
        )
        engines.append(engine)

    for engine in engines:
        engine.run()
        performance.add_trades(engine.get_trades())

    performance.report()


if __name__ == "__main__":
    main()

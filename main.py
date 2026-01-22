from config import DATA_PATH, SYMBOLS
from strategies.symbol_engine import SymbolEngine


def main():
    print("Intraday multi-stock scanner started 🚀")

    engines = []

    for symbol in SYMBOLS:
        filename = f"{symbol}_5min_2025.csv"
        engine = SymbolEngine(symbol, DATA_PATH, filename)
        engines.append(engine)

    for engine in engines:
        engine.run()


if __name__ == "__main__":
    main()

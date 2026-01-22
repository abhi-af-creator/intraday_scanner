from pathlib import Path

from config import DATA_PATH, SYMBOLS, DATA_INTERVAL, HISTORICAL_PERIOD
from strategies.symbol_engine import SymbolEngine
from strategies.performance import PerformanceAnalyzer
from inputs.composite_news import CompositeNewsProvider
from services.import_data import download_intraday_data


SL_PCT = 0.005
TGT_PCT = 0.01


def ensure_data(symbol):
    filename = f"{symbol}_{DATA_INTERVAL}_{HISTORICAL_PERIOD}.csv"
    filepath = DATA_PATH / filename

    if not filepath.exists():
        print(f"⚠️ Data missing for {symbol}. Downloading...")
        download_intraday_data(
            symbol=symbol,
            interval=DATA_INTERVAL,
            period=HISTORICAL_PERIOD,
            output_dir=DATA_PATH
        )
    else:
        print(f"✅ Data already exists for {symbol}")

    return filename


def main():
    print("Intraday multi-stock scanner started 🚀")

    engines = []
    performance = PerformanceAnalyzer()
    news_provider = CompositeNewsProvider()

    for symbol in SYMBOLS:
        filename = ensure_data(symbol)

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

from config import DATA_PATH, SYMBOLS
from strategies.symbol_engine import SymbolEngine
from strategies.performance import PerformanceAnalyzer
from inputs.no_news import NoNewsProvider
from inputs.composite_news import CompositeNewsProvider



STOP_LOSS_VALUES = [0.003, 0.005, 0.007]
TARGET_VALUES = [0.008, 0.01, 0.015]


def run_optimisation():
    news_provider = CompositeNewsProvider()

    results = []

    for sl in STOP_LOSS_VALUES:
        for tgt in TARGET_VALUES:
            performance = PerformanceAnalyzer()

            for symbol in SYMBOLS:
                filename = f"{symbol}_5min_2025.csv"
                engine = SymbolEngine(
                    symbol,
                    DATA_PATH,
                    filename,
                    news_provider,
                    sl,
                    tgt
                )
                engine.run()
                performance.add_trades(engine.get_trades())

            total_pnl = sum(t["pnl"] for t in performance.trades)

            results.append({
                "stop_loss": sl,
                "target": tgt,
                "total_pnl": total_pnl,
                "trades": len(performance.trades)
            })

    return results


if __name__ == "__main__":
    results = run_optimisation()

    print("\n📊 OPTIMISATION RESULTS")
    print("-" * 40)
    for r in results:
        print(
            f"SL={r['stop_loss']}, "
            f"TGT={r['target']} → "
            f"PnL=₹{round(r['total_pnl'],2)}, "
            f"Trades={r['trades']}"
        )

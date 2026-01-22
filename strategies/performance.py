class PerformanceAnalyzer:
    def __init__(self):
        self.trades = []

    def add_trades(self, trades):
        self.trades.extend(trades)

    def report(self):
        if not self.trades:
            print("\n📊 No trades executed.")
            return

        total_pnl = sum(t["pnl"] for t in self.trades)
        wins = [t for t in self.trades if t["pnl"] > 0]
        losses = [t for t in self.trades if t["pnl"] <= 0]

        win_rate = (len(wins) / len(self.trades)) * 100

        avg_win = sum(t["pnl"] for t in wins) / len(wins) if wins else 0
        avg_loss = sum(t["pnl"] for t in losses) / len(losses) if losses else 0

        print("\n📊 PERFORMANCE REPORT")
        print("-" * 30)
        print(f"Total Trades : {len(self.trades)}")
        print(f"Win Rate     : {round(win_rate,2)}%")
        print(f"Total PnL    : ₹{round(total_pnl,2)}")
        print(f"Avg Win      : ₹{round(avg_win,2)}")
        print(f"Avg Loss     : ₹{round(avg_loss,2)}")

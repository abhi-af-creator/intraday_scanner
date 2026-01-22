from config import (
    CAPITAL,
    RISK_PER_TRADE,
    STOP_LOSS_PCT,
    TARGET_PCT
)


class PositionManager:
    def __init__(self):
        self.position = "FLAT"
        self.entry_price = None
        self.stop_loss = None
        self.target = None
        self.qty = 0
        self.trades = []

    def calculate_quantity(self, entry_price):
        risk_amount = CAPITAL * RISK_PER_TRADE
        risk_per_share = entry_price * STOP_LOSS_PCT

        if risk_per_share <= 0:
            return 0

        qty = int(risk_amount / risk_per_share)
        return max(qty, 0)

    def enter_long(self, price, timestamp):
        self.qty = self.calculate_quantity(price)

        if self.qty == 0:
            print("⚠️ Quantity calculated as 0. Trade skipped.")
            return

        self.position = "LONG"
        self.entry_price = price
        self.stop_loss = price * (1 - STOP_LOSS_PCT)
        self.target = price * (1 + TARGET_PCT)

        print(
            f"🟢 BUY {self.qty} @ {round(price,2)} | "
            f"SL: {round(self.stop_loss,2)} | "
            f"TARGET: {round(self.target,2)} | {timestamp}"
        )

    def exit_long(self, price, timestamp, reason):
        pnl_per_share = price - self.entry_price
        total_pnl = pnl_per_share * self.qty

        self.trades.append({
            "entry": self.entry_price,
            "exit": price,
            "qty": self.qty,
            "pnl": total_pnl,
            "reason": reason
        })

        print(
            f"🔴 EXIT {self.qty} @ {round(price,2)} | "
            f"PnL: ₹{round(total_pnl,2)} | "
            f"Reason: {reason} | {timestamp}"
        )

        self.position = "FLAT"
        self.entry_price = None
        self.stop_loss = None
        self.target = None
        self.qty = 0

    def on_candle(self, candle, signal):
        price = candle["close"]
        timestamp = candle["datetime"]

        if self.position == "FLAT":
            if signal == "BUY":
                self.enter_long(price, timestamp)

        elif self.position == "LONG":
            if price <= self.stop_loss:
                self.exit_long(price, timestamp, "STOP_LOSS")

            elif price >= self.target:
                self.exit_long(price, timestamp, "TARGET")

            elif signal == "SELL":
                self.exit_long(price, timestamp, "SIGNAL_EXIT")

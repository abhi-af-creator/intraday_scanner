from config import (
    CAPITAL,
    RISK_PER_TRADE,
    SLIPPAGE_PCT,
    BROKERAGE_PCT,
    DAILY_MAX_LOSS,
    MAX_TRADES_PER_DAY
)


class PositionManager:
    def __init__(self, stop_loss_pct, target_pct, broker=None, symbol=None):
        # Strategy parameters
        self.stop_loss_pct = float(stop_loss_pct)
        self.target_pct = float(target_pct)

        # Broker
        self.broker = broker
        self.symbol = symbol

        # Position state
        self.position = "FLAT"
        self.entry_price = None
        self.stop_loss = None
        self.target = None
        self.qty = 0

        # Risk & tracking
        self.trades = []
        self.trades_today = 0
        self.day_pnl = 0.0

    # -------------------------
    # Internal helpers
    # -------------------------

    def _apply_slippage(self, price, side):
        price = float(price)   # ✅ CRITICAL FIX

        if side == "BUY":
            return price * (1 + SLIPPAGE_PCT)
        else:
            return price * (1 - SLIPPAGE_PCT)

    def _apply_costs(self, pnl):
        pnl = float(pnl)
        brokerage = abs(pnl) * BROKERAGE_PCT * 2
        return pnl - brokerage

    def calculate_quantity(self, entry_price):
        entry_price = float(entry_price)

        risk_amount = CAPITAL * RISK_PER_TRADE
        risk_per_share = entry_price * self.stop_loss_pct

        if risk_per_share <= 0:
            return 0

        return int(risk_amount / risk_per_share)

    # -------------------------
    # Trade lifecycle
    # -------------------------

    def enter_long(self, price, timestamp):
        price = float(price)   # ✅ SAFETY CAST

        if self.trades_today >= MAX_TRADES_PER_DAY:
            print("⚠️ Max trades reached for the day. BUY blocked.")
            return

        if self.day_pnl <= -DAILY_MAX_LOSS:
            print("🛑 Daily loss limit hit. Trading stopped.")
            return

        price = self._apply_slippage(price, "BUY")
        qty = self.calculate_quantity(price)

        if qty <= 0:
            print("⚠️ Quantity calculated as 0. BUY skipped.")
            return

        self.position = "LONG"
        self.entry_price = price
        self.qty = qty
        self.stop_loss = price * (1 - self.stop_loss_pct)
        self.target = price * (1 + self.target_pct)
        self.trades_today += 1

        print(
            f"🟢 BUY {qty} @ {round(price,2)} "
            f"| SL: {round(self.stop_loss,2)} "
            f"| TARGET: {round(self.target,2)} "
            f"| {timestamp}"
        )

        if self.broker:
            self.broker.place_order(
                symbol=self.symbol,
                side="BUY",
                qty=qty
            )

    def exit_long(self, price, timestamp, reason):
        price = float(price)   # ✅ SAFETY CAST
        price = self._apply_slippage(price, "SELL")

        raw_pnl = (price - self.entry_price) * self.qty
        net_pnl = self._apply_costs(raw_pnl)

        self.trades.append({
            "entry": self.entry_price,
            "exit": price,
            "qty": self.qty,
            "pnl": net_pnl,
            "reason": reason
        })

        self.day_pnl += net_pnl

        print(
            f"🔴 EXIT {self.qty} @ {round(price,2)} "
            f"| Net PnL: ₹{round(net_pnl,2)} "
            f"| Reason: {reason} "
            f"| Day PnL: ₹{round(self.day_pnl,2)} "
            f"| {timestamp}"
        )

        if self.broker:
            self.broker.place_order(
                symbol=self.symbol,
                side="SELL",
                qty=self.qty
            )

        # Reset position
        self.position = "FLAT"
        self.entry_price = None
        self.stop_loss = None
        self.target = None
        self.qty = 0

    # -------------------------
    # Candle handler
    # -------------------------

    def on_candle(self, candle, signal):
        price = float(candle["close"])     # ✅ FINAL GUARD
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

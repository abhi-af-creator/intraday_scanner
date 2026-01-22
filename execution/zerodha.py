from kiteconnect import KiteConnect
from execution.broker import Broker


class ZerodhaBroker(Broker):
    def __init__(self, api_key, access_token, paper=True):
        self.paper = paper
        self.kite = KiteConnect(api_key=api_key)
        self.kite.set_access_token(access_token)

    def place_order(self, symbol, side, qty, price=None):
        if self.paper:
            print(f"🧾 PAPER ORDER → {side} {qty} {symbol} @ {price}")
            return None

        transaction_type = (
            self.kite.TRANSACTION_TYPE_BUY
            if side == "BUY"
            else self.kite.TRANSACTION_TYPE_SELL
        )

        return self.kite.place_order(
            variety=self.kite.VARIETY_REGULAR,
            exchange=self.kite.EXCHANGE_NSE,
            tradingsymbol=symbol,
            transaction_type=transaction_type,
            quantity=qty,
            order_type=self.kite.ORDER_TYPE_MARKET,
            product=self.kite.PRODUCT_MIS
        )

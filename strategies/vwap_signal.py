class VWAPSignal:
    def __init__(self):
        self.previous_close = None
        self.previous_vwap = None

    def generate(self, close_price, vwap):
        signal = None

        if self.previous_close is not None and self.previous_vwap is not None:
            # Bullish cross
            if self.previous_close < self.previous_vwap and close_price > vwap:
                signal = "BUY"

            # Bearish cross
            elif self.previous_close > self.previous_vwap and close_price < vwap:
                signal = "SELL"

        self.previous_close = close_price
        self.previous_vwap = vwap

        return signal

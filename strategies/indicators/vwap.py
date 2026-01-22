class VWAP:
    def __init__(self):
        self.cumulative_pv = 0.0
        self.cumulative_volume = 0
        self.current_date = None

    def update(self, candle):
        candle_date = candle["datetime"].date()

        # Reset at start of new trading day
        if self.current_date != candle_date:
            self.current_date = candle_date
            self.cumulative_pv = 0.0
            self.cumulative_volume = 0

        typical_price = (
            candle["high"] + candle["low"] + candle["close"]
        ) / 3

        self.cumulative_pv += typical_price * candle["volume"]
        self.cumulative_volume += candle["volume"]

        if self.cumulative_volume == 0:
            return None

        return self.cumulative_pv / self.cumulative_volume

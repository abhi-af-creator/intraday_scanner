class VWAP:
    def __init__(self):
        self.cumulative_pv = 0.0
        self.cumulative_volume = 0.0
        self.current_date = None

    def update(self, candle):
        candle_date = candle["datetime"].date()

        # Reset at start of new trading day
        if self.current_date != candle_date:
            self.current_date = candle_date
            self.cumulative_pv = 0.0
            self.cumulative_volume = 0.0

        try:
            high = float(candle["high"])
            low = float(candle["low"])
            close = float(candle["close"])
            volume = float(candle["volume"])
        except (ValueError, TypeError):
            return None  # skip bad candles safely

        if volume <= 0:
            return None

        typical_price = (high + low + close) / 3

        self.cumulative_pv += typical_price * volume
        self.cumulative_volume += volume

        return self.cumulative_pv / self.cumulative_volume

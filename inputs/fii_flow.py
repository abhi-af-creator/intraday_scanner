from inputs.news_provider import NewsProvider


class FIINewsProvider(NewsProvider):
    def __init__(self):
        # Mock data (replace with NSE / NSDL later)
        self.fii_flow = {
            "2025-10-01": -7200,  # heavy selling
            "2025-10-02":  3500
        }

        self.threshold = -5000  # ₹ Cr

    def has_negative_news(self, symbol, date):
        date_str = date.strftime("%Y-%m-%d")
        flow = self.fii_flow.get(date_str, 0)

        return flow <= self.threshold

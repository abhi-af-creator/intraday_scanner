from inputs.news_provider import NewsProvider


class MockNewsProvider(NewsProvider):
    def __init__(self):
        # Hardcoded negative-news days (for testing)
        self.negative_news = {
            "TEST_STOCK": ["2025-10-01"],
            "TEST_STOCK_2": []
        }

    def has_negative_news(self, symbol, date):
        date_str = date.strftime("%Y-%m-%d")
        return date_str in self.negative_news.get(symbol, [])

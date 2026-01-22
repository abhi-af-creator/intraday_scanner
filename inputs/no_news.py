from inputs.news_provider import NewsProvider


class NoNewsProvider(NewsProvider):
    def has_negative_news(self, symbol, date):
        return False
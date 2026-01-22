from inputs.et_news import EconomicTimesNewsProvider
from inputs.fii_flow import FIINewsProvider
from inputs.news_provider import NewsProvider


class CompositeNewsProvider(NewsProvider):
    def __init__(self):
        self.et = EconomicTimesNewsProvider()
        self.fii = FIINewsProvider()

    def has_negative_news(self, symbol, date):
        if self.et.has_negative_news(symbol, date):
            return True

        if self.fii.has_negative_news(symbol, date):
            return True

        return False

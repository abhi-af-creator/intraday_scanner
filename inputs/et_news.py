import feedparser
from inputs.news_provider import NewsProvider


class EconomicTimesNewsProvider(NewsProvider):
    def __init__(self):
        self.feed_url = (
            "https://economictimes.indiatimes.com/markets/rssfeeds/1977021501.cms"
        )

        # Simple negative keywords (expand later)
        self.negative_keywords = [
            "falls",
            "drops",
            "declines",
            "profit down",
            "loss",
            "weak",
            "misses",
            "downgrade",
            "sell-off",
            "regulatory",
            "penalty"
        ]

    def has_negative_news(self, symbol, date):
        feed = feedparser.parse(self.feed_url)

        for entry in feed.entries:
            title = entry.title.lower()

            # crude symbol match (improve later)
            if symbol.lower() in title:
                for word in self.negative_keywords:
                    if word in title:
                        return True

        return False

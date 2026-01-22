class LiveFeed:
    def connect(self):
        raise NotImplementedError

    def stream(self):
        """
        Should yield live candles one by one
        """
        raise NotImplementedError

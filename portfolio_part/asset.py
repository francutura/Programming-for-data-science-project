from constants import DATE_FORMAT


class Asset:
    def __init__(self, ticker, data):
        self.ticker = ticker
        self.data = data
        self.data.sort(key=lambda x: x[0])

    def __repr__(self):
        return self.ticker

    def _fix_missing_data(data):
        return data

    # TODO
    def return_(self, percentage):
        pass

    # TODO
    def volatility(self):
        pass

    def pretty_print_data(self):
        for entry in self.data:
            print(f"{entry[0].strftime(DATE_FORMAT)} - {entry[1]}")

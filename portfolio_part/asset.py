import statistics
import datetime

from constants import DATE_FORMAT, DATE_START, DATE_END


class Asset:
    def __init__(self, ticker, data):
        self.ticker = ticker
        self._data = data
        self.return_ = self._return_()
        self.volatility = self._volatility()
        self._fix_missing_data()

    def __repr__(self):
        return self.ticker

    def _fix_missing_data(self):
        """Fill dates that are missing from date range.

        Takes the avreage of values from dates between the
        missing dates and creates new entries that weren't
        present in the dataset before.

        Args:
            data (list): Asset data
        """
        self._data.sort(key=lambda x: x[0])

        i = 0
        data_len = len(self._data)
        curr_date = DATE_START

        while i < data_len:

            if curr_date > DATE_END:
                break

            # if the date is missing
            if self._data[i][0] != curr_date:
                if i - 1 < 0:
                    self._data.insert(i, (curr_date, self._data[i][1]))
                else:
                    self._data.insert(
                        i, (curr_date, (self._data[i][1] + self._data[i - 1][1]) / 2)
                    )

                curr_date += datetime.timedelta(days=1)
                data_len += 1
                i += 1
                continue

            curr_date += datetime.timedelta(days=1)
            i += 1

    def _return_(self):
        """Compute the ticker return.

        Returns:
            float: stock return
        """
        return ((self._data[-1][1] - self._data[0][1]) / self._data[0][1]) * 100

    def _volatility(self):
        """Compute the ticker volatility.

        Returns:
            float: volatility
        """
        return statistics.stdev([ele[1] for ele in self._data])

    def pretty_print_data(self):
        """Pretty print historical price data."""
        for entry in self._data:
            print(f"{entry[0].strftime(DATE_FORMAT)} - {entry[1]}")

import csv
import datetime

from constants import AssetData, DATE_FORMAT, DATE_END, DATE_START
from asset import Asset


def create_assets():
    """Creates a dictionary with avaliable asset
    and historical data pairs.

    Returns:
        dict: asset ticker -> Asset
    """
    assets = {}

    # creating assets
    for ticker, path in AssetData.items():
        data = []
        try:
            with open(path) as csvfile:
                reader = csv.reader(csvfile)

                # Skip header
                next(reader)
                for row in reader:
                    row[0] = datetime.datetime.strptime(row[0], DATE_FORMAT)
                    row[1] = float(row[1])
                    data.append(row)

            asset = Asset(ticker, data)
            assets[ticker] = asset
        except Exception:
            print(f"Failed to create asset '{ticker}'")
            continue

    return assets


def fix_missing_data(data, date_start, date_end):

    i = 0
    data_len = len(data)
    curr_date = date_start

    while i < data_len:

        # if the date is missing
        if data[i][0] != curr_date:
            if i - 1 < 0:
                data.insert(i, (curr_date, data[i][1]))
            else:
                data.insert(i, (curr_date, (data[i][1] + data[i - 1][1]) / 2))

            curr_date += datetime.timedelta(days=1)
            data_len += 1
            i += 1
            continue

        curr_date += datetime.timedelta(days=1)
        i += 1

    return data


if __name__ == "__main__":
    # create the assets
    assets = create_assets()

    # fix missing dates
    for ticker, asset in assets.items():
        asset.pretty_print_data()
        print()
        assets[ticker].data = fix_missing_data(asset.data, DATE_START, DATE_END)
        assets[ticker].pretty_print_data()
        break

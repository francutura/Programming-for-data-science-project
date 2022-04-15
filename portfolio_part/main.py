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


#def fix_missing_data(data, date_start, date_end):

if __name__ == "__main__":
    # create the assets
    assets = create_assets()

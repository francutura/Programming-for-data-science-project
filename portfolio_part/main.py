import csv
import datetime
import itertools
import statistics

from constants import AssetData, DATE_FORMAT, PORTFOLIO_ALLOCATIONS_PATH
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


# def fix_missing_data(data, date_start, date_end):

if __name__ == "__main__":
    # create the assets
    assets = create_assets()

    # creating portfolios
    portfolios = []
    combs = []
    for asset in AssetData.keys():
        combs.extend([asset] * 5)

    for comb in set(itertools.combinations(combs, 5)):
        portfolio = dict(zip(AssetData.keys(), [0] * len(AssetData.keys())))
        for ticker in comb:
            portfolio[ticker] += 20
        portfolios.append(portfolio)

    # sub-task save portfolios
    with open(PORTFOLIO_ALLOCATIONS_PATH, "w") as csvfile:
        writer = csv.DictWriter(csvfile, AssetData.keys())
        writer.writeheader()
        writer.writerows(portfolios)

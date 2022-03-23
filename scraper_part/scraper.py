import requests
import csv
import bs4
import os

from constants import (
    MAIN_PAGE_URL,
    HISTORICAL_DATA_URL,
    CSV_COLUMNS,
    HEADERS,
    POST_HEADERS,
    AMUNDI_HISTORICAL_DATA,
    AMUNDI_HEADERS,
    AMUNDI_OUTPUT_PATH,
    AMUNDI_POST_DATA,
    ISHARES_HISTORICAL_DATA,
    ISHARES_HEADERS,
    ISHARES_OUTPUT_PATH,
    ISHARES_POST_DATA,
    GOLD_HISTORICAL_DATA,
    GOLD_HEADERS,
    GOLD_OUTPUT_PATH,
    GOLD_POST_DATA,
    DOLLAR_HISTORICAL_DATA,
    DOLLAR_HEADERS,
    DOLLAR_OUTPUT_PATH,
    DOLLAR_POST_DATA,
    BONDS_HISTORICAL_DATA,
    BONDS_HEADERS,
    BONDS_OUTPUT_PATH,
    BONDS_POST_DATA,
)


def parse_scraped_data(data):
    """Parses HTML for historical price
    data on given ticker

    Args:
        data (str): raw HTML AST

    Returns:
        list: list of dict pairs:
            DATE: date of price
            PRICE: price of ticker
    """
    soup = bs4.BeautifulSoup(data, features="lxml")
    retval = []

    for entry in soup.find_all("tr"):
        rows = entry.find_all("td")

        if not rows:
            continue

        date = rows[0].string
        price = rows[1].string

        if not date or not price:
            continue

        retval.append({"Date": date, "Price": price})

    return retval


def get_historical_data(session, data, headers):
    """Retrives the historical price data for a given
    ticker.

    Args:
        session (requests.Session): investment.com session
        data (str): POST data
        headers (dict): POST headers

    Returns:
        list: historical data
    """

    # Add the POST request headers
    headers.update(POST_HEADERS)

    # Retrive historical data
    x = session.post(
        HISTORICAL_DATA_URL, data=data, headers=headers, allow_redirects=False
    )

    # Parse the data
    retval = parse_scraped_data(x.text)

    return retval


def save_historical_data(path, data):
    """Save scraped historical data on a ticker
    in a CSV formatted file.

    Args:
        path (str): path
        data (list): historical data
    """
    try:
        with open(path, "w") as csvfile:
            writer = csv.DictWriter(csvfile, CSV_COLUMNS)
            writer.writeheader()
            writer.writerows(data)
    except IOError:
        print(f"Failed writing data to path '{path}'")
        return

    print(f"Saved data to {os.path.basename(path)} file")


def run_scrape(ticker, session, his_data_url, post_data, headers, output_path):
    """Run scrape routine on a ticker.

    Args:
        ticker (str): string repr of ticker
        session (requests.Session): investing.com session
        his_data_url (str): historical data URL
        post_data (str): POST str
        headers (dict): POST headers
        output_path (str): path to save file
    """
    try:
        session.get(his_data_url)
        data = get_historical_data(session, post_data, headers)
        save_historical_data(output_path, data)
    except Exception:
        print(f"Failed parsing {ticker} data")


def main():
    session = requests.Session()
    session.headers.update(HEADERS)

    run_scrape(
        "AMUNDI",
        session,
        AMUNDI_HISTORICAL_DATA,
        AMUNDI_POST_DATA,
        AMUNDI_HEADERS,
        AMUNDI_OUTPUT_PATH,
    )
    run_scrape(
        "ISHARES",
        session,
        ISHARES_HISTORICAL_DATA,
        ISHARES_POST_DATA,
        ISHARES_HEADERS,
        ISHARES_OUTPUT_PATH,
    )
    run_scrape(
        "GOLD",
        session,
        GOLD_HISTORICAL_DATA,
        GOLD_POST_DATA,
        GOLD_HEADERS,
        GOLD_OUTPUT_PATH,
    )
    run_scrape(
        "DOLLAR",
        session,
        DOLLAR_HISTORICAL_DATA,
        DOLLAR_POST_DATA,
        DOLLAR_HEADERS,
        DOLLAR_OUTPUT_PATH,
    )
    run_scrape(
        "BONDS",
        session,
        BONDS_HISTORICAL_DATA,
        BONDS_POST_DATA,
        BONDS_HEADERS,
        BONDS_OUTPUT_PATH,
    )


if __name__ == "__main__":
    main()

import os

######### SHARED #########
MAIN_PAGE_URL = "https://www.investing.com"
HISTORICAL_DATA_URL = "https://www.investing.com/instruments/HistoricalDataAjax"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0",
    "Accept": "text/plain, */*; q=0.01",
    "Accept-Language": "en-US,en;q=0.5",
    "Content-Type": "application/x-www-form-urlencoded",
    "DNT": "1",
    "Connection": "keep-alive",
}

OUTPUT_PATH = "./scraper_part/scraped_csvs"
CSV_COLUMNS = ["Date", "Price"]

POST_HEADERS = {
    "Origin": "https://www.investing.com",
    "X-Requested-With": "XMLHttpRequest",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
}
##########################

######### AMUDI ##########
AMUNDI_HISTORICAL_DATA = (
    "https://www.investing.com/funds/amundi-msci-wrld-ae-c-historical-data"
)

AMUNDI_HEADERS = {
    "Referer": AMUNDI_HISTORICAL_DATA,
}

AMUNDI_POST_DATA = "curr_id=1084955&smlID=27416334&header=0P00012PP6+Historical+Data&st_date=01%2F01%2F2020&end_date=12%2F31%2F2020&interval_sec=Daily&sort_col=date&sort_ord=DESC&action=historical_data"

AMUNDI_OUTPUT_FILE = "amundi-msci-wrld-ae-c.csv"
AMUNDI_OUTPUT_PATH = os.path.join(OUTPUT_PATH, AMUNDI_OUTPUT_FILE)
##########################

######### CRPS ###########
ISHARES_HISTORICAL_DATA = (
    "https://www.investing.com/etfs/ishares-global-corporate-bond-$-historical-data"
)

ISHARES_HEADERS = {
    "Referer": ISHARES_HISTORICAL_DATA,
}

ISHARES_POST_DATA = "curr_id=45643&smlID=2530956&header=CRPS+Historical+Data&st_date=01%2F01%2F2020&end_date=12%2F31%2F2020&interval_sec=Daily&sort_col=date&sort_ord=DESC&action=historical_data"

ISHARES_OUTPUT_FILE = "ishares-global-corporate-bond-$.csv"
ISHARES_OUTPUT_PATH = os.path.join(OUTPUT_PATH, ISHARES_OUTPUT_FILE)
##########################

######### GOLD ###########
GOLD_HISTORICAL_DATA = "https://www.investing.com/etfs/spdr-gold-trust-historical-data"

GOLD_HEADERS = {
    "Referer": GOLD_HISTORICAL_DATA,
}

GOLD_POST_DATA = "curr_id=9227&smlID=2501017&header=GLD+Historical+Data&st_date=01%2F01%2F2020&end_date=12%2F31%2F2020&interval_sec=Daily&sort_col=date&sort_ord=DESC&action=historical_data"

GOLD_OUTPUT_FILE = "spdr-gold-trust.csv"
GOLD_OUTPUT_PATH = os.path.join(OUTPUT_PATH, GOLD_OUTPUT_FILE)
##########################

######## DOLLAR ##########
DOLLAR_HISTORICAL_DATA = "https://www.investing.com/indices/usdollar-historical-data"

DOLLAR_HEADERS = {
    "Referer": DOLLAR_HISTORICAL_DATA,
}

DOLLAR_POST_DATA = "curr_id=942611&smlID=2067751&header=US+Dollar+Index+Historical+Data&st_date=01%2F01%2F2020&end_date=12%2F31%2F2020&interval_sec=Daily&sort_col=date&sort_ord=DESC&action=historical_data"

DOLLAR_OUTPUT_FILE = "usdollar.csv"
DOLLAR_OUTPUT_PATH = os.path.join(OUTPUT_PATH, DOLLAR_OUTPUT_FILE)
##########################


######### BONDS ##########
BONDS_HISTORICAL_DATA = (
    "https://www.investing.com/etfs/db-x-trackers-ii-global-sovereign-5-historical-data"
)

BONDS_HEADERS = {
    "Referer": BONDS_HISTORICAL_DATA,
}

BONDS_POST_DATA = "curr_id=949510&smlID=2569824&header=XG7S+Historical+Data&st_date=01%2F01%2F2020&end_date=12%2F31%2F2020&interval_sec=Daily&sort_col=date&sort_ord=DESC&action=historical_data"

BONDS_OUTPUT_FILE = "db-x-trackers-ii-global-sovereign-5.csv"
BONDS_OUTPUT_PATH = os.path.join(OUTPUT_PATH, BONDS_OUTPUT_FILE)
##########################
import os
from enum import Enum

CSV_PATH = os.path.join("..", "scraper_part", "scraped_csvs")

DATE_FORMAT = "%b %d, %Y"

AssetData = {
    "ST": os.path.join(CSV_PATH, "amundi-msci-wrld-ae-c.csv"),
    "CB": os.path.join(CSV_PATH, "ishares-global-corporate-bond-$.csv"),
    "PB": os.path.join(CSV_PATH, "db-x-trackers-ii-global-sovereign-5.csv"),
    "GO": os.path.join(CSV_PATH, "spdr-gold-trust.csv"),
    "CA": os.path.join(CSV_PATH, "usdollar.csv"),
}

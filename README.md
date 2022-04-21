# Programming-for-data-science-project
This is a repository containing source code for the final project of the programming for data science course held at UPM semester 2021/2022  

The goal is to design a back testing tool for a fictional investment firm. The first part of the project scrapes the investing.com website and generates a CSV file with historical data on the price movements of a ticker.


## Running code

### First part

For the scraping part it is required to have the python package BeautifulSoup installed

```
pip3 install bs4
```

You can run the scraper part of the task from the scraper_part directory.

```
python3 scraper.py
```

This should create the scraped CSV files in the scraped_csvs directory.

### Second part

For the portfolio part no aditional dependencies are required apart from standard python packages. From the portfolio_part directory run the script as following

```
python3 main.py
```

This should create two CSV files. First one is portfolio_allocations.csv which contains the 127 portfolios as described in the task description.

  The second CSV file is called portfolio_metrics.csv which enriches the first CSV file with two additional columns RETURN and VOLAT corresponding to the return and volatility of a given porfolio allocation.
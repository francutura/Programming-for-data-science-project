# Programming-for-data-science-project
This is a repository containing source code for the final project of the programming for data science course held at UPM semester 2021/2022

The goal is to design a back testing tool for a fictional investment firm. The first part of the project scrapes the investing.com website and generates a CSV file with historical data on the price movements of a ticker.


## Running code

### First part

For the scraping part it is required to have the python package BeautifulSoup installed

```
pip3 install bs4
```

You can run the scraper part of the task using.

```
python3 scraper_part/scraper.py
```

This should create the scraped CSV files in the scraper_part directory.

### Second part

For the portfolio generation part no additional dependencies are required apart from standard python packages. Please run the script as following

```
python3 portfolio_part/main.py
```

This should create a CSV file portfolio_allocations.csv which contains the 127 portfolios as described in the task description.

### Data analysis

For running the data analysis it is needed some libraries that will be included in the (matplotlib, pandas, numpy, seaborn, and scipy).  Please run the script as following

```
python3 portfolio_part/portofolio_analysis.py
```
This script will create the metrics, plots(saved under plots directory), statistics, and a CSV file called portfolio_metrics.csv which enriches the first CSV file with two additional columns RETURN and VOLAT corresponding to the return and volatility of a given portfolio allocation.

## Requirement

All the required libraries are in the requirements.txt file that can be run using

```
pip install -r requirements.txt
```





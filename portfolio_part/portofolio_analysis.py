import statistics

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as st
import seaborn as sns
from numpy import average
from scipy.stats import pearsonr

from constants import AssetData, PORTFOLIO_ALLOCATIONS_PATH, PORTFOLIO_METRICS_PATH


def _return(row):
    """
    Compute the portfolio return using (current_value - buy_amount) * 100 / buy_amount
    param:
        Pandas row representing a portofolio (weights for each assets)
    Returns:
        The float representing the portfolio return
    """
    buy, current = [], []
    for asset in AssetData.keys():
        buy_price = df.query("Date == '2020-01-01'")[f"{asset}_price"].values
        current_price = df.query("Date == '2020-12-31'")[f"{asset}_price"].values
        buy.extend(row[asset] * buy_price)
        current.extend(row[asset] * current_price)
    buy_amount = sum(buy)
    current_value = sum(current)
    portfolio_return = (current_value - buy_amount) * 100 / buy_amount
    return portfolio_return


def _volatility(row):
    """
    Compute the Volatility
    param:
        Pandas row representing a portofolio (weights for each assets)
    Returns:
        The float representing the portfolio return
    """
    daily, values = [], []
    for _, ro in df.iterrows():
        for asset in AssetData.keys():
            price = ro[f"{asset}_price"]
            daily.append(row[asset] * price * 0.01)
        values.append(sum(daily))
    volatility = statistics.stdev(values) * 100 / average(values)
    return volatility


if __name__ == "__main__":

    portfolios_df = pd.read_csv(PORTFOLIO_ALLOCATIONS_PATH)
    st_df = pd.read_csv(AssetData["ST"])
    cb_df = pd.read_csv(AssetData["CB"])
    pb_df = pd.read_csv(AssetData["PB"])
    go_df = pd.read_csv(AssetData["GO"])
    ca_df = pd.read_csv(AssetData["CA"])

    dfs = [df.set_index(["Date"]) for df in [st_df, cb_df, pb_df, go_df, ca_df]]
    df = pd.concat(dfs, axis=1).reset_index()
    df["Date"] = pd.to_datetime(df["Date"])
    df.columns = ["Date", "ST_price", "CB_price", "PB_price", "GO_price", "CA_price"]
    df.sort_values(by="Date", inplace=True)
    df = df.reset_index(drop=True)

    # Some data is missing, we decided to interpolate, and extrapolate the first missing value
    cols = [col for col in df.columns if col != "Date"]
    for col in cols:
        df[col] = df[col].interpolate()
        df[col] = df[col].bfill()

    # Calculating return and volatility
    portfolio_return = portfolios_df.apply(_return, axis=1)
    portfolio_volatility = portfolios_df.apply(_volatility, axis=1)
    portfolios_df["RETURN"] = portfolio_return
    portfolios_df["VOLAT"] = portfolio_volatility
    # save the metrics
    portfolios_df.to_csv(PORTFOLIO_METRICS_PATH)

    # Plotting
    # Use seaborn style defaults and set the default figure size
    sns.set(rc={"figure.figsize": (15, 4)})

    # Taking into account ALL generated returns, does your team think it is more probable
    # to obtain a positive or negative return?
    sns.displot(portfolios_df, x="RETURN", binwidth=2, color="r")
    # calculating return confidence interval
    return_95confidence = st.t.interval(
        alpha=0.95,
        df=len(portfolios_df["RETURN"]) - 1,
        loc=np.mean(portfolios_df["RETURN"]),
        scale=st.sem(portfolios_df["RETURN"]),
    )
    return_95confidence = [np.round(conf, decimals=2) for conf in return_95confidence]
    print("\n")
    print(f"Portfolios return 95% confidence interval is {return_95confidence}\n")

    # Does your team think it is ALWAYS true that the higher the risk, the higher the obtained return is?
    fig1, ax1 = plt.subplots()
    sns.regplot(
        data=portfolios_df, x="VOLAT", y="RETURN", line_kws={"color": "red"}, ax=ax1
    )
    corr = pearsonr(portfolios_df.RETURN, portfolios_df.VOLAT)
    print(
        f"The correlation coefficient between portfolio return and volatility is {round(corr[0], 2)}\n"
    )
    # compare volatility and Return
    fig, ax = plt.subplots()
    plot_1 = ax.plot(
        portfolios_df["RETURN"],
        marker=".",
        linestyle="-",
        linewidth=1,
        label="Return",
        color="b",
    )
    ax.tick_params(axis="y", labelcolor="b")
    ax.set_ylabel("Return", color="b")

    ax2 = ax.twinx()
    plot_2 = ax2.plot(
        portfolios_df["VOLAT"],
        marker=".",
        linestyle="-",
        label="volatility",
        color="r",
        linewidth=1,
    )
    ax2.tick_params(axis="y", labelcolor="r")
    ax2.set_ylabel("Volatility", color="r")
    lns = plot_1 + plot_2
    labels = [l.get_label() for l in lns]
    plt.legend(lns, labels, loc=0)
    plt.show()


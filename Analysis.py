import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import datetime as dt
import pandas_datareader as pdr


def ts_timeperiod(company, start_date, end_date):
    start = dt.datetime.strptime(start_date, '%Y-%m-%d')
    end = dt.datetime.strptime(end_date, '%Y-%m-%d')
    df = pdr.get_data_yahoo(company, start=start, end=end)
    df.to_csv(company + '.csv')
    return df


def ts_statistics(df):
    col_names = df.columns.tolist()
    col_name = input(f"Enter column name to calculate statistics ({', '.join(col_names)}): ")
    selected_cols = [col_name]
    while True:
        add_cols = input("Do you want to calculate statistics for additional columns (Y/N)? ")
        if add_cols.lower() == 'y':
            col_name = input(f"Enter column name ({', '.join(col_names)}): ")
            selected_cols.append(col_name)
        else:
            break
    print(f"Calculating statistics for {', '.join(selected_cols)}...")
    for col_name in selected_cols:
        col = df[col_name]
        print(f"Statistics for {col_name}:")
        print(f"Minimum: {np.min(col)}")
        print(f"Maximum: {np.max(col)}")
        print(f"Mean: {np.mean(col)}")
        print(f"Standard Deviation: {np.std(col)}")
        print(f"Variance: {np.var(col)}")


def ts_plot(df, column):
    plt.plot(df['Date'], df[column])
    plt.title(f"{column} over time")
    plt.xlabel("Date")
    plt.ylabel(column)
    plt.show()


def select_ticker():
    print("Select a stock ticker:")
    ticker_list = ["MMM", "ADBE", "AAPL", "AMZN", "AMD", "AMAT", "T", "CAT", "HPE", "IBM", "MSFT"]
    print("Available tickers:", *ticker_list, sep=', ')
    ticker = input("Enter a ticker symbol from the above list: ").upper()
    while ticker not in ticker_list:
        ticker = input("Invalid ticker symbol. Enter a symbol from the list: ").upper()
    return ticker


if __name__ == "__main__":
    ticker = select_ticker()
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")

    period1 = int(time.mktime(dt.datetime.strptime(start_date, '%Y-%m-%d').timetuple()))
    period2 = int(time.mktime(dt.datetime.strptime(end_date, '%Y-%m-%d').timetuple()))

    interval = '1d'
    query_string = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'
    stock = pd.read_csv(query_string)
    stock.to_csv(f"{ticker}.csv")

    ts_statistics(stock)
    column = input("Enter a column to plot: ")
    ts_plot(stock, column)

import datetime
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np


def ts_statistics(df):
    col_names = df.columns.tolist()
    col_name = input(f"Enter a column to calculate statistics for: {', '.join(col_names)}: ")
    selected_cols = [col_name]
    while True:
        add_cols = input("Do you want to calculate statistics for another column? (Y/N): ")
        if add_cols.lower() == 'y':
            col_name = input(f"Enter a column to calculate statistics for: {', '.join(col_names)}: ")
            selected_cols.append(col_name)
        else:
            break
    print("Statistics for stock prices:")
    print(f"Stock price time series (columns): {', '.join(col_names)}")
    for col_name in selected_cols:
        col = df[col_name]
        print(f"Column: {col_name}")
        print(f"Min = {np.min(col):.4f}")
        print(f"Max = {np.max(col):.4f}")
        print(f"Mean = {np.mean(col):.4f}")
        print(f"Standard Deviation = {np.std(col):.4f}")
        print(f"Variance = {np.var(col):.4f}")


def ts_plot(df):
    col_names = df.columns.tolist()
    col_name = input(f"Enter a column to plot: {', '.join(col_names)}: ")
    plt.plot(df.index, df[col_name])
    plt.title(f"{col_name} over time")
    plt.show()


def ts_timeperiod(ticker):
    global start_date, end_date
    while True:
        start_date_str = input("Enter the start date (dd/mm/yyyy): ")
        end_date_str = input("Enter the end date (dd/mm/yyyy): ")
        try:
            start_date = datetime.datetime.strptime(start_date_str, "%d/%m/%Y").date()
            end_date = datetime.datetime.strptime(end_date_str, "%d/%m/%Y").date()
        except ValueError:
            print("Invalid date format. Please try again.")
            continue
        if start_date > end_date:
            print("Start date cannot be later than end date. Please try again.")
            continue
        if end_date > datetime.date.today():
            print("End date cannot be later than today's date. Please try again.")
            continue
        break
    stock1 = yf.download(ticker, start=start_date, end=end_date)
    return stock1


if __name__ == "__main__":
    ticker = select_ticker()
    stock = ts_timeperiod()
    ts_statistics(stock)
    ts_plot(stock)

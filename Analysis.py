import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf


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
    plt.plot(df.index, df[column])
    plt.title(f"{column} over time")
    plt.xlabel("Date")
    plt.ylabel(column)
    plt.show()


if __name__ == "__main__":
    ticker = "AAPL"  # Replace with your desired ticker symbol
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")

    stock = yf.download(ticker, start=start_date, end=end_date)

    ts_statistics(stock)
    column = input("Enter a column to plot: ")
    ts_plot(stock, column)


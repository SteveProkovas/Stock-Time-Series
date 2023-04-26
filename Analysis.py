import pandas
import matplotlib.pyplot as plt
import time
import datetime
from datetime import date


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


def ts_plot(df):
    plt.plot(df['date'], df[column])
    plt.title(f"{column} over time")
    plt.xlabel("Date")
    plt.ylabel(column)
    plt.show()


# Βοηθητικές συναρτήσεις για εισόδους επιλογών - δίνονται έτοιμες
def select_ticker():
    """Επιλογή μετοχής"""
    print("Επιλογή εταιρικής μετοχής")
    ticker_list = ["MMM", "ADBE", "AAPL", "AMZN", "AMD", "AMAT", "T", "CAT", "HPE", "IBM",
                   "MSFT"]  # λίστα με τα ticker (συντομογραφίες ονομάτων μετοχών) εταιριών του Χρημ. της Νέας Υόρκης
    print("Tickers εταιριών:", *ticker_list, sep=', ')
    ticker = input("Εισάγετε ένα από τα παραπάνω ticker μετοχής: ").upper()
    while ticker not in ticker_list:
        ticker = input("Λάθος Ticker. Εισάγετε ένα από τα παραπάνω: ").upper()
    return ticker


def select_ts(df):
    """Επιλογή χρονοσειράς/στήλης από dataframe"""
    col_list = list(df.columns)
    print("Xρονοσειρές της μετοχής (στήλες δεδομένων)", *col_list[1:], sep=', ')
    df_col = input("Εισάγετε χρονοσειρά (στήλη δεδομένων) από τις παραπάνω): ").capitalize()
    while df_col not in col_list:
        df_col = input("Λάθος χρονοσειρά/στήλη! Εισάγετε μία από τις παραπάνω: ").capitalize()
    return df_col


def confirm_continuation(msg):
    cont = input(msg + "(Y/N): ")
    while cont not in ["Y", "y", "N", "n"]:
        cont = input("Εισάγετε (Y)es ή (N)o: ")
    return True if cont.upper() == "Y" else False


if __name__ == "__main__":
    ticker = select_ticker()
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    period1 = int(time.mktime(start_date.timetuple()))
    period2 = int(time.mktime(end_date.timetuple()))
    interval = '1d'
    query_string = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'
    stock = pd.read_csv(query_string)
    stock.to_csv(f"{ticker}.csv")
    stock = ts_timeperiod(ticker, start_date, end_date)
    ts_statistics(stock)
    ts_plot(stock)
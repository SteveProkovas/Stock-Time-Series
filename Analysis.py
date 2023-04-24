# Σκοπός του παρόντος προγράμματος είναι η φόρτωση τιμών μετοχών (ανά ημέρα) από το yahoo finance (
# https://finance.yahoo.com/), και στη συνέχεια ο υπολογισμός κάποιων βασικών στατιστικών μεγεθών και η σχεδίαση της
# γραφικής παράστασης τιμών μεγεθών της συγκεκριμένης μετοχής που θα φορτώνεται κάθε φορά.

# Εισαγωγή χρήσιμων (modules) της python
import pandas
import matplotlib.pyplot as plt
import time
import datetime
from datetime import date


# Εισαγωγή χρονικής περιόδου για την οποία θα φορτωθούν τα δεδομένα
def ts_timeperiod():
    """Εισαγωγή χρονικής περιόδου για την οποία θα φορτωθούν τα δεδομένα. Επιστρέφει πλειάδα από δύο ημερομηνίες,
    της μορφής (τελική, αρχική)."""

    # Υποερώτημα 1: Εδώ μπαίνει η απάντηση για το υποερώτημα 1.

    return end_date, start_date


# Στατιστικά μέτρα τιμών μετοχής
def ts_statistics(df):  # df pandas data frame
    """Στατιστικά μέτρα τιμών μετοχής"""
    print("\nΣτατιστικά μέτρα τιμών μετοχής")
    stat = True
    while stat:
        # Επιλογή χρονοσειράς/στήλης
        df_col = select_ts(df)
        # Υποερώτημα 2: εδώ μπαίνει η απάντηση για το υποερώτημα 2

        # Ερώτημα για συνέχιση
        stat = confirm_continuation("Θέλετε να υπολογίσετε Στατιστικά Μέτρα και για άλλη Τιμή (Στήλη)?")


# Γραφική παράσταση τιμών μετοχής
def ts_plot(df):  # df pandas data frame
    """Γραφική παράσταση τιμών μετοχής"""
    print("\nΓραφική παράσταση τιμών μετοχής")
    plt_flag = True
    while plt_flag:
        # Επιλογή στήλης
        df_col = select_ts(df)
        # Υποερώτημα 3: εδώ μπαίνει η απάντηση για το υποερώτημα 3

        # Ερώτημα για συνέχιση
        plt_flag = confirm_continuation("Θέλετε να σχεδιάσετε και άλλη Τιμή (Στήλη)?")


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
    """Λήψη απάντησης για συνέχιση ή όχι"""
    cont = input(msg + "(Y/N): ")
    while cont not in ["Y", "y", "N", "n"]:
        cont = input("Εισάγετε (Y)es ή (N)o: ")
    return True if cont.upper() == "Y" else False


# Κυρίως πρόγραμμα
if __name__ == "__main__":
    # Επιλογή μετοχής (ticker)
    ticker = select_ticker()
    # Εισαγωγή/μετατροπή ημερομηνιών έναρξης/λήξης για τα δεδομένα μετοχής   
    end_date, start_date = ts_timeperiod()
    period1 = int(time.mktime(start_date.timetuple()))
    period2 = int(time.mktime(end_date.timetuple()))
    # Φόρτωση χρονομετρών μετοχής από το Yahoo Finance
    interval = '1d'  # 1d (one Day). Θα μπορούσαμε να χρησιμοποιήσουμε και 1m (one Month)
    query_string = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'
    stock = pd.read_csv(query_string)  # φορτώνει τη χρονοσειρά των τιμών των μετοχών σαν data frame
    # Αποθήκευση των τιμών της μετοχής, τοπικά, σε αρχείο τύπου csv
    stock.to_csv(f"{ticker}.csv")
    # Εμφάνιση στατιστικών
    ts_statistics(stock)
    # Εμφάνιση γραφικών παραστάσεων
    ts_plot(stock)

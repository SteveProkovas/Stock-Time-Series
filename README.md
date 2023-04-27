# Stock-Time-Series
Stock Time Series created in python 

This software is designed to retrieve stock data from Yahoo Finance, perform statistical analysis on the data, and visualize the stock's performance over time. It utilizes the 'pandas' library for data manipulation and analysis, 'matplotlib' for data visualization, and 'pandas_datareader' to fetch the stock data from Yahoo Finance.

Here's a step-by-step guide on how to use the software:

    Running the program: Run the program using a Python interpreter or an integrated development environment (IDE) that supports Python.

    Selecting a stock: The program will prompt you to select a stock by entering its ticker symbol. You can choose from the provided list of ticker symbols (MMM, ADBE, AAPL, etc.). Enter the ticker symbol exactly as shown, in uppercase.

    Entering the time period: After selecting the stock, you will be prompted to enter the start and end dates for the desired time period of the stock data. Enter the dates in the format 'YYYY-MM-DD'.

    Data retrieval and analysis: The program will retrieve the stock data from Yahoo Finance using the 'pandas_datareader' module. It will then calculate statistics for the selected columns in the data. You will be prompted to enter the column name(s) for which you want to calculate statistics. Enter the column name(s) exactly as shown in the available columns.

    Displaying statistics: The program will display the calculated statistics for each selected column, including minimum, maximum, mean, standard deviation, and variance.

    Plotting the data: After displaying the statistics, you will be prompted to enter the column name for which you want to plot the data. Enter the column name exactly as shown. The program will then plot the selected column's values over time using 'matplotlib'.

    Analyzing the plot: Once the plot is displayed, you can analyze the stock's performance over time based on the selected column.

That's it! You can repeat the process to analyze different stocks or time periods as needed. The software provides a convenient way to retrieve stock data, calculate statistics, and visualize the data for analysis.

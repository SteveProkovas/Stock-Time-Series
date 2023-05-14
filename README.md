# Stock-Time-Series
we first retrieve daily stock data for Apple Inc. (AAPL) from Alpha Vantage's API using the requests library. We then convert the JSON data into a Pandas dataframe and create a PDF document using ReportLab's canvas module. We add a title to the document and a line chart based on the closing stock price using ReportLab's LinePlot module. Finally, we save the PDF document to a file named "stock_data.pdf".

Note that you will need to replace "YOUR_API_KEY" with your actual Alpha Vantage API key in the code snippet above.

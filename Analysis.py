import requests
import pandas as pd
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.shapes import Drawing, String

# Step 1: Retrieve stock data from Alpha Vantage API
url = "https://www.alphavantage.co/query"
params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "AAPL",
    "outputsize": "compact",
    "apikey": "YOUR_API_KEY"
}
response = requests.get(url, params=params)
data = response.json()

# Convert JSON data into a Pandas dataframe
df = pd.DataFrame.from_dict(data['Time Series (Daily)'], orient='index')
df = df.astype(float)

# Step 3: Create a PDF document with a line chart based on the stock data
pdf = canvas.Canvas("stock_data.pdf", pagesize=letter)

# Add a title to the PDF document
pdf.drawString(0.5 * inch, 10 * inch, "Apple Inc. Stock Data")

# Add a line chart to the PDF document using ReportLab's LinePlot module
drawing = Drawing(400, 200)
data = [(i, v) for i, v in enumerate(df['4. close'])]
lp = LinePlot()
lp.x = 50
lp.y = 50
lp.height = 125
lp.width = 300
lp.data = [data]
lp.lines[0].strokeColor = colors.blue
lp.lines[0].strokeWidth = 2
drawing.add(lp)
pdf.draw(drawing)

# Step 4: Save the PDF document
pdf.save()

import yfinance as yf

# Step 1: Fetch stock data using yfinance
stock = yf.Ticker("RELIANCE.NS")

# Fetch the historical data for 1 month
hist = stock.history(period="1mo")

# Convert the relevant columns to a string format for analysis
# You can use .to_string() directly to include more rows if needed.
# Here, we'll keep the last 30 days of data, which corresponds to about 1 month.
stock_data = hist[['Close', 'Volume']].to_string()
print(stock_data)
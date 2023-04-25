import yfinance as yf

# Define the stock symbol you want to access data for
stock_symbol = "AAPL"

# Define the timeframe for the data
start_date = "2023-01-01"
end_date = "2023-04-24"

# Access the data using the Yahoo Finance API
stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

# Print the data
print(stock_data)

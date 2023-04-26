import yfinance as yf
import pandas as pd
import time

stocks = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'FB', 'NVDA', 'SPY', 'VOO']

# Define the function to pick stocks based on fundamental and technical indicators
def pick_stocks(stocks):
    results = []
    for stock in stocks:
        try:
            # Retrieve historical stock data
            data = yf.download(stock, period='1y')
            if len(data) == 0:
                print(f"stock {stock} not found")
                continue

            # Perform technical analysis using moving averages and relative strength index (RSI),
            # and then evaluates each stock based on its forward price-to-earnings (P/E) ratio,
            # which is a fundamental indicator of a stock's valuation.
            ma_50 = data['Close'].rolling(window=50).mean()
            ma_200 = data['Close'].rolling(window=200).mean()

            # RSI stands for Relative Strength Index. It is a technical indicator that measures the strength of a 
            # stock's price action by comparing the magnitude of its recent gains to the magnitude of its recent losses.
            # The RSI is calculated based on the average gain and loss of a stock over a specified time period. 
            # The most common time period used is 14 days, but it can be adjusted to fit the investor's preference.
            # The RSI oscillates between 0 and 100, with values above 70 indicating that a stock is overbought 
            # (i.e., it has risen too much too quickly and may be due for a price correction), 
            # while values below 30 indicate that a stock is oversold 
            # (i.e., it has fallen too much too quickly and may be due for a price rebound).
            # Traders and investors often use RSI as a signal for buying or selling a stock. 
            # For example, if a stock's RSI is above 70, some traders might interpret it as a signal to sell the stock 
            # because it is overbought and likely to decline in price. 
            # Conversely, if a stock's RSI is below 30, some traders might interpret it as a signal to buy the stock because it is oversold and likely to rebound in price.
            rsi = 100 - (100 / (1 + (data['Close'].diff().fillna(0).apply(lambda x: max(x, 0)).rolling(window=14).mean() / data['Close'].diff().fillna(0).apply(lambda x: abs(x)).rolling(window=14).mean())))

            # Retrieve financial data using yfinance
            financials = yf.Ticker(stock).info
            forward_pe = financials['forwardPE']

            # Evaluate the stock based on fundamental and technical indicators
            if ma_50[-1] > ma_200[-1] and rsi[-1] > 50 and rsi[-1] < 80 and forward_pe < 80:
                results.append(stock)
            else:
                print(f"stock: {stock}, ma_50: {ma_50[-1]}, ma_200: {ma_50[-1]}, rsi: {rsi[-1]}, forward_pe: {forward_pe}")
        except:
            print(f"stock {stock} data format has problem")

        # Pause for a second to avoid getting blocked by Yahoo Finance
        time.sleep(1)

    return results

results = pick_stocks(stocks)
print("Stocks to buy:", results)

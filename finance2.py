import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd  # Import pandas

def calculate_daily_volatility(prices):
    returns = np.log(prices / prices.shift(1))
    daily_volatility = returns.dropna().std() * np.sqrt(252)  # Calculate daily volatility for each day
    return daily_volatility

# Symbol of the action to retrieve
symbol = "AAPL"

# Retrieve historical data of the action
start_date = "2024-03-05"
end_date = "2024-05-05"
data = yf.download(symbol, start=start_date, end=end_date)

# Extract closing prices
closing_prices = data["Close"]

# Calculate daily volatility
daily_volatility = calculate_daily_volatility(closing_prices)

# Display the results
print(f"Daily Volatility of {symbol}:")
print(daily_volatility)

def calculate_daily_volatility2(returns):
    daily_volatility = returns.dropna().std() * np.sqrt(252)  # Calculate daily volatility for each day
    return daily_volatility

# Symbol of the stock to retrieve
symbol = "AAPL"
data = yf.download(symbol, start="2022-01-01", end=datetime.now().strftime('%Y-%m-%d'))

# Ensure closing prices are in a column named 'Close'
closing_prices = data['Close']

# Calculate daily returns with a small adjustment to avoid division by zero
data['Daily_Returns'] = np.log(closing_prices / closing_prices.shift(1))
data['Daily_Returns'].dropna(inplace=True)  # Drop NA values caused by the first row

# Calculate daily volatility based on daily returns
data['Daily_Volatility'] = calculate_daily_volatility2(data['Daily_Returns'])

# Create a figure with two subplots: one for closing prices and one for daily returns
fig, axs = plt.subplots(2, figsize=(10, 8))

# Plot closing prices on the top subplot
axs[0].plot(closing_prices.index, closing_prices, label='Closing Prices')
axs[0].set_title(f'Closing Prices of {symbol} from January 2022 to today')
axs[0].set_xlabel('Date')
axs[0].set_ylabel('Price ($)')
axs[0].legend()
axs[0].grid(True)


# Plot daily volatility on the bottom subplot

axs[1].plot(data.index, data['Daily_Volatility'], label=f'{symbol} Daily Volatility', linestyle='--', color='orange')
axs[1].set_title(f'{symbol} Closing Prices and Daily Volatility from 2022 to today')
axs[1].set_xlabel('Date')
axs[1].set_ylabel('Price ($) & Volatility')
axs[1].legend()
axs[1].grid(True)

# Adjust layout to fit subplots nicely
plt.tight_layout()

# Show the figure with both subplots
plt.show()
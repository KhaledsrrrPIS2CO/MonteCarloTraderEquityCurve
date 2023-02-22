import yfinance as yf
import numpy as np
import pandas as pd
from scipy.stats import norm


def get_implied_volatility(ticker, expiration, option_type, strike):
    # Download option data from Yahoo Finance
    option = yf.Ticker(ticker)
    data = option.option_chain(expiration)
    df = data.calls if option_type == 'call' else data.puts

    # Filter for the specified strike price
    df = df[df.strike == strike]

    # Calculate the implied volatility using the Black-Scholes model
    S = option.info['regularMarketPrice']
    r = 0.01  # Risk-free rate
    T = (pd.to_datetime(expiration) - pd.Timestamp.today()).days / 365
    K = strike
    option_price = df.lastPrice.iloc[0]
    option = np.log(S / K) + (r + 0.5 * np.power(df.impliedVolatility.iloc[0], 2)) * T
    d1 = option / (df.impliedVolatility.iloc[0] * np.sqrt(T))
    d2 = d1 - df.impliedVolatility.iloc[0] * np.sqrt(T)
    implied_volatility = df.impliedVolatility.iloc[0] if option_type == 'call' else -df.impliedVolatility.iloc[0]

    return implied_volatility


def get_historical_volatility(ticker, lookback_period):
    # Download historical price data from Yahoo Finance
    stock = yf.Ticker(ticker)
    hist_data = stock.history(period=lookback_period)

    # Calculate daily returns
    daily_returns = hist_data['Close'].pct_change().dropna()

    # Calculate the historical volatility
    historical_volatility = daily_returns.std() * np.sqrt(252)

    return historical_volatility


def is_option_cheap(ticker, expiration, option_type, strike, lookback_period):
    # Calculate implied and historical volatility
    implied_volatility = get_implied_volatility(ticker, expiration, option_type, strike)
    historical_volatility = get_historical_volatility(ticker, lookback_period)

    # Determine if option is cheap or expensive
    if implied_volatility > historical_volatility:
        return 'Option is expensive'
    elif implied_volatility < historical_volatility:
        return 'Option is cheap'
    else:
        return 'Option is fairly priced'


# Example usage
ticker = 'AAPL'
expiration = '2023-03-17'
option_type = 'call'
strike = 150
lookback_period = '1y'

result = is_option_cheap(ticker, expiration, option_type, strike, lookback_period)
print(result)

exit()
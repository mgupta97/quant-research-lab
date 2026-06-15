import yfinance as yf
import pandas as pd
import numpy as np

ticker = "AAPL"

data = yf.download(
    ticker,
    period="1y",
    auto_adjust=True,
)

data["log_return"] = np.log(
    data["Close"] / data["Close"].shift(1)
)

daily_vol = data["log_return"].std()

annualized_vol = daily_vol * np.sqrt(252)

print(
    f"{ticker} Historical Volatility: "
    f"{annualized_vol:.2%}"
)
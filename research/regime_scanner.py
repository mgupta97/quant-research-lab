import yfinance as yf
import numpy as np
import pandas as pd


tickers = ["AAPL", "MSFT", "NVDA", "AMZN", "GOOG"]

results = []


def classify_regime(vol):
    if vol < 0.20:
        return "Low Volatility"
    elif vol < 0.35:
        return "Normal Volatility"
    else:
        return "High Volatility"


for ticker in tickers:
    data = yf.download(
        ticker,
        period="2y",
        auto_adjust=True,
        progress=False,
    )

    close = data["Close"]

    if hasattr(close, "columns"):
        close = close.iloc[:, 0]

    returns = np.log(close / close.shift(1))

    rolling_vol = returns.rolling(21).std() * np.sqrt(252)

    current_vol = rolling_vol.dropna().iloc[-1]

    regime = classify_regime(current_vol)

    results.append(
        {
            "Ticker": ticker,
            "Current Volatility": current_vol,
            "Regime": regime,
        }
    )


df = pd.DataFrame(results)

print("\n" + "=" * 70)
print("MULTI-ASSET VOLATILITY REGIME SCANNER")
print("=" * 70)

print(
    df.to_string(
        index=False,
        formatters={
            "Current Volatility": "{:.2%}".format,
        },
    )
)

print("=" * 70)
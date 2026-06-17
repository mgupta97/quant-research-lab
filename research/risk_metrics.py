import yfinance as yf
import numpy as np
import pandas as pd


ticker = "AAPL"

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

realized_vol = returns.rolling(21).std() * np.sqrt(252)
forecast_vol = realized_vol.shift(1)
iv_proxy = realized_vol.rolling(63).mean()

df = pd.DataFrame(
    {
        "Return": returns,
        "Realized Vol": realized_vol,
        "Forecast Vol": forecast_vol,
        "IV Proxy": iv_proxy,
    }
).dropna()

df["Signal"] = np.where(
    df["Forecast Vol"] > df["IV Proxy"],
    1,
    -1,
)

df["Strategy Return"] = (
    df["Signal"]
    * df["Return"].shift(-1)
)

df = df.dropna()

mean_return = (
    df["Strategy Return"]
    .mean()
)

volatility = (
    df["Strategy Return"]
    .std()
)

sharpe = (
    mean_return
    / volatility
    * np.sqrt(252)
)

equity_curve = (
    1 + df["Strategy Return"]
).cumprod()

rolling_max = (
    equity_curve
    .cummax()
)

drawdown = (
    equity_curve
    - rolling_max
) / rolling_max

max_drawdown = (
    drawdown.min()
)

print("\n" + "=" * 70)
print("RISK METRICS REPORT")
print("=" * 70)
print(f"Ticker          : {ticker}")
print(f"Sharpe Ratio    : {sharpe:.2f}")
print(f"Max Drawdown    : {max_drawdown:.2%}")
print("=" * 70)
import yfinance as yf
import numpy as np
import pandas as pd


ticker = "AAPL"

thresholds = [
    0.00,
    0.01,
    0.02,
    0.03,
    0.05,
    0.07,
    0.10,
]

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

results = []

for threshold in thresholds:
    temp = df.copy()

    temp["Spread"] = temp["Forecast Vol"] - temp["IV Proxy"]

    temp["Signal"] = np.where(
        temp["Spread"] > threshold,
        1,
        np.where(
            temp["Spread"] < -threshold,
            -1,
            0,
        ),
    )

    temp["Strategy Return"] = temp["Signal"] * temp["Return"].shift(-1)

    temp = temp.dropna()

    traded = temp[temp["Signal"] != 0]

    if len(traded) == 0:
        continue

    mean_return = traded["Strategy Return"].mean()
    volatility = traded["Strategy Return"].std()

    sharpe = mean_return / volatility * np.sqrt(252)

    equity_curve = (1 + traded["Strategy Return"]).cumprod()
    rolling_max = equity_curve.cummax()
    drawdown = (equity_curve - rolling_max) / rolling_max
    max_drawdown = drawdown.min()

    results.append(
        {
            "Threshold": threshold,
            "Trades": len(traded),
            "Sharpe": sharpe,
            "Max Drawdown": max_drawdown,
        }
    )

results_df = pd.DataFrame(results)

print("\n" + "=" * 80)
print("SHARPE OPTIMIZATION REPORT")
print("=" * 80)

print(
    results_df.to_string(
        index=False,
        formatters={
            "Threshold": "{:.2%}".format,
            "Sharpe": "{:.2f}".format,
            "Max Drawdown": "{:.2%}".format,
        },
    )
)

print("=" * 80)
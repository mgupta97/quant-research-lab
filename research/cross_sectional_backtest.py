import yfinance as yf
import numpy as np
import pandas as pd


tickers = [
    "AAPL",
    "MSFT",
    "NVDA",
    "AMZN",
    "GOOG",
]

results = []


for ticker in tickers:

    try:

        data = yf.download(
            ticker,
            period="2y",
            auto_adjust=True,
            progress=False,
        )

        close = data["Close"]

        if hasattr(close, "columns"):
            close = close.iloc[:, 0]

        returns = np.log(
            close / close.shift(1)
        )

        realized_vol = (
            returns.rolling(21).std()
            * np.sqrt(252)
        )

        forecast_vol = realized_vol.shift(1)

        iv_proxy = (
            realized_vol
            .rolling(63)
            .mean()
        )

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
            "BUY VOL",
            "SELL VOL",
        )

        df["Next Day Abs Return"] = (
            df["Return"]
            .shift(-1)
            .abs()
        )

        df["Median Abs Return"] = (
            df["Next Day Abs Return"]
            .rolling(63)
            .median()
        )

        df["Correct"] = np.where(
            (
                (df["Signal"] == "BUY VOL")
                & (
                    df["Next Day Abs Return"]
                    > df["Median Abs Return"]
                )
            )
            |
            (
                (df["Signal"] == "SELL VOL")
                & (
                    df["Next Day Abs Return"]
                    <= df["Median Abs Return"]
                )
            ),
            1,
            0,
        )

        df = df.dropna()

        win_rate = df["Correct"].mean()

        results.append(
            {
                "Ticker": ticker,
                "Trades": len(df),
                "Win Rate": win_rate,
            }
        )

    except Exception as e:

        print(
            f"Failed for {ticker}: {e}"
        )


results_df = pd.DataFrame(results)

average_win_rate = (
    results_df["Win Rate"]
    .mean()
)

print("\n")
print("=" * 70)
print("CROSS-SECTIONAL VOLATILITY BACKTEST")
print("=" * 70)

print(
    results_df.to_string(
        index=False,
        formatters={
            "Win Rate": "{:.2%}".format
        },
    )
)

print("=" * 70)
print(
    f"Average Win Rate: "
    f"{average_win_rate:.2%}"
)
print("=" * 70)
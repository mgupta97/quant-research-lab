import yfinance as yf
import pandas as pd
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt

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

        stock = yf.Ticker(ticker)

        data = yf.download(
            ticker,
            period="1y",
            auto_adjust=True,
            progress=False,
        )

        data["log_return"] = np.log(
            data["Close"] / data["Close"].shift(1)
        )

        hv = (
            data["log_return"].std()
            * np.sqrt(252)
        )
        if hasattr(hv, "iloc"):
            hv = float(hv.iloc[0])
        else:
            hv = float(hv)

        expiration = stock.options[1]

        option_chain = stock.option_chain(
            expiration
        )

        calls = option_chain.calls

        current_price = float(
            data["Close"].iloc[-1].iloc[0]
        )

        calls["distance"] = abs(
            calls["strike"] - current_price
        )

        atm_call = (
            calls.sort_values("distance")
            .iloc[0]
        )

        iv = atm_call[
            "impliedVolatility"
        ]

        spread = iv - hv

        results.append(
            {
                "Ticker": ticker,
                "HV": hv,
                "IV": iv,
                "Spread": spread,
            }
        )

    except Exception as e:

        print(
            f"Failed for {ticker}"
        )
        print(type(e))
        print(e)

df = pd.DataFrame(results)

df = df.sort_values(
    "Spread",
    ascending=False,
)

print("\n")
print("=" * 70)
print("IV vs HV DASHBOARD")
print("=" * 70)

print(
    df.to_string(
        index=False,
        formatters={
            "HV": "{:.2%}".format,
            "IV": "{:.2%}".format,
            "Spread": "{:.2%}".format,
        },
    )
)

print("=" * 70)

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.bar(df["Ticker"], df["Spread"])
plt.axhline(0, linestyle="--")
plt.title("IV-HV Spread by Ticker")
plt.xlabel("Ticker")
plt.ylabel("IV - HV Spread")
plt.grid(axis="y")

output_dir = Path("research/figures")
output_dir.mkdir(parents=True, exist_ok=True)

plt.savefig(
    output_dir / "iv_hv_spread_by_ticker.png",
    dpi=300,
    bbox_inches="tight",
)

plt.show()
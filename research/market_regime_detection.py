import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


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

rolling_vol = returns.rolling(21).std() * np.sqrt(252)

df = pd.DataFrame(
    {
        "Volatility": rolling_vol,
    }
).dropna()


def classify_regime(vol):
    if vol < 0.20:
        return "Low Volatility"
    elif vol < 0.35:
        return "Normal Volatility"
    else:
        return "High Volatility"


df["Regime"] = df["Volatility"].apply(classify_regime)

regime_counts = df["Regime"].value_counts()

print("\n" + "=" * 60)
print("MARKET REGIME DETECTION REPORT")
print("=" * 60)
print(f"Ticker: {ticker}")
print("\nRegime Counts:")
print(regime_counts)
print("=" * 60)

plt.figure(figsize=(12, 6))
plt.plot(df.index, df["Volatility"])
plt.title("Market Regime Detection Using Rolling Volatility")
plt.xlabel("Date")
plt.ylabel("Annualized Volatility")
plt.grid(True)

output_dir = Path("research/figures")
output_dir.mkdir(parents=True, exist_ok=True)

plt.savefig(
    output_dir / "market_regime_detection.png",
    dpi=300,
    bbox_inches="tight",
)

plt.show()
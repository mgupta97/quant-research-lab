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

actual_volatility = returns.rolling(21).std() * np.sqrt(252)

forecast_volatility = actual_volatility.shift(1)

results = pd.DataFrame(
    {
        "Actual Volatility": actual_volatility,
        "Forecast Volatility": forecast_volatility,
    }
).dropna()

correlation = results["Actual Volatility"].corr(
    results["Forecast Volatility"]
)

print("\n" + "=" * 60)
print("VOLATILITY FORECAST REPORT")
print("=" * 60)
print(f"Ticker      : {ticker}")
print(f"Model       : 1-Day Lagged Rolling Volatility")
print(f"Correlation: {correlation:.4f}")
print("=" * 60)

plt.figure(figsize=(12, 6))
plt.plot(results.index, results["Actual Volatility"], label="Actual Volatility")
plt.plot(results.index, results["Forecast Volatility"], label="Forecast Volatility")
plt.title("Actual vs Forecasted Volatility")
plt.xlabel("Date")
plt.ylabel("Annualized Volatility")
plt.legend()
plt.grid(True)

output_dir = Path("research/figures")
output_dir.mkdir(parents=True, exist_ok=True)

plt.savefig(
    output_dir / "volatility_forecast.png",
    dpi=300,
    bbox_inches="tight",
)

plt.show()
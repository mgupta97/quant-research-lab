import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from sklearn.cluster import KMeans


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

model = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10,
)

df["Cluster"] = model.fit_predict(
    df[["Volatility"]]
)

cluster_order = (
    df.groupby("Cluster")["Volatility"]
    .mean()
    .sort_values()
    .index
)

cluster_labels = {
    cluster_order[0]: "Low Volatility",
    cluster_order[1]: "Normal Volatility",
    cluster_order[2]: "High Volatility",
}

df["Regime"] = df["Cluster"].map(cluster_labels)

print("\n" + "=" * 60)
print("ML MARKET REGIME DETECTION REPORT")
print("=" * 60)
print(f"Ticker: {ticker}")
print("\nCluster Means:")
print(df.groupby("Regime")["Volatility"].mean())
print("\nRegime Counts:")
print(df["Regime"].value_counts())
print("=" * 60)

plt.figure(figsize=(12, 6))

for regime in ["Low Volatility", "Normal Volatility", "High Volatility"]:
    subset = df[df["Regime"] == regime]
    plt.scatter(
        subset.index,
        subset["Volatility"],
        label=regime,
        s=10,
    )

plt.title("ML-Based Market Regime Detection")
plt.xlabel("Date")
plt.ylabel("Annualized Volatility")
plt.legend()
plt.grid(True)

output_dir = Path("research/figures")
output_dir.mkdir(parents=True, exist_ok=True)

plt.savefig(
    output_dir / "ml_regime_detection.png",
    dpi=300,
    bbox_inches="tight",
)

plt.show()
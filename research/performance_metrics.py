import yfinance as yf
import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score, accuracy_score


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

df["Predicted"] = np.where(
    df["Forecast Vol"] > df["IV Proxy"],
    1,
    0,
)

df["Next Day Abs Return"] = df["Return"].shift(-1).abs()
df["Median Abs Return"] = df["Next Day Abs Return"].rolling(63).median()

df["Actual"] = np.where(
    df["Next Day Abs Return"] > df["Median Abs Return"],
    1,
    0,
)

df = df.dropna()

accuracy = accuracy_score(df["Actual"], df["Predicted"])
precision = precision_score(df["Actual"], df["Predicted"])
recall = recall_score(df["Actual"], df["Predicted"])
f1 = f1_score(df["Actual"], df["Predicted"])
matrix = confusion_matrix(df["Actual"], df["Predicted"])

print("\n" + "=" * 70)
print("PERFORMANCE METRICS REPORT")
print("=" * 70)
print(f"Ticker   : {ticker}")
print(f"Trades   : {len(df)}")
print(f"Accuracy : {accuracy:.2%}")
print(f"Precision: {precision:.2%}")
print(f"Recall   : {recall:.2%}")
print(f"F1 Score : {f1:.2%}")

print("\nConfusion Matrix:")
print(matrix)
print("=" * 70)
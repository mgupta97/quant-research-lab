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

threshold = 0.10

all_returns = []
risk_scores = []

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

        df["Spread"] = df["Forecast Vol"] - df["IV Proxy"]

        df["Signal"] = np.where(
            df["Spread"] > threshold,
            1,
            np.where(df["Spread"] < -threshold, -1, 0),
        )

        df["Confidence"] = abs(df["Spread"])

        df["Position"] = df["Signal"] * df["Confidence"]

        df["Strategy Return"] = df["Position"] * df["Return"].shift(-1)

        df = df.dropna()

        recent_vol = df["Realized Vol"].iloc[-1]

        risk_score = 1 / recent_vol

        all_returns.append(
            df["Strategy Return"].reset_index(drop=True)
        )

        risk_scores.append(risk_score)

        print(f"{ticker}: {(df['Signal'] != 0).sum()} trades")

    except Exception as e:
        print(f"Failed for {ticker}: {e}")


portfolio = pd.concat(all_returns, axis=1)
portfolio.columns = tickers

weights = np.array(risk_scores)
weights = weights / weights.sum()

portfolio["Portfolio Return"] = portfolio[tickers].dot(weights)

mean_return = portfolio["Portfolio Return"].mean()
volatility = portfolio["Portfolio Return"].std()

sharpe = mean_return / volatility * np.sqrt(252)

equity_curve = (1 + portfolio["Portfolio Return"]).cumprod()
rolling_max = equity_curve.cummax()
drawdown = (equity_curve - rolling_max) / rolling_max

max_drawdown = drawdown.min()
total_return = equity_curve.iloc[-1] - 1

print("\n" + "=" * 90)
print("IMPROVED PORTFOLIO BACKTEST REPORT")
print("=" * 90)
print(f"Threshold       : {threshold:.0%}")
print(f"Weighting       : Inverse Volatility")
print(f"Position Sizing : Confidence Weighted")
print(f"Total Return    : {total_return:.2%}")
print(f"Sharpe Ratio    : {sharpe:.2f}")
print(f"Max Drawdown    : {max_drawdown:.2%}")
print("=" * 90)

print("\nPortfolio Weights:")
for ticker, weight in zip(tickers, weights):
    print(f"{ticker}: {weight:.2%}")
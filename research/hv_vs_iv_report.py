import yfinance as yf
import numpy as np


ticker = "AAPL"
assumed_iv = 0.30

data = yf.download(
    ticker,
    period="1y",
    auto_adjust=True,
    progress=False,
)

data["log_return"] = np.log(
    data["Close"] / data["Close"].shift(1)
)

historical_volatility = (
    data["log_return"].std() * np.sqrt(252)
)

spread = assumed_iv - historical_volatility

print("\n" + "=" * 50)
print("VOLATILITY ANALYSIS REPORT")
print("=" * 50)

print(f"Ticker                : {ticker}")
print(f"Historical Volatility : {historical_volatility:.2%}")
print(f"Assumed Implied Vol   : {assumed_iv:.2%}")
print(f"IV - HV Spread        : {spread:.2%}")

print("\nInterpretation:")

if spread > 0:
    print(
        "Options appear expensive relative to recent "
        "historical volatility."
    )
    print(
        "The market is pricing higher future uncertainty "
        "than what has recently occurred."
    )
elif spread < 0:
    print(
        "Options appear cheap relative to recent "
        "historical volatility."
    )
    print(
        "The market is pricing lower future uncertainty "
        "than what has recently occurred."
    )
else:
    print(
        "Implied and historical volatility are approximately equal."
    )

print("=" * 50)
import yfinance as yf
import numpy as np


ticker = "AAPL"

stock = yf.Ticker(ticker)

price_data = yf.download(
    ticker,
    period="1y",
    auto_adjust=True,
    progress=False,
)

price_data["log_return"] = np.log(
    price_data["Close"] / price_data["Close"].shift(1)
)

historical_volatility = (
    price_data["log_return"].std() * np.sqrt(252)
)

expirations = stock.options
nearest_expiration = expirations[1]

option_chain = stock.option_chain(nearest_expiration)
calls = option_chain.calls

current_price = float(price_data["Close"].iloc[-1].iloc[0])

calls["distance_from_spot"] = abs(
    calls["strike"] - current_price
)

atm_call = calls.sort_values(
    "distance_from_spot"
).iloc[0]

print("\nATM OPTION DATA")
print(atm_call)

market_iv = atm_call["impliedVolatility"]

spread = market_iv - historical_volatility

print("\n" + "=" * 50)
print("REAL-MARKET VOLATILITY ANALYSIS REPORT")
print("=" * 50)

print(f"Ticker                : {ticker}")
print(f"Current Price         : {current_price:.2f}")
print(f"Nearest Expiration    : {nearest_expiration}")
print(f"ATM Strike            : {atm_call['strike']}")
print(f"Historical Volatility : {historical_volatility:.2%}")
print(f"Market Implied Vol    : {market_iv:.2%}")
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
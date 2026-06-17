import yfinance as yf
import numpy as np
import pandas as pd
from scipy.optimize import minimize


tickers = ["AAPL", "MSFT", "NVDA", "AMZN", "GOOG"]


def classify_regime(vol):
    if vol < 0.20:
        return "Low Volatility"
    elif vol < 0.35:
        return "Normal Volatility"
    else:
        return "High Volatility"


def compute_garch_forecast(returns):
    returns = returns.dropna() * 100

    def garch_log_likelihood(params):
        omega, alpha, beta = params

        if omega <= 0 or alpha < 0 or beta < 0 or alpha + beta >= 1:
            return 1e10

        n = len(returns)
        variance = np.zeros(n)
        variance[0] = np.var(returns)

        for t in range(1, n):
            variance[t] = (
                omega
                + alpha * returns.iloc[t - 1] ** 2
                + beta * variance[t - 1]
            )

        log_likelihood = -0.5 * np.sum(
            np.log(2 * np.pi)
            + np.log(variance)
            + returns.values**2 / variance
        )

        return -log_likelihood

    result = minimize(
        garch_log_likelihood,
        [0.1, 0.05, 0.9],
        method="Nelder-Mead",
    )

    omega, alpha, beta = result.x

    n = len(returns)
    variance = np.zeros(n)
    variance[0] = np.var(returns)

    for t in range(1, n):
        variance[t] = (
            omega
            + alpha * returns.iloc[t - 1] ** 2
            + beta * variance[t - 1]
        )

    latest_vol = np.sqrt(variance[-1]) / 100 * np.sqrt(252)

    return latest_vol


results = []

for ticker in tickers:
    try:
        stock = yf.Ticker(ticker)

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

        hv = returns.rolling(21).std().dropna().iloc[-1] * np.sqrt(252)

        garch_forecast = compute_garch_forecast(returns)

        expirations = stock.options
        expiration = expirations[1]

        option_chain = stock.option_chain(expiration)
        calls = option_chain.calls

        current_price = float(close.iloc[-1])

        calls["distance"] = abs(calls["strike"] - current_price)

        atm_call = calls.sort_values("distance").iloc[0]

        iv = atm_call["impliedVolatility"]

        spread_forecast_iv = garch_forecast - iv

        regime = classify_regime(hv)

        if spread_forecast_iv > 0.03 and regime != "High Volatility":
            signal = "BUY VOLATILITY"
        elif spread_forecast_iv < -0.03:
            signal = "SELL VOLATILITY"
        else:
            signal = "NO TRADE"

        results.append(
            {
                "Ticker": ticker,
                "HV": hv,
                "IV": iv,
                "GARCH Forecast": garch_forecast,
                "Forecast-IV Spread": spread_forecast_iv,
                "Regime": regime,
                "Signal": signal,
            }
        )

    except Exception as e:
        print(f"Failed for {ticker}: {e}")


df = pd.DataFrame(results)

print("\n" + "=" * 90)
print("VOLATILITY SIGNAL ENGINE")
print("=" * 90)

print(
    df.to_string(
        index=False,
        formatters={
            "HV": "{:.2%}".format,
            "IV": "{:.2%}".format,
            "GARCH Forecast": "{:.2%}".format,
            "Forecast-IV Spread": "{:.2%}".format,
        },
    )
)

print("=" * 90)
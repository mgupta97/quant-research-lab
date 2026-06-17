# Quant Research Lab: Options Pricing, Volatility Forecasting, and Signal Validation

## Abstract

This project develops a quantitative finance research platform for options pricing, volatility modeling, regime detection, and signal validation. The system implements Black-Scholes pricing, Greeks, implied volatility estimation, Monte Carlo simulation, GARCH volatility forecasting, and cross-sectional volatility signal testing across major technology equities.

The strongest empirical result is a cross-sectional volatility signal backtest across AAPL, MSFT, NVDA, AMZN, and GOOG, achieving an average win rate of 54.66% over 356 trades per asset.

## 1. Introduction

Financial markets are characterized by uncertainty, changing volatility regimes, and rapidly evolving expectations. Quantitative models seek to measure and forecast these dynamics to support pricing, risk management, and trading decisions.

The objective of this project was to build a quantitative research platform from first principles using Python. Rather than relying on pre-built financial libraries, the project implements key concepts manually, including option pricing models, implied volatility estimation, volatility forecasting, regime detection, and signal validation.

The project follows a progressive research framework:

1. Implement theoretical pricing models.
2. Validate analytical formulas numerically.
3. Analyze real market volatility.
4. Forecast future volatility.
5. Detect market regimes.
6. Generate trading signals.
7. Evaluate signals through backtesting.

The final system combines quantitative finance, statistical modeling, machine learning, and forecasting techniques into a unified research environment.

---

## 2. Research Objectives

The project was designed to answer the following research questions:

### Option Pricing

* Can the Black-Scholes model be implemented and validated from scratch?
* Does Monte Carlo simulation converge to analytical pricing results?

### Volatility Research

* How does implied volatility vary across option strikes?
* Can historical volatility explain future market behavior?
* Does volatility exhibit clustering and persistence?

### Forecasting

* Can GARCH models provide useful volatility forecasts?
* Are volatility regimes identifiable using statistical and machine learning approaches?

### Signal Generation

* Does disagreement between forecast volatility and market expectations contain predictive information?
* Can such information be converted into a measurable trading signal?

### Validation

* Does the signal generalize across multiple assets?
* Does performance remain stable across different technology stocks?

## 3. Methodology

### 3.1 Black-Scholes Option Pricing

The Black-Scholes model was implemented from first principles to price European call and put options. The model assumes lognormally distributed asset prices, constant volatility, frictionless markets, and continuous trading.

The implementation was used as the analytical benchmark throughout the project and served as the foundation for validating numerical pricing methods.

Key outputs included:

* Call option pricing
* Put option pricing
* Delta
* Gamma
* Vega
* Theta
* Rho

Numerical validation was performed to ensure consistency between analytical and finite-difference estimates of the Greeks.

---

### 3.2 Monte Carlo Simulation

A Monte Carlo pricing engine was developed to estimate option values through simulation.

The simulation generated thousands of future stock-price paths under the geometric Brownian motion assumption. Option payoffs were calculated at maturity and discounted to present value.

The model was compared against Black-Scholes pricing.

Results showed strong convergence:

| Model         | Price   |
| ------------- | ------- |
| Black-Scholes | 10.4506 |
| Monte Carlo   | 10.4538 |

The final difference was only 0.0033, demonstrating successful implementation and convergence.

---

### 3.3 Implied Volatility Estimation

A Newton-Raphson optimization procedure was implemented to estimate implied volatility from observed option prices.

The algorithm iteratively adjusted volatility until the Black-Scholes theoretical price matched the observed market price.

The implementation enabled:

* Implied volatility estimation
* Volatility smile analysis
* Market volatility comparison

---

### 3.4 Historical Volatility Analysis

Historical volatility was calculated using log returns and annualized using the square-root-of-time rule.

Rolling volatility estimates were used throughout the project as a benchmark for:

* Volatility forecasting
* Regime detection
* Signal generation

Historical volatility served as the primary measure of realized market uncertainty.

---

### 3.5 GARCH Volatility Forecasting

A GARCH(1,1) model was implemented using maximum likelihood estimation.

The model forecasts future volatility using both recent market shocks and historical volatility persistence.

Estimated parameters for AAPL were:

| Parameter    | Value  |
| ------------ | ------ |
| Omega        | 0.1647 |
| Alpha        | 0.0879 |
| Beta         | 0.8545 |
| Alpha + Beta | 0.9424 |

The high Alpha + Beta value indicated strong volatility persistence and clustering.

---

### 3.6 Market Regime Detection

Two regime detection approaches were implemented.

#### Rule-Based Regime Detection

Volatility observations were classified into:

* Low Volatility
* Normal Volatility
* High Volatility

using predefined thresholds.

#### Machine Learning Regime Detection

K-Means clustering was applied to volatility observations.

The algorithm identified volatility regimes directly from the data rather than relying on manually selected thresholds.

Cluster analysis revealed distinct low, normal, and high-volatility market states.

---

### 3.7 Volatility Signal Generation

A signal-generation framework was constructed to identify situations where model forecasts differed from market expectations.

The framework compared:

Forecast Volatility

versus

Implied Volatility Proxy

Signals were defined as:

* BUY VOLATILITY
* SELL VOLATILITY
* NO TRADE

depending on the direction and magnitude of disagreement.

---

### 3.8 Cross-Sectional Validation

To evaluate robustness, the signal-generation framework was tested across multiple large-cap technology stocks:

* AAPL
* MSFT
* NVDA
* AMZN
* GOOG

Cross-sectional testing was performed to determine whether the observed predictive behavior generalized beyond a single asset.

This approach reduced the risk of overfitting to a specific security and provided a more realistic assessment of model performance.

## 4. Results and Findings

### 4.1 Monte Carlo Validation

The Monte Carlo pricing engine was evaluated against the analytical Black-Scholes solution.

| Metric              | Value   |
| ------------------- | ------- |
| Black-Scholes Price | 10.4506 |
| Monte Carlo Price   | 10.4538 |
| Difference          | 0.0033  |

The negligible difference demonstrates successful implementation and convergence of the simulation framework.

---

### 4.2 Volatility Forecasting

Rolling volatility forecasting produced a correlation of:

| Metric      | Value  |
| ----------- | ------ |
| Correlation | 0.9833 |

This result suggests strong persistence in volatility and supports the hypothesis that volatility exhibits clustering behavior.

Periods of high volatility tend to be followed by elevated volatility, while calm periods tend to remain calm.

---

### 4.3 GARCH Volatility Forecasting

The GARCH(1,1) model estimated:

| Parameter    | Value  |
| ------------ | ------ |
| Omega        | 0.1647 |
| Alpha        | 0.0879 |
| Beta         | 0.8545 |
| Alpha + Beta | 0.9424 |

The large Alpha + Beta value indicates substantial volatility persistence.

This finding is consistent with financial market literature and validates the use of GARCH for volatility forecasting.

---

### 4.4 Rule-Based Regime Detection

For AAPL, volatility regimes were classified as:

| Regime            | Observations |
| ----------------- | ------------ |
| Low Volatility    | 166          |
| Normal Volatility | 285          |
| High Volatility   | 30           |

Most observations occurred within the normal-volatility regime.

---

### 4.5 Machine Learning Regime Detection

K-Means clustering identified the following volatility clusters:

| Regime            | Average Volatility |
| ----------------- | ------------------ |
| Low Volatility    | 17.18%             |
| Normal Volatility | 27.27%             |
| High Volatility   | 71.87%             |

The clustering approach successfully separated extreme volatility periods from ordinary market conditions.

---

### 4.6 Cross-Sectional Signal Validation

The volatility signal framework was evaluated across five large-cap technology stocks.

| Ticker | Win Rate |
| ------ | -------- |
| AAPL   | 55.90%   |
| MSFT   | 52.81%   |
| NVDA   | 56.74%   |
| AMZN   | 53.09%   |
| GOOG   | 54.78%   |

Average performance:

| Metric           | Value  |
| ---------------- | ------ |
| Average Win Rate | 54.66% |

The consistency across multiple assets suggests that forecast-market volatility disagreement contains useful predictive information.

This represents the strongest empirical finding of the project.

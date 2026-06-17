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

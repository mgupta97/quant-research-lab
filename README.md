# Quant Research Lab

A quantitative finance research platform built from first principles to investigate option pricing, volatility forecasting, market regime detection, and decision-making under uncertainty.

## Overview

This project explores how forecasting models, statistical learning techniques, and uncertainty quantification methods can be used to generate and evaluate volatility-based signals in financial markets.

The project combines:

* Option Pricing
* Volatility Forecasting
* Machine Learning
* Market Regime Detection
* Signal Generation
* Portfolio Construction
* Risk Evaluation

The broader goal is to study predictive modeling and decision-making under uncertainty, with applications in quantitative finance, operations research, and industrial engineering.

---

## Research Questions

1. Can option pricing models be implemented and validated from scratch?
2. How accurately can volatility be estimated and forecasted?
3. Do market volatility regimes naturally emerge from historical data?
4. Does disagreement between forecast volatility and market expectations contain predictive information?
5. Can volatility-based signals generalize across multiple assets?

---

## Methodology

### Option Pricing

* Black-Scholes Pricing Model
* European Call Pricing
* European Put Pricing
* Greeks

  * Delta
  * Gamma
  * Vega

### Numerical Methods

* Monte Carlo Simulation
* Finite Difference Validation
* Newton-Raphson Implied Volatility Solver

### Volatility Modeling

* Historical Volatility
* Volatility Smile Analysis
* IV vs HV Comparison
* GARCH(1,1) Forecasting

### Regime Detection

* Rule-Based Volatility Regimes
* K-Means Clustering

### Signal Generation

* Forecast Volatility vs Market Expectations
* Cross-Sectional Validation
* Confidence-Based Signal Filtering

### Portfolio Construction

* Equal Weight Portfolio
* Inverse Volatility Weighting
* Confidence-Based Position Sizing

---

## Key Results

### Monte Carlo Validation

| Metric              | Value   |
| ------------------- | ------- |
| Black-Scholes Price | 10.4506 |
| Monte Carlo Price   | 10.4538 |
| Difference          | 0.0033  |

### Volatility Forecasting

| Metric               | Value  |
| -------------------- | ------ |
| Forecast Correlation | 0.9833 |

### Cross-Sectional Validation

| Ticker | Accuracy |
| ------ | -------- |
| AAPL   | 55.90%   |
| MSFT   | 52.81%   |
| NVDA   | 56.74%   |
| AMZN   | 53.09%   |
| GOOG   | 54.78%   |

Average Accuracy: **54.66%**

### Classification Metrics (AAPL)

| Metric    | Value  |
| --------- | ------ |
| Accuracy  | 56.18% |
| Precision | 56.11% |
| Recall    | 56.74% |
| F1 Score  | 56.42% |

### Signal Optimization

| Threshold | Sharpe | Max Drawdown |
| --------- | ------ | ------------ |
| 0%        | -0.11  | -27.36%      |
| 5%        | 0.45   | -13.31%      |
| 10%       | 0.64   | -11.66%      |

### Portfolio Optimization

| Metric       | Baseline | Optimized |
| ------------ | -------- | --------- |
| Sharpe Ratio | -0.19    | -0.10     |
| Max Drawdown | -18.83%  | -3.19%    |
| Total Return | -4.47%   | -0.44%    |

---

## Research Report

Full report available:

research/report/Quant_Research_Report.pdf

---

## Technologies

* Python
* NumPy
* Pandas
* SciPy
* Scikit-Learn
* Matplotlib
* yFinance

---

## Future Work

* Historical Options IV Data
* Hidden Markov Models
* EGARCH and GJR-GARCH
* Volatility Surface Modeling
* Portfolio Optimization Under Uncertainty
* Stochastic Optimization
* Risk-Aware Decision Frameworks

---

## Author

Mehul Gupta

Master of Business Analytics, University of Illinois Chicago

Research Interests:

* Operations Research
* Quantitative Finance
* Machine Learning
* Optimization Under Uncertainty
* Decision Analytics

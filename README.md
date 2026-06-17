# Quant Research Lab

A quantitative finance research platform built from scratch in Python.

This repository explores option pricing, risk management, implied volatility, Monte Carlo simulation, and volatility research using both theoretical models and real market data.

---

# Project Goals

* Build core quantitative finance models from scratch
* Understand option pricing theory beyond textbook formulas
* Validate analytical results using numerical methods
* Analyze real-world option market data
* Produce research-grade visualizations and reports
* Develop a portfolio-quality quant research repository

---

# Features

## Option Pricing

### Black-Scholes Pricing Model

Implemented from scratch:

* European Call Pricing
* European Put Pricing

### Monte Carlo Pricing

Implemented Monte Carlo simulation for European options and validated convergence against Black-Scholes.

---

## Greeks

Implemented analytically:

* Delta
* Gamma
* Vega
* Theta
* Rho

---

## Implied Volatility

Implemented a Newton-Raphson solver to compute implied volatility from market option prices.

Features:

* Call Option IV
* ATM Option Analysis
* Real Market Option Chains

---

# Validation Framework

Analytical formulas validated numerically.

Research scripts include:

* Delta Validation
* Gamma Validation
* Vega Validation

---

# Research Projects

## 1. Vega Strike Experiment

Research Question:

> Does Vega truly peak at-the-money?

Finding:

Vega peaked near the forward ATM strike rather than exactly at the spot price.

Generated:

* Vega vs Strike chart

---

## 2. Volatility Smile Analysis

Research Question:

> Does implied volatility remain constant across strikes?

Finding:

Higher implied volatility was observed for strikes farther from the underlying price, demonstrating a volatility smile.

Generated:

* Volatility Smile chart

---

## 3. Historical vs Implied Volatility Report

Research Question:

> Is the market pricing more or less volatility than history suggests?

Example Result:

| Metric                | Value  |
| --------------------- | ------ |
| Historical Volatility | 22.65% |
| Implied Volatility    | 18.31% |
| Spread                | -4.34% |

Interpretation:

The market was pricing lower future volatility than recent realized volatility.

---

## 4. Multi-Asset IV vs HV Dashboard

Universe:

* AAPL
* MSFT
* NVDA
* AMZN
* GOOG

Latest Results:

| Ticker | HV     | IV     | Spread |
| ------ | ------ | ------ | ------ |
| GOOG   | 28.53% | 35.19% | +6.67% |
| MSFT   | 25.76% | 29.32% | +3.56% |
| AMZN   | 30.33% | 32.01% | +1.68% |
| AAPL   | 22.65% | 22.58% | -0.06% |
| NVDA   | 35.08% | 33.84% | -1.24% |

Finding:

* GOOG options appeared most expensive relative to historical volatility.
* NVDA options appeared cheapest relative to historical volatility.

Generated:

* IV-HV Spread Ranking Chart

---

## 5. Monte Carlo Convergence Study

Research Question:

> Does Monte Carlo pricing converge to the Black-Scholes solution?

Results:

Black-Scholes:

10.4506

Monte Carlo:

10.4538

Difference:

0.0033

Finding:

Monte Carlo converges closely to the analytical Black-Scholes solution as simulation count increases.

Generated:

* Monte Carlo Convergence Chart

---

# Project Structure

```text
quant-research-lab/

src/
├── pricing/
│   ├── black_scholes.py
│   ├── implied_volatility.py
│   └── monte_carlo.py

tests/
├── test_black_scholes.py
├── test_implied_volatility.py
└── test_monte_carlo.py

research/
├── validate_gamma.py
├── validate_vega.py
├── vega_experiment.py
├── volatility_smile.py
├── hv_vs_iv_report.py
├── iv_hv_dashboard.py
├── compare_bs_vs_monte_carlo.py
├── monte_carlo_convergence.py
└── figures/
```

---

# Technologies

* Python
* NumPy
* SciPy
* Pandas
* Matplotlib
* PyTest
* yFinance

---

# Current Progress

### Quantitative Finance

* Black-Scholes Pricing
* Greeks
* Implied Volatility
* Volatility Smile Analysis
* Historical vs Implied Volatility
* Monte Carlo Pricing

### Research

* Numerical Validation
* Volatility Research
* Market Data Analysis
* Multi-Asset Screening

---

# Future Work

## Volatility Forecasting

* Rolling Volatility Models
* GARCH Models
* Volatility Regime Detection

## Derivatives Research

* Volatility Surface Construction
* Local Volatility Models
* Stochastic Volatility Models

## Quantitative Trading

* Volatility Trading Signals
* Options Strategy Backtesting
* Portfolio Risk Analytics

## Machine Learning

* Volatility Prediction
* Regime Classification
* Market State Detection

---

# Author

Mehul Gupta

Master of Business Analytics
University of Illinois Chicago

Interests:

* Quantitative Research
* Quantitative Trading
* Operations Research
* Financial Engineering
* Applied Machine Learning

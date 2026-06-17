# Quant Research Lab

A quantitative finance research platform built from first principles to explore option pricing, volatility forecasting, market regime detection, and decision-making under uncertainty.

## Project Motivation

Financial markets are complex systems characterized by uncertainty, changing volatility regimes, and evolving expectations.

This project was developed to investigate how statistical models, forecasting techniques, and machine learning methods can be combined to support decision-making under uncertainty.

The research focuses on:

* Option pricing
* Volatility modeling
* Regime detection
* Signal generation
* Cross-sectional validation

The broader objective is to study forecasting and uncertainty quantification methods relevant to quantitative finance, operations research, and industrial engineering.

---

## Research Questions

This project explores the following questions:

1. Can classical option pricing models be implemented and validated from scratch?
2. How accurately can volatility be estimated and forecasted?
3. Do volatility regimes naturally emerge in financial markets?
4. Does disagreement between model forecasts and market expectations contain predictive information?
5. Can volatility-based signals generalize across multiple assets?

---

## Methodology

### Option Pricing

* Black-Scholes Option Pricing Model
* Call and Put Pricing
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
* Implied Volatility Analysis
* Volatility Smile Visualization
* GARCH(1,1) Forecasting

### Regime Detection

* Rule-Based Volatility Regimes
* K-Means Market Regime Detection

### Signal Generation

* Forecast Volatility vs Market Expectations
* Volatility Signal Engine
* Cross-Sectional Validation Framework

---

## Project Structure

```text
quant-research-lab/
│
├── src/
│   └── pricing/
│
├── tests/
│
├── research/
│   ├── figures/
│   ├── report/
│   └── experiments/
│
├── requirements.txt
└── README.md
```

---

## Key Results

### Monte Carlo Validation

| Metric              | Value   |
| ------------------- | ------- |
| Black-Scholes Price | 10.4506 |
| Monte Carlo Price   | 10.4538 |
| Difference          | 0.0033  |

The Monte Carlo engine successfully converged to the analytical Black-Scholes solution.

---

### Volatility Forecasting

| Metric      | Value  |
| ----------- | ------ |
| Correlation | 0.9833 |

Results indicate strong volatility persistence.

---

### GARCH Forecasting

| Parameter    | Value  |
| ------------ | ------ |
| Omega        | 0.1647 |
| Alpha        | 0.0879 |
| Beta         | 0.8545 |
| Alpha + Beta | 0.9424 |

The model identified significant volatility clustering and persistence.

---

### Cross-Sectional Signal Validation

| Ticker | Win Rate |
| ------ | -------- |
| AAPL   | 55.90%   |
| MSFT   | 52.81%   |
| NVDA   | 56.74%   |
| AMZN   | 53.09%   |
| GOOG   | 54.78%   |

### Average Win Rate

**54.66%**

The signal generalized across all tested assets.

---

## Research Report

A full research report is available in:

```text
research/report/Quant_Research_Report.pdf
```

The report documents:

* Methodology
* Experiments
* Results
* Limitations
* Future Research Directions

---

## Technologies

* Python
* NumPy
* Pandas
* SciPy
* Matplotlib
* Scikit-Learn
* yFinance

---

## Future Work

Planned extensions include:

* Sharpe Ratio Analysis
* Maximum Drawdown Evaluation
* Precision / Recall Metrics
* Portfolio-Level Backtesting
* Hidden Markov Models
* Stochastic Volatility Models
* Risk-Aware Optimization Frameworks

---

## Author

Mehul Gupta

Master of Business Analytics, University of Illinois Chicago

Interested in:

* Operations Research
* Quantitative Finance
* Machine Learning
* Decision-Making Under Uncertainty

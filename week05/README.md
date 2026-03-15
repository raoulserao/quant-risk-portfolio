# Portfolio Analysis with Python

This project implements a simple **portfolio analysis framework** using historical financial data.  
It compares different portfolio allocations in terms of **return, volatility, and drawdown**, using real market data downloaded from Yahoo Finance.

The goal is to illustrate basic portfolio performance and risk metrics using Python.

---

# Overview

The script:

1. Downloads historical price data for selected assets.
2. Computes daily returns.
3. Builds different portfolio allocations.
4. Simulates portfolio value over time.
5. Computes performance and risk metrics.
6. Visualizes results with equity curves and drawdown plots.

The analysis uses daily data starting from **2010**.

---

# Assets Used

The example portfolios use the following assets:

- **SPY** — S&P 500 ETF
- **AAPL** — Apple Inc.
- **MSFT** — Microsoft Corporation

These assets represent a mix of a broad market index and large-cap technology stocks.

---

# Portfolio Allocations

Three portfolios are tested:

| Portfolio | Allocation |
|-----------|------------|
| 100_SPY | 100% SPY |
| 50_AAPL_50_MSFT | 50% AAPL, 50% MSFT |
| 40_SPY_30_AAPL_30_MSFT | 40% SPY, 30% AAPL, 30% MSFT |

---

# Performance Metrics

For each portfolio the following metrics are computed.

## Total Return
Total percentage return over the full investment period.

## Annualized Return
The **compound annual growth rate (CAGR)** implied by the total return.

## Annualized Volatility
The annualized standard deviation of daily returns:

σ_annual = σ_daily × √252

where 252 is the approximate number of trading days in a year.

## Maximum Drawdown
The largest peak-to-trough decline of the portfolio value.

Drawdown is defined as:

Drawdown = (Portfolio Value − Historical Peak) / Historical Peak

---

# Visualizations

The project generates two plots.

## Equity Curves

Shows the evolution of portfolio value over time.

Saved as:

figures/portoflio_equity_curves.png

This allows visual comparison of long-term growth across portfolios.

---

## Drawdowns

Shows the drawdown series for each portfolio.

Saved as:

figures/portfolio_drawdowns.png

This plot highlights the **risk profile** of each allocation by showing how far the portfolio falls below its previous peaks.

---

# Project Structure

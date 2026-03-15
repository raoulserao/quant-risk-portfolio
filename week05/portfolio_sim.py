import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

# Create a directory where plots will be saved
os.makedirs("figures", exist_ok=True)


def download_returns(tickers, start_date):
    """
    Download historical price data and compute daily returns.

    Parameters
    ----------
    tickers : list
        List of asset tickers.
    start_date : str
        Start date for the historical data.

    Returns
    -------
    pandas.DataFrame
        DataFrame of daily returns for each asset.
    """
    data = yf.download(tickers, start=start_date, auto_adjust=True, progress=False)

    # Handle the case where yfinance returns multi-level columns
    if isinstance(data.columns, pd.MultiIndex):
        close_prices = data["Close"]
    else:
        close_prices = data[["Close"]]
        close_prices.columns = tickers

    # Compute daily percentage returns
    returns = close_prices.pct_change().dropna()

    return returns


def compute_portfolio_returns(asset_returns, weights):
    """
    Compute portfolio returns as a weighted combination of asset returns.
    """
    return asset_returns.dot(weights)


def compute_portfolio_value(portfolio_returns, initial_capital=10000):
    """
    Compute the portfolio value over time using cumulative compounding.
    """
    return initial_capital * (1 + portfolio_returns).cumprod()


def compute_drawdown(capital):
    """
    Compute the drawdown series of a portfolio.

    Drawdown measures the percentage drop from the historical peak.
    """
    running_max = capital.cummax()
    drawdown = (capital - running_max) / running_max
    return drawdown


def compute_metrics(portfolio_returns, capital, drawdown, initial_capital=10000):
    """
    Compute key performance and risk metrics for the portfolio.
    """
    # Total return over the full period
    total_return = capital.iloc[-1] / initial_capital - 1

    # Annualized return (CAGR)
    n_days = len(portfolio_returns)
    annualized_return = (1 + total_return) ** (252 / n_days) - 1

    # Annualized volatility based on daily returns
    annualized_volatility = portfolio_returns.std() * np.sqrt(252)

    # Maximum drawdown
    max_drawdown = drawdown.min()

    return {
        "Total Return": total_return,
        "Annualized Return": annualized_return,
        "Annualized Volatility": annualized_volatility,
        "Max Drawdown": max_drawdown,
    }


def plot_equity_curves(portfolio_values):
    """
    Plot the equity curves of all portfolios.
    """
    plt.figure(figsize=(10, 6))

    for name, capital in portfolio_values.items():
        plt.plot(capital.index, capital.values, label=name)

    plt.title("Portfolio Equity Curves")
    plt.xlabel("Date")
    plt.ylabel("Portfolio Value")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("figures/equity_curves.png")
    plt.show()


def plot_drawdowns(portfolio_drawdowns):
    """
    Plot the drawdown series of all portfolios.
    """
    plt.figure(figsize=(10, 6))

    for name, drawdown in portfolio_drawdowns.items():
        plt.plot(drawdown.index, drawdown.values, label=name)

    plt.title("Portfolio Drawdowns")
    plt.xlabel("Date")
    plt.ylabel("Drawdown")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("figures/drawdowns.png")
    plt.show()


def main():
    # Assets used in the portfolio analysis
    tickers = ["SPY", "AAPL", "MSFT"]

    # Historical data start date
    start_date = "2010-01-01"

    # Initial portfolio capital
    initial_capital = 10000

    # Portfolio allocations (weights must sum to 1)
    portfolios = {
        "100_SPY": np.array([1.0, 0.0, 0.0]),
        "50_AAPL_50_MSFT": np.array([0.0, 0.5, 0.5]),
        "40_SPY_30_AAPL_30_MSFT": np.array([0.4, 0.3, 0.3]),
    }

    # Download asset returns
    asset_returns = download_returns(tickers, start_date)

    # Ensure the correct column order
    asset_returns = asset_returns[tickers]

    portfolio_values = {}
    portfolio_drawdowns = {}
    metrics_list = []

    # Compute results for each portfolio
    for portfolio_name, weights in portfolios.items():
        portfolio_returns = compute_portfolio_returns(asset_returns, weights)
        capital = compute_portfolio_value(portfolio_returns, initial_capital)
        drawdown = compute_drawdown(capital)

        metrics = compute_metrics(
            portfolio_returns=portfolio_returns,
            capital=capital,
            drawdown=drawdown,
            initial_capital=initial_capital,
        )

        portfolio_values[portfolio_name] = capital
        portfolio_drawdowns[portfolio_name] = drawdown

        metrics_list.append({
            "Portfolio": portfolio_name,
            "Total Return": metrics["Total Return"],
            "Annualized Return": metrics["Annualized Return"],
            "Annualized Volatility": metrics["Annualized Volatility"],
            "Max Drawdown": metrics["Max Drawdown"],
        })

    # Convert metrics into a DataFrame
    metrics_df = pd.DataFrame(metrics_list)

    # Express metrics in percentage terms
    metrics_df["Total Return"] = (metrics_df["Total Return"] * 100).round(2)
    metrics_df["Annualized Return"] = (metrics_df["Annualized Return"] * 100).round(2)
    metrics_df["Annualized Volatility"] = (metrics_df["Annualized Volatility"] * 100).round(2)
    metrics_df["Max Drawdown"] = (metrics_df["Max Drawdown"] * 100).round(2)

    print("\nPortfolio Metrics (%):")
    print(metrics_df.to_string(index=False))

    # Plot portfolio performance
    plot_equity_curves(portfolio_values)

    # Plot drawdown series
    plot_drawdowns(portfolio_drawdowns)


if __name__ == "__main__":
    main()

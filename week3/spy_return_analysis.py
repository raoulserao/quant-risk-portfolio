import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import os
os.makedirs("figures", exist_ok=True)



def main():
    ticker = "SPY"
    start = "2000-01-01"

    # Download adjusted prices (includes dividends and splits)
    df = yf.download(ticker, start=start, auto_adjust=True, progress=False)

    # Flatten MultiIndex columns if returned by yfinance
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    # Reset index so Date becomes a column
    df = df.reset_index()

    # Compute daily returns
    df["price"] = df["Close"]
    df["ret"] = df["price"].pct_change()
    df = df.dropna().reset_index(drop=True)

    print("Columns:", list(df.columns))
    print("Rows:", len(df))
    print("\nDaily return statistics:")
    print(df["ret"].describe())

    # Compute annual returns (end-of-year close to end-of-year close)
    annual_price = df.set_index("Date")["price"].resample("YE").last()
    annual_returns = annual_price.pct_change().dropna()
    annual_returns.index = annual_returns.index.year
    annual_returns_pct = annual_returns * 100

    # ---- Plots ----

    # Adjusted price over time
    plt.figure(figsize=(10, 5))
    plt.plot(df["Date"], df["price"])
    plt.title(f"{ticker} Adjusted Price")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.tight_layout()
    plt.savefig("figures/spy_price.png", dpi=150)
    plt.show()

    # Distribution of daily returns
    plt.figure(figsize=(10, 5))
    plt.hist(df["ret"], bins=80)
    plt.title(f"{ticker} Daily Returns Distribution")
    plt.xlabel("Return")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("figures/spy_daily_returns_hist.png", dpi=150)
    plt.show()

    # Annual returns bar chart
    plt.figure(figsize=(10, 5))
    plt.bar(annual_returns_pct.index, annual_returns_pct)
    plt.axhline(0)
    plt.title(f"{ticker} Annual Returns (%)")
    plt.xlabel("Year")
    plt.ylabel("Return (%)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("figures/spy_annual_returns.png", dpi=150)
    plt.show()


if __name__ == "__main__":
    main()

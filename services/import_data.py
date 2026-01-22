import yfinance as yf
from pathlib import Path


def download_intraday_data(
    symbol: str,
    interval: str = "5m",
    period: str = "30d",
    exchange_suffix: str = ".NS",
    output_dir: Path = Path("data/raw/2025")
):
    # Ensure output directory exists
    output_dir.mkdir(parents=True, exist_ok=True)

    # Build Yahoo symbol
    yf_symbol = f"{symbol}{exchange_suffix}"
    print(f"📥 Downloading {yf_symbol}")

    # Download data
    df = yf.download(
        yf_symbol,
        interval=interval,
        period=period,
        progress=False
    )

    if df.empty:
        raise ValueError(f"No data returned for {yf_symbol}")

    # Format dataframe
    df.reset_index(inplace=True)
    df.rename(columns={
        "Datetime": "datetime",
        "Open": "open",
        "High": "high",
        "Low": "low",
        "Close": "close",
        "Volume": "volume"
    }, inplace=True)

    # File name
    filename = f"{symbol}_{interval}_{period}.csv"
    filepath = output_dir / filename

    # Save
    df.to_csv(filepath, index=False)
    print(f"✅ Saved {filepath}")

    return filepath

# config.py

# Trading universe
SYMBOLS = [
    "TEST_STOCK"
]

# Timeframe (for historical / intraday replay)
TIMEFRAME = "5min"

# Data path
DATA_PATH = "data/raw/2025"

# Trading session timings (IST)
MARKET_START = "09:15"
MARKET_END = "15:30"

# Risk parameters (will be used later)
CAPITAL = 100000          # ₹1,00,000
RISK_PER_TRADE = 0.005    # 0.5%

STOP_LOSS_PCT = 0.005    # 0.5%
TARGET_PCT   = 0.01     # 1%

CAPITAL = 100000          # ₹1,00,000
RISK_PER_TRADE = 0.005    # 0.5% of capital
STOP_LOSS_PCT = 0.005     # 0.5%
TARGET_PCT = 0.01         # 1%

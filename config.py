# config.py
from pathlib import Path
# Trading universe
SYMBOLS = ["RELIANCE"
           # "TEST_STOCK",
   #"TEST_STOCK_2"
]

# Timeframe (for historical / intraday replay)
TIMEFRAME = "5min"

# Data path
DATA_PATH = Path("data/raw/2025")

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

# --- Execution realism ---
SLIPPAGE_PCT = 0.0005        # 0.05% per trade
BROKERAGE_PCT = 0.0003       # 0.03% per side
MAX_TRADES_PER_DAY = 3
DAILY_MAX_LOSS = 1500        # ₹

# Data download settings
HISTORICAL_PERIOD = "30d"
DATA_INTERVAL = "5m"
📈 Intraday Scanner – Dynamic Stock Analysis
Overview

This project is a Python-based intraday trading scanner designed to analyze Indian equities using VWAP-based strategies on intraday timeframes (e.g., 5-minute candles).
It supports historical backtesting, optimisation, walk-forward testing, and paper/live execution readiness with a modular and extensible architecture.

The system is built to closely resemble real-world trading engines, separating data ingestion, strategy logic, risk management, and execution layers.

Key Features

✅ Intraday VWAP indicator

✅ Rule-based BUY / SELL signal generation

✅ Position sizing & risk management

✅ Slippage & brokerage simulation

✅ Multi-stock scanning

✅ News-aware trade blocking

✅ Strategy optimisation (SL / Target tuning)

✅ Walk-forward (out-of-sample) testing

✅ Paper trading ready

🔄 Live broker integration ready (e.g. Zerodha)



How It Works (High Level)

Data Ingestion
Intraday OHLCV data is loaded from CSV or downloaded automatically using yfinance.

Indicator Calculation
VWAP is calculated and reset daily.

Signal Generation
BUY / SELL signals are produced based on price vs VWAP.

Risk & Position Management
Capital-based sizing, stop-loss, target, daily loss limits.

Execution Layer

Paper trading (default)

Live broker support via abstraction (future-ready)

Usage
Run Intraday Scanner
python main.py

Run Optimisation
python optimiser.py

Walk-Forward Test
python walk_forward.py

Configuration

All parameters are controlled from config.py, including:

Symbols

Capital

Risk per trade

Stop-loss & target %

Slippage & brokerage

Market session timings

Disclaimer ⚠️

This project is for educational and research purposes only.
It is not financial advice. Use live trading integrations at your own risk.

Future Enhancements

Zerodha Kite API live execution

More indicators (EMA, RSI, Volume Profile)

Strategy ensembles

Performance dashboards

Real-time WebSocket feeds

Author

Abhi
Python | Trading Systems | Data Analysis

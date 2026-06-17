# Institutional XAUUSD Trading Assistant

This is an institutional-grade trading copilot specializing in Gold (XAUUSD) trading, utilizing MetaTrader5, TradingView, and an LLM MCP interface.

## Architecture

* **Connectors**: MT5, TradingView, and market data cache.
* **Analysis**: Market structure, trends, liquidity, volume profile, multi-timeframe alignment.
* **Risk**: Position sizing, prop firm rules (Goat limits), drawdown and exposure monitoring.
* **Strategy**: Entry/exit engines, setup ranking based on confluence.
* **State**: Market state, account state, and trade state.
* **MCP**: Model Context Protocol server exposing tools to the LLM.

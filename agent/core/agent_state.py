"""
Agent State Management

Maintains the internal state of the Autonomous DeFi Agent.
Tracks balances, positions, trade history, and performance metrics.
"""

import time
import threading
from typing import Dict, List, Optional


class AgentState:

    def __init__(self):

        self._lock = threading.Lock()

        # Wallet balances
        self.wallet_balance: Dict[str, float] = {}

        # Open positions
        self.open_positions: List[dict] = []

        # Trade history
        self.trade_history: List[dict] = []

        # Performance metrics
        self.daily_pnl: float = 0.0
        self.total_pnl: float = 0.0

        # Timestamps
        self.last_trade_timestamp: Optional[float] = None
        self.start_time = time.time()

    # ------------------------------------------------------------------
    # BALANCE MANAGEMENT
    # ------------------------------------------------------------------

    def update_balance(self, token: str, amount: float):
        """Update token balance."""

        with self._lock:
            self.wallet_balance[token] = amount

    def get_balance(self, token: str) -> float:
        """Get balance for a token."""

        with self._lock:
            return self.wallet_balance.get(token, 0.0)

    def get_all_balances(self) -> Dict[str, float]:
        """Return all balances."""

        with self._lock:
            return dict(self.wallet_balance)

    # ------------------------------------------------------------------
    # POSITION MANAGEMENT
    # ------------------------------------------------------------------

    def add_position(self, position: dict):
        """Register a new open position."""

        with self._lock:
            position["timestamp"] = time.time()
            self.open_positions.append(position)

    def close_position(self, position_id: str):
        """Close an existing position."""

        with self._lock:

            for pos in self.open_positions:

                if pos.get("id") == position_id:
                    self.open_positions.remove(pos)
                    return pos

        return None

    def get_open_positions(self) -> List[dict]:
        """Return all open positions."""

        with self._lock:
            return list(self.open_positions)

    # ------------------------------------------------------------------
    # TRADE HISTORY
    # ------------------------------------------------------------------

    def record_trade(self, trade: dict):
        """Record executed trade."""

        with self._lock:

            trade["timestamp"] = time.time()
            self.trade_history.append(trade)

            self.last_trade_timestamp = trade["timestamp"]

    def get_trade_history(self) -> List[dict]:
        """Return trade history."""

        with self._lock:
            return list(self.trade_history)

    # ------------------------------------------------------------------
    # PNL MANAGEMENT
    # ------------------------------------------------------------------

    def update_pnl(self, pnl: float):
        """Update profit and loss metrics."""

        with self._lock:

            self.daily_pnl += pnl
            self.total_pnl += pnl

    def get_pnl(self):
        """Return current pnl metrics."""

        with self._lock:

            return {
                "daily_pnl": self.daily_pnl,
                "total_pnl": self.total_pnl
            }

    # ------------------------------------------------------------------
    # STATE SNAPSHOT
    # ------------------------------------------------------------------

    def snapshot(self):
        """
        Return a full snapshot of the agent state.
        Useful for monitoring or logging.
        """

        with self._lock:

            return {
                "wallet_balance": dict(self.wallet_balance),
                "open_positions": list(self.open_positions),
                "trade_history_count": len(self.trade_history),
                "daily_pnl": self.daily_pnl,
                "total_pnl": self.total_pnl,
                "last_trade_timestamp": self.last_trade_timestamp,
                "uptime_seconds": time.time() - self.start_time
            }

    # ------------------------------------------------------------------
    # RESET METHODS
    # ------------------------------------------------------------------

    def reset_daily_metrics(self):
        """Reset daily performance metrics."""

        with self._lock:
            self.daily_pnl = 0.0

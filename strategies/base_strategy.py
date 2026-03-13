"""
Base Strategy Interface for Autonomous DeFi Agent

All trading strategies must inherit from BaseStrategy.

This class defines the standard interface and common functionality
for all strategies used by the agent system.
"""

import time
from abc import ABC, abstractmethod


class BaseStrategy(ABC):

    def __init__(
        self,
        name: str,
        priority: int = 1,
        cooldown: int = 0,
        enabled: bool = True
    ):
        """
        Initialize a strategy.

        Args:
            name (str): Strategy name
            priority (int): Strategy priority (higher = more important)
            cooldown (int): Minimum seconds between actions
            enabled (bool): Whether strategy is active
        """

        self.name = name
        self.priority = priority
        self.cooldown = cooldown
        self.enabled = enabled

        self.last_execution_time = 0

    def is_enabled(self) -> bool:
        """Return whether strategy is enabled."""
        return self.enabled

    def set_enabled(self, value: bool):
        """Enable or disable strategy."""
        self.enabled = value

    def in_cooldown(self) -> bool:
        """Check whether the strategy is currently in cooldown."""
        if self.cooldown == 0:
            return False

        now = time.time()
        return (now - self.last_execution_time) < self.cooldown

    def update_execution_time(self):
        """Record the last execution timestamp."""
        self.last_execution_time = time.time()

    def evaluate_safe(self, market_data, agent_state):
        """
        Safe wrapper around evaluate().

        Handles:
        - disabled strategies
        - cooldown enforcement
        - error isolation
        """

        if not self.enabled:
            return None

        if self.in_cooldown():
            return None

        try:

            action = self.evaluate(market_data, agent_state)

            if action:
                action["strategy"] = self.name
                action["priority"] = self.priority
                action["timestamp"] = time.time()

            return action

        except Exception as e:
            print(f"[Strategy Error] {self.name}: {e}")
            return None

    @abstractmethod
    def evaluate(self, market_data, agent_state):
        """
        Core strategy logic.

        Must return either:
        - action dict
        - None

        Example action format:

        {
            "type": "swap",
            "protocol": "uniswap",
            "from_token": "USDT",
            "to_token": "ETH",
            "amount": 100
        }
        """
        pass

    def score(self, action) -> float:
        """
        Optional scoring function.

        Decision engine may use this to rank competing actions.

        Default implementation returns priority.
        """

        return float(self.priority)

    def on_trade_executed(self, action, result):
        """
        Hook executed after a successful trade.

        Can be overridden by strategies that need internal state updates.
        """

        self.update_execution_time()

    def on_trade_failed(self, action, error):
        """
        Hook executed when trade execution fails.

        Strategies may override this for retry logic or cooldown extension.
        """

        pass

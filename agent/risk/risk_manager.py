"""
Risk Manager

Enforces economic and operational constraints before
transactions are executed by the agent.

Responsibilities:
- trade size limits
- daily loss limits
- protocol whitelist
- wallet safety checks
- slippage validation
- gas sanity checks
"""

from typing import Dict
from agent.core.agent_state import AgentState


class RiskManager:

    def __init__(
        self,
        max_trade_size_usd: float = 1000,
        max_daily_loss_usd: float = 500,
        allowed_protocols=None,
        min_wallet_balance_eth: float = 0.05
    ):

        self.max_trade_size = max_trade_size_usd
        self.max_daily_loss = max_daily_loss_usd

        self.allowed_protocols = allowed_protocols or [
            "uniswap",
            "aave",
            "curve"
        ]

        self.min_wallet_balance_eth = min_wallet_balance_eth

    # --------------------------------------------------
    # MAIN VALIDATION PIPELINE
    # --------------------------------------------------

    def validate_action(
        self,
        action: Dict,
        agent_state: AgentState,
        wallet_controller,
        gas_estimator
    ):

        self._check_protocol(action)
        self._check_trade_size(action)
        self._check_daily_loss(agent_state)
        self._check_wallet_balance(wallet_controller)
        self._check_gas_price(gas_estimator)

        return True

    # --------------------------------------------------
    # PROTOCOL VALIDATION
    # --------------------------------------------------

    def _check_protocol(self, action):

        protocol = action.get("protocol")

        if protocol not in self.allowed_protocols:

            raise Exception(
                f"[RiskManager] Protocol not allowed: {protocol}"
            )

    # --------------------------------------------------
    # TRADE SIZE LIMIT
    # --------------------------------------------------

    def _check_trade_size(self, action):

        amount = action.get("amount")

        if amount is None:
            return

        if amount > self.max_trade_size:

            raise Exception(
                f"[RiskManager] Trade size exceeds limit: {amount}"
            )

    # --------------------------------------------------
    # DAILY LOSS LIMIT
    # --------------------------------------------------

    def _check_daily_loss(self, agent_state: AgentState):

        pnl = agent_state.get_pnl()

        if pnl["daily_pnl"] < -self.max_daily_loss:

            raise Exception(
                "[RiskManager] Daily loss limit exceeded"
            )

    # --------------------------------------------------
    # WALLET BALANCE SAFETY
    # --------------------------------------------------

    def _check_wallet_balance(self, wallet_controller):

        balance = wallet_controller.get_balance()

        if balance < self.min_wallet_balance_eth:

            raise Exception(
                "[RiskManager] Wallet balance too low for safe operation"
            )

    # --------------------------------------------------
    # GAS SAFETY
    # --------------------------------------------------

    def _check_gas_price(self, gas_estimator):

        if not gas_estimator.is_gas_price_acceptable():

            raise Exception(
                "[RiskManager] Gas price exceeds allowed threshold"
            )

    # --------------------------------------------------
    # SLIPPAGE VALIDATION
    # --------------------------------------------------

    def check_slippage(
        self,
        expected_price,
        execution_price,
        max_slippage_percent=2
    ):

        diff = abs(expected_price - execution_price)

        slippage = (diff / expected_price) * 100

        if slippage > max_slippage_percent:

            raise Exception(
                f"[RiskManager] Slippage too high: {slippage}%"
            )

        return True

"""
Gas Estimator

Responsible for estimating gas costs and validating
transaction economic viability.

Features:
- gas estimation
- gas price retrieval
- transaction cost calculation
- gas safety buffers
- gas limit enforcement
"""

from typing import Dict


class GasEstimator:

    def __init__(
        self,
        blockchain_client,
        max_gas_price_gwei: int = 100,
        gas_buffer: float = 1.2
    ):
        """
        Parameters

        blockchain_client : BlockchainClient
        max_gas_price_gwei : int
            Maximum acceptable gas price
        gas_buffer : float
            Safety multiplier for gas estimation
        """

        self.blockchain = blockchain_client
        self.max_gas_price_gwei = max_gas_price_gwei
        self.gas_buffer = gas_buffer

    # --------------------------------------------------
    # GAS PRICE
    # --------------------------------------------------

    def get_current_gas_price(self):

        gas_price = self.blockchain.get_gas_price()

        return gas_price

    # --------------------------------------------------
    # GAS LIMIT ESTIMATION
    # --------------------------------------------------

    def estimate_gas_limit(self, tx: Dict):

        try:

            gas_limit = self.blockchain.estimate_gas(tx)

            gas_limit = int(gas_limit * self.gas_buffer)

            return gas_limit

        except Exception as e:

            raise Exception(f"[GasEstimator] Gas estimation failed: {e}")

    # --------------------------------------------------
    # MAIN ESTIMATE ROUTINE
    # --------------------------------------------------

    def estimate(self, tx: Dict):

        gas_price = self.get_current_gas_price()

        gas_limit = self.estimate_gas_limit(tx)

        tx["gasPrice"] = gas_price
        tx["gas"] = gas_limit

        return gas_limit

    # --------------------------------------------------
    # COST CALCULATION
    # --------------------------------------------------

    def calculate_tx_cost(self, gas_limit: int, gas_price: int):

        cost_wei = gas_limit * gas_price

        cost_eth = self.blockchain.w3.from_wei(cost_wei, "ether")

        return float(cost_eth)

    # --------------------------------------------------
    # ECONOMIC VALIDATION
    # --------------------------------------------------

    def is_gas_price_acceptable(self):

        gas_price = self.get_current_gas_price()

        gas_price_gwei = self.blockchain.w3.from_wei(gas_price, "gwei")

        return gas_price_gwei <= self.max_gas_price_gwei

    # --------------------------------------------------
    # FULL GAS ANALYSIS
    # --------------------------------------------------

    def analyze_transaction(self, tx: Dict):

        gas_price = self.get_current_gas_price()

        gas_limit = self.estimate_gas_limit(tx)

        tx_cost = self.calculate_tx_cost(gas_limit, gas_price)

        gas_price_gwei = self.blockchain.w3.from_wei(gas_price, "gwei")

        return {
            "gas_limit": gas_limit,
            "gas_price_wei": gas_price,
            "gas_price_gwei": float(gas_price_gwei),
            "estimated_cost_eth": tx_cost,
            "gas_price_ok": gas_price_gwei <= self.max_gas_price_gwei
        }

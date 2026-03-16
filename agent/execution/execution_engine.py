"""
Execution Engine

Responsible for executing blockchain transactions produced
by the decision engine.

Pipeline:
1. Build transaction
2. Estimate gas
3. Sign transaction
4. Send transaction
5. Update agent state
"""

from typing import Dict

from agent.core.agent_state import AgentState


class ExecutionEngine:

    def __init__(self, wallet_controller, blockchain_client, gas_estimator):

        self.wallet = wallet_controller
        self.blockchain = blockchain_client
        self.gas_estimator = gas_estimator

    # --------------------------------------------------
    # MAIN EXECUTION ENTRYPOINT
    # --------------------------------------------------

    def execute(self, action: Dict, agent_state: AgentState):

        try:

            print(f"[ExecutionEngine] Executing action: {action}")

            tx = self.build_transaction(action)

            gas = self.estimate_gas(tx)

            tx["gas"] = gas

            signed_tx = self.sign_transaction(tx)

            tx_hash = self.send_transaction(signed_tx)

            self.update_state(action, tx_hash, agent_state)

            return tx_hash

        except Exception as e:

            print(f"[ExecutionEngine] Execution failed: {e}")
            return None

    # --------------------------------------------------
    # TRANSACTION BUILDING
    # --------------------------------------------------

    def build_transaction(self, action: Dict):

        """
        Convert action into a blockchain transaction.
        """

        tx = {
            "to": action.get("protocol_address"),
            "data": action.get("calldata"),
            "value": action.get("value", 0),
            "chain_id": action.get("chain_id"),
        }

        print(f"[ExecutionEngine] Transaction built")

        return tx

    # --------------------------------------------------
    # GAS ESTIMATION
    # --------------------------------------------------

    def estimate_gas(self, tx: Dict):

        gas = self.gas_estimator.estimate(tx)

        print(f"[ExecutionEngine] Gas estimated: {gas}")

        return gas

    # --------------------------------------------------
    # SIGNING
    # --------------------------------------------------

    def sign_transaction(self, tx: Dict):

        signed = self.wallet.sign_transaction(tx)

        print("[ExecutionEngine] Transaction signed")

        return signed

    # --------------------------------------------------
    # BROADCAST
    # --------------------------------------------------

    def send_transaction(self, signed_tx):

        tx_hash = self.blockchain.send_raw_transaction(signed_tx)

        print(f"[ExecutionEngine] TX sent: {tx_hash}")

        return tx_hash

    # --------------------------------------------------
    # STATE UPDATE
    # --------------------------------------------------

    def update_state(self, action, tx_hash, agent_state: AgentState):

        agent_state.record_trade({
            "type": action.get("type"),
            "tx_hash": tx_hash,
            "protocol": action.get("protocol"),
            "amount": action.get("amount"),
            "from_token": action.get("from_token"),
            "to_token": action.get("to_token")
        })

        print("[ExecutionEngine] Agent state updated")

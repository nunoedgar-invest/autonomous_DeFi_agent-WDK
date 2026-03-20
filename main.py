"""
Main Entrypoint for Autonomous DeFi Agent
"""

from agent.core.agent_state import AgentState
from agent.core.decision_engine import DecisionEngine
from agent.core.agent_loop import AgentLoop

from agent.execution.execution_engine import ExecutionEngine
from agent.execution.gas_estimator import GasEstimator

from agent.wallet.wallet_controller import WalletController
from agent.blockchain.blockchain_client import BlockchainClient

from agent.risk.risk_manager import RiskManager

from strategies.strategy_loader import load_strategies


def main():

    # ----------------------------------------
    # CONFIG
    # ----------------------------------------

    RPC_URL = "https://rpc.ankr.com/eth"
    PRIVATE_KEY = "YOUR_PRIVATE_KEY"

    # ----------------------------------------
    # CORE COMPONENTS
    # ----------------------------------------

    agent_state = AgentState()

    blockchain_client = BlockchainClient(RPC_URL)

    wallet = WalletController(
        private_key=PRIVATE_KEY,
        rpc_url=RPC_URL
    )

    gas_estimator = GasEstimator(blockchain_client)

    execution_engine = ExecutionEngine(
        wallet_controller=wallet,
        blockchain_client=blockchain_client,
        gas_estimator=gas_estimator
    )

    risk_manager = RiskManager()

    strategies = load_strategies()

    decision_engine = DecisionEngine(
        strategies=strategies,
        agent_state=agent_state
    )

    # ----------------------------------------
    # AGENT LOOP
    # ----------------------------------------

    agent_loop = AgentLoop(
        decision_engine=decision_engine,
        risk_manager=risk_manager,
        execution_engine=execution_engine,
        agent_state=agent_state,
        wallet_controller=wallet,
        gas_estimator=gas_estimator,
        loop_interval=10
    )

    agent_loop.start()


# ----------------------------------------
# RUN
# ----------------------------------------

if __name__ == "__main__":
    main()



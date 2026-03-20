"""
Agent Loop

Main autonomous execution loop of the DeFi agent.

Coordinates:
- market data ingestion
- strategy evaluation
- risk validation
- execution pipeline
"""

import time
from typing import Dict, Optional


class AgentLoop:

    def __init__(
        self,
        decision_engine,
        risk_manager,
        execution_engine,
        agent_state,
        wallet_controller,
        gas_estimator,
        market_data_provider=None,
        loop_interval: int = 10
    ):

        self.decision_engine = decision_engine
        self.risk_manager = risk_manager
        self.execution_engine = execution_engine
        self.agent_state = agent_state
        self.wallet = wallet_controller
        self.gas_estimator = gas_estimator
        self.market_data_provider = market_data_provider

        self.loop_interval = loop_interval
        self.running = False

    # --------------------------------------------------
    # CONTROL METHODS
    # --------------------------------------------------

    def start(self):

        print("[AgentLoop] Starting agent...")
        self.running = True

        while self.running:

            try:

                self._run_cycle()

            except Exception as e:

                print(f"[AgentLoop] Error in loop: {e}")

            time.sleep(self.loop_interval)

    def stop(self):

        print("[AgentLoop] Stopping agent...")
        self.running = False

    # --------------------------------------------------
    # SINGLE EXECUTION CYCLE
    # --------------------------------------------------

    def _run_cycle(self):

        print("\n[AgentLoop] New cycle")

        market_data = self._get_market_data()

        action = self._decide(market_data)

        if not action:

            print("[AgentLoop] No action decided")
            return

        self._validate(action)

        tx_hash = self._execute(action)

        print(f"[AgentLoop] Cycle completed | TX: {tx_hash}")

    # --------------------------------------------------
    # MARKET DATA
    # --------------------------------------------------

    def _get_market_data(self) -> Dict:

        if self.market_data_provider:

            return self.market_data_provider.get_data()

        # fallback mock data (for demo/hackathon)
        return {
            "ETH_price": 3000,
            "ETH_change_24h": -2.5,
            "gas_price": 25
        }

    # --------------------------------------------------
    # DECISION
    # --------------------------------------------------

    def _decide(self, market_data: Dict) -> Optional[Dict]:

        action = self.decision_engine.decide(market_data)

        if action:
            print(f"[AgentLoop] Action decided: {action}")

        return action

    # --------------------------------------------------
    # RISK VALIDATION
    # --------------------------------------------------

    def _validate(self, action: Dict):

        print("[AgentLoop] Running risk checks")

        self.risk_manager.validate_action(
            action,
            self.agent_state,
            self.wallet,
            self.gas_estimator
        )

    # --------------------------------------------------
    # EXECUTION
    # --------------------------------------------------

    def _execute(self, action: Dict):

        print("[AgentLoop] Executing action")

        tx_hash = self.execution_engine.execute(
            action,
            self.agent_state
        )

        return tx_hash

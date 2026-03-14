"""
Decision Engine

Responsible for evaluating loaded strategies and selecting
the best action to execute based on priority and constraints.
"""

import time
from typing import List, Optional, Dict

from agent.core.agent_state import AgentState
from strategies.base_strategy import BaseStrategy


class DecisionEngine:

    def __init__(self, strategies: List[BaseStrategy], agent_state: AgentState):

        self.strategies = strategies
        self.agent_state = agent_state

        # track last execution per strategy
        self.strategy_last_run = {}

    # --------------------------------------------------
    # STRATEGY COOLDOWN MANAGEMENT
    # --------------------------------------------------

    def _cooldown_passed(self, strategy: BaseStrategy) -> bool:
        """Check if strategy cooldown has passed."""

        last_run = self.strategy_last_run.get(strategy.name)

        if last_run is None:
            return True

        elapsed = time.time() - last_run

        return elapsed >= strategy.cooldown

    def _mark_strategy_run(self, strategy: BaseStrategy):

        self.strategy_last_run[strategy.name] = time.time()

    # --------------------------------------------------
    # STRATEGY EVALUATION
    # --------------------------------------------------

    def evaluate_strategies(self, market_data: Dict) -> List[Dict]:
        """
        Evaluate all strategies and collect proposed actions.
        """

        proposals = []

        for strategy in self.strategies:

            if not self._cooldown_passed(strategy):
                continue

            try:

                action = strategy.evaluate(market_data, self.agent_state)

                if action:

                    proposals.append({
                        "strategy": strategy,
                        "priority": strategy.priority,
                        "action": action
                    })

            except Exception as e:

                print(f"[DecisionEngine] Strategy {strategy.name} failed: {e}")

        return proposals

    # --------------------------------------------------
    # ACTION SELECTION
    # --------------------------------------------------

    def select_best_action(self, proposals: List[Dict]) -> Optional[Dict]:
        """
        Select the highest priority action from proposals.
        """

        if not proposals:
            return None

        proposals.sort(key=lambda x: x["priority"], reverse=True)

        best = proposals[0]

        return best

    # --------------------------------------------------
    # DECISION PIPELINE
    # --------------------------------------------------

    def decide(self, market_data: Dict) -> Optional[Dict]:
        """
        Full decision pipeline.
        """

        proposals = self.evaluate_strategies(market_data)

        if not proposals:
            return None

        best = self.select_best_action(proposals)

        strategy = best["strategy"]

        self._mark_strategy_run(strategy)

        return best["action"]

"""
Example Usage

Inside the agent loop:
"""

from agent.core.decision_engine import DecisionEngine

engine = DecisionEngine(strategies, agent_state)

action = engine.decide(market_data)

""" 
Example return:
"""

{
 "type": "swap",
 "protocol": "uniswap",
 "from_token": "USDT",
 "to_token": "ETH",
 "amount": 100
}

"""
This action would then go to:
"""

execution_engine.execute(action)

""" 
# Example Market Data Input
"""

market_data = {
    "ETH_price": 2950,
    "ETH_change_24h": -3.4,
    "gas_price": 22
}




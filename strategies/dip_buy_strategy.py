from strategies.base_strategy import BaseStrategy


class DipBuyStrategy(BaseStrategy):

    def __init__(self):
        super().__init__(
            name="DipBuyStrategy",
            priority=5,
            cooldown=300
        )

    def evaluate(self, market_data, agent_state):

        if market_data["ETH_change_24h"] < -3:
            return {
                "type": "swap",
                "protocol": "uniswap",
                "from_token": "USDT",
                "to_token": "ETH",
                "amount": 100
            }

        return None

  

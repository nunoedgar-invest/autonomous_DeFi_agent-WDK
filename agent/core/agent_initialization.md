Inside your agent initialization:

```Python
from agent.core.strategy_loader import StrategyLoader

loader = StrategyLoader()
strategies = loader.load_strategies()

```

Output example:

```
[StrategyLoader] Found modules: ['dip_buy_strategy']
[StrategyLoader] Loaded strategy: DipBuyStrategy
[StrategyLoader] Total strategies loaded: 1
```

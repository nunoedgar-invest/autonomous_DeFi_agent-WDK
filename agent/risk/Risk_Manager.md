# Responsibilities of the Risk Manager

The module should enforce:


• maximum trade size

• maximum daily loss

• allowed protocol whitelist

• minimum wallet balance safety buffer

• slippage limits

• cooldown safeguards

• gas sanity checks

• protocol restrictions


This ensures the agent **cannot destroy its own capital**.


# Example Integration

### Inside your Execution Pipeline:

```Python
risk_manager.validate_action(
    action,
    agent_state,
    wallet_controller,
    gas_estimator
)
```

If validation passes:
```Python
ExecutionEngine.execute(action)
```

If not:
```Python
ExecutionEngine.execute(action)
```

# Example Action Being Checked

```Python
action = {
    "type": "swap",
    "protocol": "uniswap",
    "from_token": "USDT",
    "to_token": "ETH",
    "amount": 500
}
```

The risk manager will verify:


• protocol allowed

• trade size < limit


• daily loss < limit

• wallet balance sufficient

• gas price acceptable


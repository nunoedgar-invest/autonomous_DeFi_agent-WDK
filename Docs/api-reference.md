# API Reference

Recommended files:

```Bash
docs/

architecture.md
agent-design.md
strategy-framework.md
risk-model.md
execution-layer.md
api-reference.md
frontend-dashboard.md
deployment.md
```


## Agent

GET /api/agent/status

Returns agent runtime status.

POST /api/agent/start

Starts the autonomous trading agent.

POST /api/agent/stop

Stops the trading agent.

---

## Wallet

GET /api/wallet

Returns wallet address and balance.

---

## Trades

GET /api/trades

Returns trade history.

POST /api/trades/execute

Execute a manual trade.

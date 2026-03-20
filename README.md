# Autonomous_DeFi_Agent-WDK

### Hackathon Galáctica – WDK Edition 1

An autonomous AI-powered DeFi agent capable of managing a self-custodial wallet, executing on-chain transactions, calculating gas fees, and interacting with DeFi smart contracts across multiple blockchains.

Built for **Hackathon Galáctica: WDK Edition 1** by **Tether**.

---

# Overview

AI agents are evolving beyond simple assistants.
This project explores **agents as economic infrastructure**: autonomous systems that manage capital, execute tasks, and interact with blockchain logic under predefined constraints.

The **Autonomous DeFi Agent** acts as an automated financial operator capable of:

* Managing a self-custodial wallet
* Monitoring DeFi markets
* Executing trading strategies
* Calculating optimal gas fees
* Interacting with smart contracts
* Settling transactions on-chain

---

```Bash
pip install python-dotenv
``` 

# Key Features

### Self-Custodial Wallet Management

The agent controls its own wallet and signs transactions locally.

### Autonomous Trade Execution

Implements strategy logic that determines when to execute trades.

### Gas Fee Optimization

Uses on-chain data to calculate optimal gas price before execution.

### Smart Contract Interaction Pipeline

Supports interaction with DeFi protocols (DEX swaps, staking, lending).

### Multi-Chain Ready Architecture

Designed to support multiple EVM-compatible chains.

---

# Architecture

User / Strategy Input
↓
AI Decision Engine
↓
Execution Layer
↓
Wallet Controller
↓
Blockchain Interaction Layer
↓
Smart Contract Pipeline

---

# System Components

## AI Decision Engine

Responsible for:

* strategy evaluation
* risk management
* execution triggers

Example logic:

```
IF ETH price dips >3% in 24h
AND gas price < threshold
THEN execute swap USDT → ETH
```

---

## Wallet Controller

Handles:

* wallet creation
* private key management
* transaction signing

Example:

```
wallet = new ethers.Wallet(PRIVATE_KEY, provider)
```

---

## Gas Estimator

Calculates optimal transaction parameters:

* gas price
* maxFeePerGas
* maxPriorityFeePerGas

Transactions are simulated before execution to prevent failures.

---

## Transaction Execution Engine

Responsible for:

1. token approval
2. trade execution
3. confirmation tracking
4. portfolio update

Example pipeline:

```
Approve Token
Swap Token
Verify Settlement
Update Agent State
```

---

# Project Structure
```
autonomous-defi-agent/
│
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── .env.example
├── .gitignore
│
├── docs/
│   ├── architecture.md
│   ├── agent-design.md
│   ├── smart-contracts.md
│   └── demo-guide.md
│
├── agent/
│   ├── core/
│   │   ├── decision_engine.py
│   │   ├── strategy_engine.py
│   │   └── risk_manager.py
│   │
│   ├── monitoring/
│   │   ├── price_monitor.py
│   │   └── gas_monitor.py
│   │
│   ├── execution/
│   │   ├── trade_executor.py
│   │   └── tx_pipeline.py
│   │
│   └── run_agent.py
│
├── blockchain/
│   ├── wallet/
│   │   ├── wallet_manager.py
│   │   └── key_store.py
│   │
│   ├── gas/
│   │   └── gas_estimator.py
│   │
│   ├── chains/
│   │   ├── ethereum.py
│   │   ├── polygon.py
│   │   └── arbitrum.py
│   │
│   └── rpc_client.py
│
├── contracts/
│   ├── AgentVault.sol
│   ├── AgentExecutor.sol
│   │
│   ├── interfaces/
│   │   ├── IUniswapRouter.sol
│   │   └── IERC20.sol
│   │
│   └── scripts/
│       ├── deploy.ts
│       └── verify.ts
│
├── api/
│   ├── server.py
│   ├── routes/
│   │   ├── portfolio.py
│   │   └── agent_control.py
│   │
│   └── schemas/
│       └── models.py
│
├── dashboard/
│   ├── frontend/
│   │   ├── pages/
│   │   ├── components/
│   │   └── services/
│   │
│   └── package.json
│
├── strategies/
│   ├── dip_buy_strategy.py
│   ├── arbitrage_strategy.py
│   └── rebalance_strategy.py
│
├── simulations/
│   ├── backtest_engine.py
│   └── scenario_tests.py
│
├── tests/
│   ├── test_agent.py
│   ├── test_wallet.py
│   └── test_strategies.py
│
├── scripts/
│   ├── start_agent.sh
│   ├── deploy_contracts.sh
│   └── setup_env.sh
│
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
│
└── .github/
    ├── workflows/
    │   └── ci.yml
    │
    └── ISSUE_TEMPLATE/
        ├── bug_report.md
        └── feature_request.md
```

```
docs/
```
Include:

architecture diagram

design explanation

demo instructions

```
contracts/
```
Contains:

vault contracts

executor contracts

interfaces

This shows proper Web3 engineering practices.

### 4️⃣ Strategy Modules
```
strategies/
```
Allows plug-in strategies:
```
dip buy
arbitrage
yield farming
portfolio rebalance

```

### 5️⃣ Simulations / Backtesting
```
simulations/
```
Example:
```
simulate strategy over historical prices
```
Even a simple simulation module adds huge credibility.
---

# Tech Stack

AI / Backend

* Python
* FastAPI
* LangChain

Blockchain

* ethers.js
* web3.py
* Hardhat

Infrastructure

* Docker
* Redis

Data Sources

* RPC Nodes
* DEX APIs
* Gas Oracles

---

# Security Constraints

The agent operates under strict rules to reduce risk.

Example:

```
max_trade_size = 1000 USD
max_daily_loss = 5%
allowed_protocols = ["Uniswap", "Aave"]
```

Transactions outside these parameters are rejected.

---

# Getting Started

## Clone the repository

```
git clone https://github.com/YOUR_USERNAME/autonomous-defi-agent.git
cd autonomous-defi-agent
```

---

## Install dependencies

```
pip install -r requirements.txt
```

or

```
npm install
```

---

## Configure environment

Create a `.env` file:

```
PRIVATE_KEY=
RPC_URL=
CHAIN_ID=
```

---

## Run the agent

```
python agent/run_agent.py
```

---

# Demo Scenario

1. User deposits USDT
2. Agent monitors ETH market
3. ETH price drops below defined threshold
4. Agent calculates gas cost
5. Agent swaps USDT → ETH
6. Transaction confirmed on-chain
7. Portfolio updated

---

# Future Improvements

* cross-chain arbitrage
* autonomous portfolio rebalancing
* MEV-aware routing
* agent-to-agent trading
* DAO-governed strategy modules

---

# Hackathon Submission

Project created for:

**Hackathon Galáctica: WDK Edition 1**

Hosted by **Tether**

Theme: **Agents as Economic Infrastructure**

---

# License

MIT License

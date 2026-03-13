# Contributing to Autonomous DeFi Agent

This file explains how people can contribute to your project.
It prevents confusion and keeps contributions organized.

Thank you for your interest in contributing to **Autonomous DeFi Agent**.
This project explores autonomous agents as economic infrastructure capable of interacting with DeFi protocols and executing on-chain financial strategies.

We welcome contributions from developers, researchers, and builders interested in **AI agents, blockchain infrastructure, and decentralized finance**.

---

# Ways to Contribute

You can contribute in several ways:

* Reporting bugs
* Suggesting new features
* Implementing trading strategies
* Improving documentation
* Writing tests
* Improving performance or security

All contributions that improve the project are welcome.

---

# Development Setup

## 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/autonomous-defi-agent.git
cd autonomous-defi-agent
```

## 2. Install dependencies

Python dependencies:

```bash
pip install -r requirements.txt
```

JavaScript dependencies (for smart contracts or frontend):

```bash
npm install
```

---

## 3. Configure environment variables

Create a `.env` file using the provided template:

```
cp .env.example .env
```

Example variables:

```
RPC_URL=
PRIVATE_KEY=
CHAIN_ID=
MAX_TRADE_SIZE=1000
MAX_DAILY_LOSS=5
```

---

## 4. Run the agent locally

```bash
python agent/run_agent.py
```

---

# Branching Strategy

We use a simple Git branching workflow.

Main branches:

* **main** → stable production-ready code
* **dev** → active development branch

Feature branches should follow this format:

```
feature/<feature-name>
```

Example:

```
feature/gas-estimator
feature/arbitrage-strategy
feature/wallet-manager
```

Bug fixes:

```
fix/<bug-name>
```

---

# Pull Request Guidelines

Before submitting a Pull Request:

* Ensure your code builds successfully
* Ensure tests pass
* Update documentation if necessary
* Clearly describe the purpose of the change

Pull requests should include:

* A clear title
* A detailed description of changes
* Any relevant issue references

Example PR title:

```
Add gas fee estimator module
```

---

# Coding Standards

Please follow these guidelines:

### Python

* Follow **PEP8** style guidelines
* Use descriptive variable and function names
* Write docstrings for public functions

### Smart Contracts

* Follow Solidity best practices
* Add comments explaining contract logic
* Avoid unnecessary complexity

### General

* Keep functions small and focused
* Prefer readability over cleverness
* Document non-obvious behavior

---

# Testing

When possible, include tests for new functionality.

Run tests with:

```bash
pytest
```

Smart contract tests:

```bash
npx hardhat test
```

---

# Reporting Issues

If you find a bug, please open an issue including:

* description of the issue
* steps to reproduce
* expected behavior
* actual behavior
* environment information

This helps maintainers resolve issues quickly.

---

# Security Issues

Because this project interacts with **financial infrastructure and blockchain assets**, security vulnerabilities should be reported responsibly.

If you discover a security issue, please **do not open a public issue**.
Instead contact the maintainers privately.

---

# Community

By contributing, you agree to follow our **Code of Conduct**.

We aim to maintain a collaborative, respectful, and inclusive environment for all contributors.

Thank you for helping improve the Autonomous DeFi Agent project.

```Bash
git add CONTRIBUTING.md CODE_OF_CONDUCT.md
git commit -m "Add contribution guidelines and code of conduct"
git push
```


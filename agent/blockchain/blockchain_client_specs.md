# Blockchain Client Specification for Buildes

This module will be the single interface to the blockchain, which is a best practice in trading infrastructure.

It will handle:

• RPC connection management
• transaction broadcasting
• confirmation tracking
• gas estimation
• balance queries
• smart contract interactions
• event logs
• multi-chain readiness

```Bash
Decision Engine
      ↓
Execution Engine
      ↓
Wallet Controller
      ↓
Blockchain Client
      ↓
RPC / Blockchain Network
```

# Example Usage

### Initialize Client

```Python
from agent.blockchain.blockchain_client import BlockchainClient

client = BlockchainClient(
    rpc_url="https://rpc.ankr.com/eth"
)
```

### Check Network
```Python
print(client.get_chain_id())
print(client.get_block_number())
```

### Broadcast Transaction
```Python
tx_hash = client.send_raw_transaction(signed_tx)
```

### Wait for Confirmation

```Python
receipt = client.wait_for_confirmation(tx_hash)
```

### Read Balance

```Python
balance = client.get_balance("0xWalletAddress")
```

### Load Smart Contract

```Python
contract = client.load_contract(
    address="0xUniswapRouter",
    abi=router_abi
)
```

### Call Contract Function

```Python
price = client.call_contract_function(
    contract,
    "getAmountsOut",
    amount,
    path
)
```



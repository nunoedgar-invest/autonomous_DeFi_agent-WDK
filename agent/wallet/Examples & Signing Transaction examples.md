# Example Usage

```Python
from agent.wallet.wallet_controller import WalletController

wallet = WalletController(
    private_key="YOUR_PRIVATE_KEY",
    rpc_url="https://mainnet.infura.io/v3/YOUR_KEY"
)

print(wallet.wallet_status())
```
Example output:
```Python
{
 "address": "0x92A4...C4F",
 "balance": 1.82,
 "nonce": 14
}
```

# Transaction Signing Example

```Python
tx = {
    "to": "0xUniswapRouter",
    "value": 0,
    "gas": 210000,
    "chainId": 1,
    "data": "0xabc123"
}

signed = wallet.sign_transaction(tx)
```

This signed transaction will then be sent by:

```Python
blockchain_client.send_raw_transaction(signed)
```

# Security Recommendation (Important for Repo)

Never commit private keys.

Use .env file:

```Bash
PRIVATE_KEY=0x123...
RPC_URL=https://rpc.ankr.com/eth
```

Load it with:

```Python
from dotenv import load_dotenv
import os

load_dotenv()

private_key = os.getenv("PRIVATE_KEY")
```

Add to .gitignore:

```Bash
.env
```


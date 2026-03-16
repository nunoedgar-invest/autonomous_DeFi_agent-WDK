"""
Blockchain Client

Handles all blockchain RPC communication.

Responsibilities:
- send transactions
- wait for confirmations
- read balances
- interact with smart contracts
- retrieve gas data
- support multi-chain RPC connections
"""

from web3 import Web3
from typing import Optional


class BlockchainClient:

    def __init__(self, rpc_url: str):

        self.w3 = Web3(Web3.HTTPProvider(rpc_url))

        if not self.w3.is_connected():
            raise Exception("Unable to connect to RPC node")

        print("[BlockchainClient] Connected to RPC node")

    # --------------------------------------------------
    # NETWORK INFORMATION
    # --------------------------------------------------

    def get_chain_id(self):

        return self.w3.eth.chain_id

    def get_block_number(self):

        return self.w3.eth.block_number

    def get_gas_price(self):

        return self.w3.eth.gas_price

    # --------------------------------------------------
    # ACCOUNT OPERATIONS
    # --------------------------------------------------

    def get_balance(self, address: str):

        balance

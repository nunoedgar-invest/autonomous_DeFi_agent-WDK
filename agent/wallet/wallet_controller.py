"""
Wallet Controller

Manages the agent's self-custodial wallet.

Responsibilities:
- load wallet from private key
- expose wallet address
- manage nonce
- sign transactions
"""

import os
from web3 import Web3


class WalletController:

    def __init__(self, private_key: str, rpc_url: str):

        self.w3 = Web3(Web3.HTTPProvider(rpc_url))

        if not self.w3.is_connected():
            raise Exception("Failed to connect to blockchain RPC")

        self.private_key = private_key
        self.account = self.w3.eth.account.from_key(private_key)

        self.address = self.account.address

        print(f"[WalletController] Wallet loaded: {self.address}")

    # --------------------------------------------------
    # BASIC WALLET INFO
    # --------------------------------------------------

    def get_address(self):
        return self.address

    def get_balance(self):

        balance = self.w3.eth.get_balance(self.address)

        return self.w3.from_wei(balance, "ether")

    # --------------------------------------------------
    # NONCE MANAGEMENT
    # --------------------------------------------------

    def get_nonce(self):

        nonce = self.w3.eth.get_transaction_count(self.address)

        return nonce

    # --------------------------------------------------
    # TRANSACTION SIGNING
    # --------------------------------------------------

    def sign_transaction(self, tx):

        tx["nonce"] = self.get_nonce()

        tx["from"] = self.address

        if "gasPrice" not in tx:
            tx["gasPrice"] = self.w3.eth.gas_price

        signed_tx = self.w3.eth.account.sign_transaction(
            tx,
            self.private_key
        )

        return signed_tx.rawTransaction

    # --------------------------------------------------
    # GAS PRICE
    # --------------------------------------------------

    def get_gas_price(self):

        return self.w3.eth.gas_price

    # --------------------------------------------------
    # WALLET STATUS
    # --------------------------------------------------

    def wallet_status(self):

        return {
            "address": self.address,
            "balance": float(self.get_balance()),
            "nonce": self.get_nonce()
        }

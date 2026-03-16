"""
Blockchain Client

Handles all blockchain RPC communication for the Autonomous DeFi Agent.

Responsibilities:
- manage RPC connection
- send transactions
- wait for confirmations
- read balances
- estimate gas
- interact with smart contracts
- fetch blockchain data
"""

from web3 import Web3
from web3.exceptions import TransactionNotFound
from typing import Optional, Dict
import time


class BlockchainClient:

    def __init__(self, rpc_url: str):

        self.w3 = Web3(Web3.HTTPProvider(rpc_url))

        if not self.w3.is_connected():
            raise Exception("[BlockchainClient] RPC connection failed")

        print(f"[BlockchainClient] Connected to network | ChainID: {self.w3.eth.chain_id}")

    # --------------------------------------------------
    # NETWORK INFO
    # --------------------------------------------------

    def get_chain_id(self) -> int:
        return self.w3.eth.chain_id

    def get_block_number(self) -> int:
        return self.w3.eth.block_number

    def get_gas_price(self) -> int:
        return self.w3.eth.gas_price

    # --------------------------------------------------
    # BALANCE OPERATIONS
    # --------------------------------------------------

    def get_balance(self, address: str):

        balance = self.w3.eth.get_balance(address)

        return self.w3.from_wei(balance, "ether")

    # --------------------------------------------------
    # GAS ESTIMATION
    # --------------------------------------------------

    def estimate_gas(self, tx: Dict):

        try:

            gas = self.w3.eth.estimate_gas(tx)

            return gas

        except Exception as e:

            raise Exception(f"[BlockchainClient] Gas estimation failed: {e}")

    # --------------------------------------------------
    # TRANSACTION BROADCAST
    # --------------------------------------------------

    def send_raw_transaction(self, signed_tx: bytes):

        try:

            tx_hash = self.w3.eth.send_raw_transaction(signed_tx)

            return self.w3.to_hex(tx_hash)

        except Exception as e:

            raise Exception(f"[BlockchainClient] TX broadcast failed: {e}")

    # --------------------------------------------------
    # TRANSACTION STATUS
    # --------------------------------------------------

    def get_transaction(self, tx_hash: str):

        try:

            tx = self.w3.eth.get_transaction(tx_hash)

            return tx

        except TransactionNotFound:

            return None

    def get_transaction_receipt(self, tx_hash: str):

        try:

            receipt = self.w3.eth.get_transaction_receipt(tx_hash)

            return receipt

        except TransactionNotFound:

            return None

    # --------------------------------------------------
    # CONFIRMATION TRACKING
    # --------------------------------------------------

    def wait_for_confirmation(
        self,
        tx_hash: str,
        timeout: int = 120,
        poll_interval: int = 3
    ):

        start_time = time.time()

        while True:

            receipt = self.get_transaction_receipt(tx_hash)

            if receipt is not None:

                if receipt["status"] == 1:
                    print(f"[BlockchainClient] TX confirmed: {tx_hash}")
                else:
                    print(f"[BlockchainClient] TX failed: {tx_hash}")

                return receipt

            if time.time() - start_time > timeout:

                raise TimeoutError(f"[BlockchainClient] Confirmation timeout: {tx_hash}")

            time.sleep(poll_interval)

    # --------------------------------------------------
    # CONTRACT INTERACTION
    # --------------------------------------------------

    def load_contract(self, address: str, abi):

        contract = self.w3.eth.contract(
            address=Web3.to_checksum_address(address),
            abi=abi
        )

        return contract

    def call_contract_function(self, contract, function_name: str, *args):

        try:

            fn = getattr(contract.functions, function_name)

            result = fn(*args).call()

            return result

        except Exception as e:

            raise Exception(f"[BlockchainClient] Contract call failed: {e}")

    # --------------------------------------------------
    # EVENT LOGS
    # --------------------------------------------------

    def get_logs(self, filter_params: Dict):

        try:

            logs = self.w3.eth.get_logs(filter_params)

            return logs

        except Exception as e:

            raise Exception(f"[BlockchainClient] Log fetch failed: {e}")

from solana.rpc.api import Client
from solana.transaction import Transaction
from solana.system_program import transfer, TransferParams
from solana.publickey import PublicKey
from solana.keypair import Keypair

class SolanaTaskLogger:
    """Handles on-chain task logging for Aether agents."""

    def __init__(self, rpc_url="https://api.mainnet-beta.solana.com"):
        self.client = Client(rpc_url)

    def log_task(self, sender_keypair, task_description, task_result):
        """Log a task and its result on-chain."""
        data = f"Task: {task_description}\nResult: {task_result}".encode("utf-8")
        transaction = Transaction().add(
            transfer(
                TransferParams(
                    from_pubkey=sender_keypair.public_key,
                    to_pubkey=sender_keypair.public_key,  # Sending to self as a log
                    lamports=5000,  # Minimal lamports for transaction
                )
            )
        )
        transaction.add_memo(data)
        response = self.client.send_transaction(transaction, sender_keypair)
        print(f"Task logged on-chain with transaction signature: {response['result']}")
        return response["result"]
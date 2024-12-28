from solana.rpc.api import Client
from solana.transaction import Transaction
from solana.publickey import PublicKey
from solana.keypair import Keypair
from solana.system_program import transfer, TransferParams
from solana.rpc.types import TxOpts

class SolanaUtils:
    """Utility class for interacting with the Solana blockchain."""

    def __init__(self, rpc_url="https://api.mainnet-beta.solana.com"):
        self.client = Client(rpc_url)

    def get_balance(self, public_key):
        """Get the balance of a Solana account."""
        balance = self.client.get_balance(public_key)
        return balance["result"]["value"]

    def send_transaction(self, sender_keypair, recipient_pubkey, amount):
        """Send SOL from one account to another."""
        transaction = Transaction().add(
            transfer(
                TransferParams(
                    from_pubkey=sender_keypair.public_key,
                    to_pubkey=PublicKey(recipient_pubkey),
                    lamports=amount,
                )
            )
        )
        response = self.client.send_transaction(
            transaction, sender_keypair, opts=TxOpts(skip_preflight=True)
        )
        return response["result"]

    def deploy_program(self, sender_keypair, program_path):
        """Deploy a Solana smart contract (BPF program)."""
        with open(program_path, "rb") as program_file:
            program_data = program_file.read()
        transaction = Transaction()
        transaction.add(
            self.client.request_airdrop(sender_keypair.public_key, 1_000_000_000)
        )  # Add lamports for deployment
        response = self.client.send_transaction(
            transaction, sender_keypair, opts=TxOpts(skip_preflight=True)
        )
        return response["result"]
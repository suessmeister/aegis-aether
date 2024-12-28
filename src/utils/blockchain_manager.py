from solana.rpc.api import Client as SolanaClient
from solana.transaction import Transaction
from solana.keypair import Keypair
from solana.publickey import PublicKey
from solana.system_program import transfer, TransferParams
from web3 import Web3


class BlockchainManager:
    """Manages multi-chain blockchain interactions for Solana and Ethereum-based chains."""

    def __init__(self, solana_rpc_url="https://api.mainnet-beta.solana.com", ethereum_rpc_url=None):
        self.solana_client = SolanaClient(solana_rpc_url)
        self.web3 = Web3(Web3.HTTPProvider(ethereum_rpc_url)) if ethereum_rpc_url else None

    # Solana Methods
    def solana_get_balance(self, public_key):
        """Get the balance of a Solana account."""
        balance = self.solana_client.get_balance(public_key)
        return balance["result"]["value"]

    def solana_send_transaction(self, sender_keypair, recipient_pubkey, amount):
        """Send SOL from one Solana account to another."""
        transaction = Transaction().add(
            transfer(
                TransferParams(
                    from_pubkey=sender_keypair.public_key,
                    to_pubkey=PublicKey(recipient_pubkey),
                    lamports=amount,
                )
            )
        )
        response = self.solana_client.send_transaction(transaction, sender_keypair)
        return response["result"]

    # Ethereum Methods
    def ethereum_get_balance(self, address):
        """Get the balance of an Ethereum account."""
        if self.web3:
            balance = self.web3.eth.get_balance(Web3.toChecksumAddress(address))
            return self.web3.fromWei(balance, "ether")
        else:
            print("Ethereum provider not configured.")
            return None

    def ethereum_send_transaction(self, sender_key, recipient_address, amount_ether):
        """Send ETH from one account to another."""
        if self.web3:
            sender_address = self.web3.eth.account.privateKeyToAccount(sender_key).address
            tx = {
                "from": sender_address,
                "to": Web3.toChecksumAddress(recipient_address),
                "value": self.web3.toWei(amount_ether, "ether"),
                "gas": 21000,
                "gasPrice": self.web3.eth.gas_price,
                "nonce": self.web3.eth.get_transaction_count(sender_address),
            }
            signed_tx = self.web3.eth.account.sign_transaction(tx, sender_key)
            tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
            return self.web3.toHex(tx_hash)
        else:
            print("Ethereum provider not configured.")
            return None
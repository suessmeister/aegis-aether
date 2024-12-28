from web3 import Web3

class BlockchainIntegration:
    def __init__(self, provider_url):
        self.web3 = Web3(Web3.HTTPProvider(provider_url))
        if self.web3.isConnected():
            print("Connected to blockchain!")
        else:
            print("Failed to connect to blockchain.")

    def deploy_contract(self, abi, bytecode):
        """Deploy a smart contract."""
        account = self.web3.eth.accounts[0]
        Contract = self.web3.eth.contract(abi=abi, bytecode=bytecode)
        tx_hash = Contract.constructor().transact({"from": account})
        tx_receipt = self.web3.eth.wait_for_transaction_receipt(tx_hash)
        print(f"Contract deployed at address: {tx_receipt.contractAddress}")
        return tx_receipt.contractAddress

    def interact_with_contract(self, contract_address, abi, function_name, *args):
        """Interact with a deployed contract."""
        contract = self.web3.eth.contract(address=contract_address, abi=abi)
        func = contract.functions[function_name](*args)
        tx_hash = func.transact({"from": self.web3.eth.accounts[0]})
        self.web3.eth.wait_for_transaction_receipt(tx_hash)
        print(f"Function {function_name} executed on contract {contract_address}.")

# Example usage
if __name__ == "__main__":
    abi = [...]  # Add contract ABI here
    bytecode = "..."  # Add contract bytecode here
    blockchain = BlockchainIntegration("https://mainnet.infura.io/v3/YOUR_PROJECT_ID")
    contract_address = blockchain.deploy_contract(abi, bytecode)
    blockchain.interact_with_contract(contract_address, abi, "yourFunction", "arg1", "arg2")
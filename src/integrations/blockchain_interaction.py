from web3 import Web3

class BlockchainIntegration:
    """Blockchain integration using Web3."""
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

    def call_contract_function(self, contract_address, abi, function_name, *args):
        """Call a function on a deployed contract."""
        contract = self.web3.eth.contract(address=contract_address, abi=abi)
        func = contract.functions[function_name](*args)
        tx_hash = func.transact({"from": self.web3.eth.accounts[0]})
        self.web3.eth.wait_for_transaction_receipt(tx_hash)
        print(f"Function {function_name} executed on contract {contract_address}.")

# Example usage
if __name__ == "__main__":
    abi = [...]  # Add your contract ABI here
    bytecode = "..."  # Add your contract bytecode here
    blockchain = BlockchainIntegration("http://127.0.0.1:8545")
    contract_address = blockchain.deploy_contract(abi, bytecode)
    blockchain.call_contract_function(contract_address, abi, "yourFunction", "arg1", "arg2")
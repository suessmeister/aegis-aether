import requests

class IPFSCommunication:
    """Decentralized communication using IPFS."""
    def __init__(self, api_url="http://127.0.0.1:5001"):
        self.api_url = api_url

    def send_message(self, message):
        """Send a message by uploading it to IPFS."""
        response = requests.post(f"{self.api_url}/api/v0/add", files={"file": message.encode()})
        if response.status_code == 200:
            ipfs_hash = response.json()["Hash"]
            print(f"Message sent to IPFS with hash: {ipfs_hash}")
            return ipfs_hash
        else:
            print("Failed to send message to IPFS.")
            return None

    def retrieve_message(self, ipfs_hash):
        """Retrieve a message from IPFS using its hash."""
        response = requests.get(f"{self.api_url}/api/v0/cat?arg={ipfs_hash}")
        if response.status_code == 200:
            print(f"Message retrieved from IPFS: {response.text}")
            return response.text
        else:
            print("Failed to retrieve message from IPFS.")
            return None

# Example usage
if __name__ == "__main__":
    ipfs_comm = IPFSCommunication()
    message = "Hello, decentralized world!"
    hash = ipfs_comm.send_message(message)
    if hash:
        ipfs_comm.retrieve_message(hash)
import requests

class IPFSStorage:
    def __init__(self, api_url="http://127.0.0.1:5001"):
        self.api_url = api_url

    def upload_file(self, file_path):
        """Upload a file to IPFS."""
        with open(file_path, "rb") as file:
            response = requests.post(f"{self.api_url}/api/v0/add", files={"file": file})
            if response.status_code == 200:
                ipfs_hash = response.json()["Hash"]
                print(f"File uploaded to IPFS with hash: {ipfs_hash}")
                return ipfs_hash
            else:
                print("Failed to upload file to IPFS.")
                return None

    def retrieve_file(self, ipfs_hash, output_path):
        """Retrieve a file from IPFS."""
        response = requests.get(f"{self.api_url}/api/v0/cat?arg={ipfs_hash}")
        if response.status_code == 200:
            with open(output_path, "wb") as file:
                file.write(response.content)
            print(f"File retrieved from IPFS and saved to: {output_path}")
        else:
            print("Failed to retrieve file from IPFS.")

# Example usage
if __name__ == "__main__":
    ipfs = IPFSStorage()
    ipfs_hash = ipfs.upload_file("example.txt")
    if ipfs_hash:
        ipfs.retrieve_file(ipfs_hash, "retrieved_example.txt")
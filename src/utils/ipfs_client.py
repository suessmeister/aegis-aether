import requests


class IPFSClient:
    """Interacts with an IPFS node to upload and retrieve files."""

    def __init__(self, ipfs_api_url="http://localhost:5001/api/v0"):
        self.ipfs_api_url = ipfs_api_url

    def upload_file(self, file_path):
        """Upload a file to IPFS."""
        with open(file_path, "rb") as file:
            files = {"file": file}
            response = requests.post(f"{self.ipfs_api_url}/add", files=files)
            if response.status_code == 200:
                cid = response.json()["Hash"]
                print(f"File uploaded to IPFS with CID: {cid}")
                return cid
            else:
                print(f"Failed to upload file to IPFS: {response.text}")
                return None

    def retrieve_file(self, cid, output_path):
        """Retrieve a file from IPFS using its CID."""
        response = requests.get(f"{self.ipfs_api_url}/cat?arg={cid}")
        if response.status_code == 200:
            with open(output_path, "wb") as file:
                file.write(response.content)
            print(f"File retrieved from IPFS and saved to: {output_path}")
        else:
            print(f"Failed to retrieve file from IPFS: {response.text}")
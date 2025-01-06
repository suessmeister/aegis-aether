import src
import requests

gov_api_key = "LZ8uq7nPA7x8sSXzgsVZ18TVWQzaJAkNNGY8E3Kz"

url = "https://developer.nrel.gov/api/alt-fuel-stations/v1.json?"
params = {  # include parameters for query
    "api_key": gov_api_key,  
    "format": "json",  
    "limit": 1
    # other parameters as needed!
}

response = requests.get(url, params=params)

if response.status_code == 200:
    print("Success:", response.json())  # Print the API response
else:
    print("Error:", response.status_code, response.text)

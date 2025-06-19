"""
To test basic functionality, ie. what ARES returns

"""

import requests
import json

url = f"https://wwwinfo.mfcr.cz/ares/api/ekonomicke-subjekty/06635482"

response = requests.get(url, timeout=10)
json_data = response.json()

assert isinstance(json_data, dict), "Expected JSON object (dict)"
print("Test passed: response is a JSON object.")

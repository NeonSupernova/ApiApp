import requests
import json
response = requests.get("https://api.coindesk.com/v1/bpi/currentprice/USD.json")
print(response.status_code)

def dprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

bitcoinPrice = response.json()["bpi"]["USD"]["rate"]
dprint(bitcoinPrice)
if bitcoinPrice > "45000":
	print('sell')
else:
	print("buy")

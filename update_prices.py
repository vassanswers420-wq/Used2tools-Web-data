import requests
import json
from datetime import datetime
import os

API_KEY = os.getenv("TRADEWATCH_KEY")

headers = {"api-key": API_KEY}

crypto_url = "https://api.tradewatch.io/crypto/quotes?symbols=BTCUSD,XRPUSD"
commodities_url = "https://api.tradewatch.io/commodities/quotes?symbols=COPPER,GOLD,SILVER,NICKEL,ALUMINIUM"

prices = {}

# crypto
r = requests.get(crypto_url, headers=headers).json()["items"]
for c in r:
    if c["symbol"] == "BTCUSD":
        prices["btc"] = c["mid"]
    if c["symbol"] == "XRPUSD":
        prices["xrp"] = c["mid"]

# commodities
r = requests.get(commodities_url, headers=headers).json()["items"]
for c in r:
    prices[c["symbol"].lower()] = c["mid"]

data = {
    "updated": datetime.utcnow().isoformat(),
    "assets": prices
}

with open("data/prices.json", "w") as f:
    json.dump(data, f, indent=2)

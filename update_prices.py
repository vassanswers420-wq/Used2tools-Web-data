import requests
import json
from datetime import datetime
import os

API_KEY = os.getenv("TRADEWATCH_KEY")
headers = {"api-key": API_KEY}

# -------------------
# URLs
# -------------------
crypto_url = "https://api.tradewatch.io/crypto/quotes?symbols=BTCUSD,XRPUSD"

commodities_url = "https://api.tradewatch.io/commodities/quotes?symbols=COPPER,GOLD,SILVER,NICKEL,ALUMINIUM"

currency_url = "https://api.tradewatch.io/Currencies/quotes?symbols=AUDUSD,CNHUSD,INRUSD"

# -------------------
# Main Prices Object
# -------------------
prices = {}

# -------------------
# CRYPTO
# -------------------
r = requests.get(crypto_url, headers=headers).json()["items"]

for c in r:
    if c["symbol"] == "BTCUSD":
        prices["btc"] = c["mid"]
    if c["symbol"] == "XRPUSD":
        prices["xrp"] = c["mid"]

# -------------------
# COMMODITIES
# -------------------
r = requests.get(commodities_url, headers=headers).json()["items"]

for c in r:
    prices[c["symbol"].lower()] = c["mid"]

# -------------------
# CURRENCIES
# -------------------
r = requests.get(currency_url, headers=headers).json()["items"]

for c in r:
    prices[c["symbol"].lower()] = c["mid"]

# -------------------
# FINAL JSON
# -------------------
data = {
    "updated": datetime.utcnow().isoformat(),
    "assets": prices
}

with open("data/prices.json", "w") as f:
    json.dump(data, f, indent=2)

import os
import requests
import json
from datetime import datetime

# Use the new secret
API_KEY = os.environ.get("UPDATE_INSIDER")

url = "https://earningsfeed.com/api/v1/insider/transactions"

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

response = requests.get(url, headers=headers)
data = response.json()

# Save inside /data folder
with open("data/insider_transactions.json", "w") as f:
    json.dump(data, f, indent=4)

print("Data updated at", datetime.utcnow())

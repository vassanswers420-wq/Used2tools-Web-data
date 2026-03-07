import os
import requests
import json

API_KEY = os.environ.get("UPDATE_INSIDER")

url = "https://earningsfeed.com/api/v1/insider/transactions"

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

all_items = []
cursor = None

while True:
    params = {}
    if cursor:
        params["cursor"] = cursor

    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    all_items.extend(data.get("items", []))

    if not data.get("hasMore"):
        break

    cursor = data.get("nextCursor")

# Save cleaned structured file
output = {
    "lastUpdated": str(json.dumps(__import__("datetime").datetime.utcnow().isoformat())),
    "count": len(all_items),
    "items": all_items
}

with open("data/insider_transactions.json", "w") as f:
    json.dump(output, f, indent=4)

print("Insider data updated.")

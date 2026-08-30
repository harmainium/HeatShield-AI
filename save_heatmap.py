import requests
import json

api_key = input("Paste your FortyGuard API key: ")

activity_id = "b007004c-28bf-4b97-8d7a-744b06ab58b4"

url = f"https://api.fortyguard.com/v1/status/{activity_id}"

headers = {
    "api-key": api_key
}

response = requests.get(url, headers=headers)

result = response.json()

heatmap = result["data"]["result"]["map_data"]

with open("data/heatmap.geojson", "w", encoding="utf-8") as f:
    json.dump(heatmap, f, indent=2)

print("Heatmap saved successfully!")
print("Tiles:", len(heatmap["features"]))
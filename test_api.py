import requests

api_key = input("Paste your FortyGuard API key: ")

url = "https://api.fortyguard.com/v1/heatmap"

headers = {
    "api-key": api_key,
    "Content-Type": "application/json"
}

payload = {
    "polygon_aoi": {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "properties": {},
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[
                        [-74.09, 40.70],
                        [-74.05, 40.70],
                        [-74.05, 40.73],
                        [-74.09, 40.73],
                        [-74.09, 40.70]
                    ]]
                }
            }
        ]
    },
    "date_time": {
        "start_date": "2024-07-15",
        "start_time": "14:00",
        "filter_type": 1
    },
    "granularity": 100
}

response = requests.post(url, headers=headers, json=payload)

print(response.status_code)
print(response.text)
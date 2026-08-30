import json
from math import hypot

# Load our two GeoJSON files
with open("data/Public_Assets.Geojson", "r", encoding="utf-8") as f:
    assets = json.load(f)

with open("data/heatmap.geojson", "r", encoding="utf-8") as f:
    heatmap = json.load(f)

# Match each public asset to the nearest heatmap tile
for asset in assets["features"]:
    asset_lon, asset_lat = asset["geometry"]["coordinates"]

    nearest_tile = None
    nearest_distance = float("inf")

    for tile in heatmap["features"]:
        coords = tile["geometry"]["coordinates"][0]

        tile_lon = sum(point[0] for point in coords[:-1]) / 4
        tile_lat = sum(point[1] for point in coords[:-1]) / 4

        distance = hypot(asset_lon - tile_lon, asset_lat - tile_lat)

        if distance < nearest_distance:
            nearest_distance = distance
            nearest_tile = tile

    if nearest_tile:
        temp = nearest_tile["properties"]["average_temperature"]
        asset["properties"]["temperature_c"] = temp

        if temp >= 35:
            risk = "Extreme"
        elif temp >= 32:
            risk = "High"
        elif temp >= 30:
            risk = "Moderate"
        else:
            risk = "Low"

        asset["properties"]["heat_risk"] = risk

# Save the combined dataset
with open("data/heatshield_assets.geojson", "w", encoding="utf-8") as f:
    json.dump(assets, f, indent=2)

print("HeatShield asset dataset created successfully!")
print("Assets processed:", len(assets["features"]))
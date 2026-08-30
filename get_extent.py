import json

with open("data/Public_Assets.Geojson", "r", encoding="utf-8") as f:
    data = json.load(f)

coords = []

for feature in data["features"]:
    lon, lat = feature["geometry"]["coordinates"]
    coords.append((lon, lat))

lons = [x[0] for x in coords]
lats = [x[1] for x in coords]

print("Number of assets:", len(coords))
print("West:", min(lons))
print("East:", max(lons))
print("South:", min(lats))
print("North:", max(lats))
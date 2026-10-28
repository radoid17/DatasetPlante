import csv
from pathlib import Path
from datetime import date

import requests

# GBIF API: colectam observatii de plante doar din romania
API_URL = "https://api.gbif.org/v1/occurrence/search"

params = {
    "country": "RO",
    "kingdomKey": 6,
    "hasCoordinate": "true",
    "mediaType": "StillImage",
    "limit": 50,
    "offset": 0,
}

response = requests.get(API_URL, params=params, timeout=30)
response.raise_for_status()
data = response.json()

records = []

for item in data.get("results", []):
    media_list = item.get("media") or []
    image = next(
        (
            media for media in media_list
            if media.get("identifier")
        ),
        {},
    )

    scientific_name = item.get("scientificName")
    image_url = image.get("identifier")

    if not scientific_name or not image_url:
        continue

    gbif_id = item.get("gbifID")

    records.append({
        "record_id": f"PLANT_{gbif_id}",
        "scientific_name": scientific_name,
        "country": item.get("countryCode"),
        "latitude": item.get("decimalLatitude"),
        "longitude": item.get("decimalLongitude"),
        "observation_date": item.get("eventDate"),
        "image_url": image_url,
        "image_license": image.get("license"),
        "record_license": item.get("license"),
        "source_url": (
            f"https://www.gbif.org/occurrence/{gbif_id}"
            if gbif_id else ""
        ),
        "collection_date": date.today().isoformat(),
    })

project_dir = Path(__file__).resolve().parent.parent
output_file = project_dir / "data" / "sample.csv"
output_file.parent.mkdir(parents=True, exist_ok=True)

fieldnames = [
    "record_id",
    "scientific_name",
    "country",
    "latitude",
    "longitude",
    "observation_date",
    "image_url",
    "image_license",
    "record_license",
    "source_url",
    "collection_date",
]

with output_file.open("w", newline="", encoding="utf-8-sig") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(records)

print(f"Total colectat: {len(records)} înregistrări")
print(f"Fișier salvat: {output_file}")
print(f"Înregistrări găsite de GBIF: {data.get('count', 0)}")

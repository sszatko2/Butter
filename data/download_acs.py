"""
Download U.S. county housing/income data from the Census ACS 5-year API.

What it does:
- Downloads ACS 5-year county estimates for 2019 through 2024.
- Saves the original API responses as JSON and the tables as CSV.
- Keeps county/state FIPS codes as text to preserve leading zeros.
- Does not require an API key for most ordinary requests, but prompts for one if you have it.

Run:
    python download_acs.py

Install the dependency first if needed:
    python -m pip install requests
"""

import csv
import json
import time
from pathlib import Path
from getpass import getpass

import requests

YEARS = range(2019, 2025)
VARIABLES = [
    "NAME",
    "B19013_001E",  # Median household income
    "B25077_001E",  # Median value of owner-occupied housing units
    "B25064_001E",  # Median gross rent
]
BASE_URL = "https://api.census.gov/data/{year}/acs/acs5"
OUTPUT_DIR = Path("data") / "raw" / "acs"

def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    api_key = getpass("Census API key (press Enter to continue without one): ").strip()

    for year in YEARS:
        url = BASE_URL.format(year=year)
        params = {
            "get": ",".join(VARIABLES),
            "for": "county:*",
            "in": "state:*",
        }
        if api_key:
            params["key"] = api_key

        print(f"Downloading ACS {year} 5-year county data...")
        response = requests.get(url, params=params, timeout=60)
        response.raise_for_status()

        # Save untouched API response for provenance/reproducibility.
        json_path = OUTPUT_DIR / f"acs5_county_{year}_raw.json"
        json_path.write_text(response.text, encoding="utf-8")

        rows = response.json()
        if not rows or len(rows) < 2:
            raise RuntimeError(f"No county data returned for {year}. Check the API response.")

        headers = rows[0]
        csv_path = OUTPUT_DIR / f"acs5_county_{year}.csv"
        with csv_path.open("w", newline="", encoding="utf-8-sig") as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            writer.writerows(rows[1:])

        print(f"  Saved {len(rows) - 1:,} records to {csv_path}")
        print(f"  Saved original response to {json_path}")
        time.sleep(0.2)

    print("\nDone. Your files are in data/raw/acs/")
    print("Keep these raw files unchanged; do cleaning and integration in separate steps.")

if __name__ == "__main__":
    main()

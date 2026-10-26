"""
ClinicalTrials.gov & OpenFDA Biotech / Pharma Lead Enricher — Python Quickstart
Official Apify Store Actor: https://apify.com/lucacelli/clinical-trials-fda-drug-safety-intel ($0.80 / 1,000 trials)
"""
import os
import requests

APIFY_TOKEN = os.getenv("APIFY_TOKEN", "YOUR_APIFY_TOKEN")
ENDPOINT = "https://api.apify.com/v2/acts/lucacelli~clinical-trials-fda-drug-safety-intel/run-sync-get-dataset-items"

payload = {
    "conditions": [
        "oncology",
        "diabetes"
    ],
    "maxTrials": 50
}

if __name__ == "__main__":
    print(f"Running ClinicalTrials.gov & OpenFDA Biotech / Pharma Lead Enricher on Apify Cloud ({ENDPOINT})...")
    response = requests.post(f"{ENDPOINT}?token={APIFY_TOKEN}", json=payload, timeout=300)
    response.raise_for_status()
    data = response.json()
    print(f"Extracted {len(data)} records! Sample:")
    print(data[:3])

"""
ClinicalTrials.gov & OpenFDA Biotech / Pharma Lead Enricher — LangChain, CrewAI & OpenAI Assistants Tool
Official Apify Actor: https://apify.com/lucacelli/clinical-trials-fda-drug-safety-intel ($0.80 / 1,000 trials)
"""
import os
import requests
from typing import Dict, Any, List

APIFY_TOKEN = os.getenv("APIFY_TOKEN", "YOUR_APIFY_TOKEN")
ENDPOINT = "https://api.apify.com/v2/acts/lucacelli~clinical-trials-fda-drug-safety-intel/run-sync-get-dataset-items"

def run_clinical_trials_fda_drug_safety_intel(custom_input: Dict[str, Any] = None) -> List[Dict[str, Any]]:
    """
    Executes ClinicalTrials.gov & OpenFDA Biotech / Pharma Lead Enricher on Apify Cloud ($0.80/1k trials).
    Query ClinicalTrials.gov API v2 and OpenFDA to extract active clinical trials, biotech/pharma sponsors, principal investigator contacts, trial phases, and FDA regulatory intelligence.
    """
    default_payload = {
    "conditions": [
        "oncology",
        "diabetes"
    ],
    "maxTrials": 50
}
    payload = custom_input if custom_input else default_payload
    res = requests.post(f"{ENDPOINT}?token={APIFY_TOKEN}", json=payload, timeout=300)
    res.raise_for_status()
    return res.json()

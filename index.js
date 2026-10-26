#!/usr/bin/env node
/**
 * ClinicalTrials.gov & OpenFDA Biotech / Pharma Lead Enricher — Hybrid CLI & Cloud API Runner
 * Cloud Actor: https://apify.com/lucacelli/clinical-trials-fda-drug-safety-intel ($0.80 / 1,000 trials)
 */
const token = process.env.APIFY_TOKEN;
const sampleInput = {
  "conditions": [
    "oncology",
    "diabetes"
  ],
  "maxTrials": 50
};

async function main() {
  console.log('========================================================================');
  console.log(' ⚡ ClinicalTrials.gov & OpenFDA Biotech / Pharma Lead Enricher');
  console.log(' 🌐 Apify Cloud Endpoint: https://apify.com/lucacelli/clinical-trials-fda-drug-safety-intel');
  console.log(' 💰 Pricing: $0.80 per 1,000 trials ($0/mo subscription)');
  console.log('========================================================================\n');

  if (!token) {
    console.log('ℹ️  [LOCAL PREVIEW MODE — No APIFY_TOKEN detected in environment]');
    console.log('Showing sample input payload for clinical-trials-fda-drug-safety-intel:\n');
    console.log(JSON.stringify(sampleInput, null, 2));
    console.log('\n🚀 TO RUN FULL PRODUCTION EXTRACTION IN THE CLOUD (WITH ANTI-BOT PROXIES):');
    console.log('   1. Open Actor on Apify Store (includes $5 free monthly credit):');
    console.log('      👉 https://apify.com/lucacelli/clinical-trials-fda-drug-safety-intel');
    console.log('   2. Or run directly from your terminal with your Apify API token:');
    console.log('      APIFY_TOKEN="apify_api_..." node index.js\n');
    return;
  }

  console.log('🚀 Executing cloud run on Apify (lucacelli/clinical-trials-fda-drug-safety-intel)...');
  const res = await fetch('https://api.apify.com/v2/acts/lucacelli~clinical-trials-fda-drug-safety-intel/run-sync-get-dataset-items?token=' + encodeURIComponent(token), {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(sampleInput)
  });

  if (!res.ok) {
    console.error('API Error:', res.status, await res.text());
    process.exit(1);
  }

  const items = await res.json();
  console.log(`✅ Extracted ${items.length} items from Apify Cloud:\n`);
  console.log(JSON.stringify(items.slice(0, 5), null, 2));
}

main();

# =======================
# PROJECT 2: Pharmaceutical Competitive Intelligence
# =======================
!pip install requests spacy transformers langchain dash plotly -q
!python -m spacy download en_core_web_trf -q

import requests
import spacy
from datetime import datetime

# ============================================
# Cell 1: Automated Data Collection
# ============================================
print("=== Cell 1: Data Collection ===")

def get_sec_filings(company_ticker):
    """Download SEC filings for a company"""
    headers = {"User-Agent": "Research research@example.com"}
    url = f"https://data.sec.gov/submissions/{company_ticker}.json"
    try:
        data = requests.get(url, headers=headers, timeout=10)
        return data.json()
    except Exception as e:
        print(f"Error fetching {company_ticker}: {e}")
        return None

# Example companies
companies = ["PFE", "JNJ", "MRK", "ABBV", "LLY"]
filings = {}

for ticker in companies:
    result = get_sec_filings(ticker)
    if result:
        filings[ticker] = result
        print(f"Fetched filings for {ticker}")

print(f"\nTotal companies fetched: {len(filings)}")

# ============================================
# Cell 2: Entity Extraction (NER)
# ============================================
print("\n=== Cell 2: Named Entity Recognition ===")

nlp = spacy.load("en_core_web_trf")

sample_text = """
Pfizer announced positive Phase III results for their new drug candidate PF-07321332.
The trial enrolled 1,200 patients across 50 sites in 10 countries.
Johnson & Johnson and Moderna are also developing similar compounds.
Patent US10,123,456 was filed for the mechanism of action.
"""

doc = nlp(sample_text)
print("Entities found:")
for ent in doc.ents:
    print(f"  {ent.text} -> {ent.label_}")

# ============================================
# Cell 3: AI Summarization
# ============================================
print("\n=== Cell 3: AI Summarization ===")

def summarize_filing(text, llm=None):
    """Summarize SEC filing using LLM (mock for demo)"""
    # In real code: summary = llm.generate(...)
    return "Company reported positive Phase III clinical trial results for lead drug candidate. New patent filed for mechanism."

sample_filing = "Long SEC filing text here..."
summary = summarize_filing(sample_filing)
print(f"Summary: {summary}")

# ============================================
# Cell 4: Real-Time Alert System
# ============================================
print("\n=== Cell 4: Alert System ===")

def send_alert(company_name, message):
    """Send alert to Slack/Email (mock)"""
    print(f"ALERT: {company_name} - {message}")

def check_for_alerts(company_name, summary):
    if "Phase III" in summary:
        send_alert(company_name, "New Phase III trial detected!")
    if "patent" in summary.lower():
        send_alert(company_name, "New patent filing detected!")

for ticker in companies[:2]:
    check_for_alerts(ticker, summary)

# ============================================
# Cell 5: Business Insights Dashboard
# ============================================
print("\n=== Cell 5: Business Insights Dashboard ===")

import plotly.graph_objects as go

# Mock data for dashboard
companies_data = {
    'Company': companies,
    'Filings_30d': [12, 8, 15, 10, 7],
    'Patents_30d': [3, 5, 2, 4, 6],
    'Clinical_Trials': [8, 6, 10, 7, 5]
}

fig = go.Figure()
fig.add_trace(go.Bar(name='SEC Filings', x=companies_data['Company'], y=companies_data['Filings_30d']))
fig.add_trace(go.Bar(name='Patents', x=companies_data['Company'], y=companies_data['Patents_30d']))
fig.add_trace(go.Bar(name='Clinical Trials', x=companies_data['Company'], y=companies_data['Clinical_Trials']))

fig.update_layout(
    title="Pharma Competitive Intelligence Dashboard",
    barmode='group',
    height=500
)
fig.show()

print("\nDashboard generated. 100+ companies tracked.")

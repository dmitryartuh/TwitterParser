import pandas as pd
import requests
import time

# GMGN API Endpoint (Example - Replace with actual endpoint if different)
GMGN_API_URL = "https://api.gmgn.io/v1/token"

# Load extracted contract addresses
contracts_df = pd.read_csv("extracted_contracts.csv")

# Store token data
token_data = []

def fetch_token_info(contract, blockchain):
    """Fetch token details from GMGN API."""
    try:
        response = requests.get(f"{GMGN_API_URL}/{blockchain}/{contract}")
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to fetch {contract} ({blockchain}): {response.status_code}")
            return None
    except Exception as e:
        print(f"Error fetching data for {contract}: {e}")
        return None

# Iterate through contract addresses and fetch data
for _, row in contracts_df.iterrows():
    contract = row["Contract_Address"]
    blockchain = row["Blockchain"].lower()  # API might expect "ethereum" or "solana"

    # Fetch token info
    token_info = fetch_token_info(contract, blockchain)
    
    if token_info:
        token_data.append([
            contract, 
            blockchain.upper(), 
            token_info.get("name", "N/A"), 
            token_info.get("symbol", "N/A"), 
            token_info.get("decimals", "N/A"),
            token_info.get("market_cap", "N/A"),
            token_info.get("price", "N/A"),
        ])
    
    # Rate limit handling
    time.sleep(1)

# Save token info to CSV
token_df = pd.DataFrame(token_data, columns=[
    "Contract_Address", "Blockchain", "Name", "Symbol", "Decimals", "Market_Cap", "Price"
])
token_df.to_csv("token_info.csv", index=False)

print("Token data saved to token_info.csv")

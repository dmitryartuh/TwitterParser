import pandas as pd
import re

# Load tweets from CSV
df = pd.read_csv("tweets_last_24h.csv")

# Regex patterns for Ethereum and Solana contract addresses
ETH_CONTRACT_REGEX = r"0x[a-fA-F0-9]{40}"
SOL_CONTRACT_REGEX = r"[1-9A-HJ-NP-Za-km-z]{32,44}"

def extract_contracts(text):
    """Extract Ethereum and Solana contract addresses from text."""
    eth_matches = re.findall(ETH_CONTRACT_REGEX, text)
    sol_matches = re.findall(SOL_CONTRACT_REGEX, text)
    return eth_matches, sol_matches

# Create a new dataframe to store extracted contracts
contracts_data = []

# Iterate through tweets and extract contract addresses
for _, row in df.iterrows():
    eth_addresses, sol_addresses = extract_contracts(row["Text"])
    for eth in eth_addresses:
        contracts_data.append([row["Tweet_ID"], row["User_ID"], "ETH", eth])
    for sol in sol_addresses:
        contracts_data.append([row["Tweet_ID"], row["User_ID"], "SOL", sol])

# Save extracted contracts to a new CSV file
contracts_df = pd.DataFrame(contracts_data, columns=["Tweet_ID", "User_ID", "Blockchain", "Contract_Address"])
contracts_df.to_csv("extracted_contracts.csv", index=False)

print("Extracted contract addresses saved to extracted_contracts.csv")

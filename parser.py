import pandas as pd
import re

df = pd.read_csv("tweets_last_24h.csv")

ETH_CONTRACT_REGEX = r"0x[a-fA-F0-9]{40}"
SOL_CONTRACT_REGEX = r"[1-9A-HJ-NP-Za-km-z]{32,44}"

def extract_contracts(text):
    eth_matches = re.findall(ETH_CONTRACT_REGEX, text)
    sol_matches = re.findall(SOL_CONTRACT_REGEX, text)
    return eth_matches, sol_matches

contracts_data = []

for _, row in df.iterrows():
    text = row["Text"]
    if pd.isnull(text):
        continue
    eth_addresses, sol_addresses = extract_contracts(text)
    for eth in eth_addresses:
        contracts_data.append([row["Tweet_ID"], row["User_ID"], "ETH", eth])
    for sol in sol_addresses:
        contracts_data.append([row["Tweet_ID"], row["User_ID"], "SOL", sol])

contracts_df = pd.DataFrame(contracts_data, columns=["Tweet_ID", "User_ID", "Blockchain", "Contract_Address"])
contracts_df.to_csv("extracted_contracts.csv", index=False)

print("Extracted contract addresses saved to extracted_contracts.csv")

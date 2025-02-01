# Twitter Token Parser

This project automates fetching tweets from your Twitter subscriptions, extracting Ethereum (ETH) and Solana (SOL) token contract addresses, and retrieving token information using the GMGN API.

## Features
- Fetches tweets from followed accounts in the last 24 hours.
- Extracts ETH and SOL contract addresses from tweet text.
- Retrieves token information (name, symbol, price, etc.) via GMGN API.
- Saves all extracted data to CSV files.
- Fully automated workflow with `run_pipeline.py`.

## Project Structure
```
├── main.py        # Fetch tweets from Twitter API
├── parser.py      # Extract contract addresses from tweets
├── load-info.py   # Fetch token data from GMGN API
├── run_pipeline.py # Runs the full workflow
├── requirements.txt # Required dependencies
├── README.md      # Project documentation
```

## Installation
### Prerequisites
- Python 3.7+
- Twitter API credentials (Bearer Token)
- GMGN API access

### Install Dependencies
```bash
pip install -r requirements.txt
```

## Usage
Run the entire workflow with:
```bash
python run_pipeline.py
```

Or run individual scripts manually:
```bash
python main.py       # Fetch tweets
python parser.py     # Extract contract addresses
python load-info.py  # Fetch token info
```

## Output Files
- `tweets_last_24h.csv` – Raw tweets fetched from Twitter.
- `extracted_contracts.csv` – Extracted ETH & SOL contract addresses.
- `token_info.csv` – Token details fetched from GMGN API.

## Configuration
Edit `main.py` to set your **Twitter API credentials**:
```python
BEARER_TOKEN = "your_bearer_token"
```

## License
MIT License

## Contributions
Feel free to submit pull requests or report issues!

## Contact
For any questions, reach out via GitHub Issues.


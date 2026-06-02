import requests
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

output_dir = BASE_DIR / "data" / "raw"

url = "https://api.mfapi.in/mf/125497"

response = requests.get(url)

print("Status Code:", response.status_code)

data = response.json()

df = pd.DataFrame(data["data"])

output_file = output_dir / "hdfc_top100_live_nav.csv"

df.to_csv(output_file, index=False)

print(f"Saved: {output_file}")
print(df.head())
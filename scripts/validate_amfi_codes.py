import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

fund_master = pd.read_csv(
    BASE_DIR / "data/raw/01_fund_master.csv"
)

nav_history = pd.read_csv(
    BASE_DIR / "data/raw/02_nav_history.csv"
)

master_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

missing_codes = master_codes - nav_codes

print("Missing Codes:", len(missing_codes))

if len(missing_codes) > 0:
    print(missing_codes)
else:
    print("All AMFI codes validated successfully.")
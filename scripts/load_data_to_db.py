import sqlite3
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

db_file = BASE_DIR / "data" / "db" / "bluestock_mf.db"

conn = sqlite3.connect(db_file)

print("Loading fund_master...")

fund_master = pd.read_csv(
    BASE_DIR / "data" / "raw" / "01_fund_master.csv"
)

fund_master.to_sql(
    "fund_master",
    conn,
    if_exists="replace",
    index=False
)

print(f"Loaded {len(fund_master):,} rows")


print("Loading nav_history...")

nav_history = pd.read_csv(
    BASE_DIR / "data" / "processed" / "clean_nav_history_filled.csv"
)

nav_history.rename(
    columns={"date": "nav_date"},
    inplace=True
)

nav_history.to_sql(
    "nav_history",
    conn,
    if_exists="replace",
    index=False
)

print(f"Loaded {len(nav_history):,} rows")


print("Loading investor_transactions...")

transactions = pd.read_csv(
    BASE_DIR / "data" / "processed" / "clean_transactions.csv"
)

transactions.to_sql(
    "investor_transactions",
    conn,
    if_exists="replace",
    index=False
)

print(f"Loaded {len(transactions):,} rows")


print("Loading scheme_performance...")

performance = pd.read_csv(
    BASE_DIR / "data" / "raw" / "07_scheme_performance.csv"
)

performance.to_sql(
    "scheme_performance",
    conn,
    if_exists="replace",
    index=False
)

print(f"Loaded {len(performance):,} rows")


print("\nAll tables loaded successfully.")

conn.close()
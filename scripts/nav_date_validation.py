import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

file_path = BASE_DIR / "data" / "processed" / "clean_nav_history.csv"

df = pd.read_csv(file_path)

df["date"] = pd.to_datetime(df["date"])

scheme = df["amfi_code"].iloc[0]

sample = df[df["amfi_code"] == scheme].copy()

full_dates = pd.date_range(
    sample["date"].min(),
    sample["date"].max(),
    freq="D"
)

missing_dates = len(full_dates) - len(sample)

print("AMFI Code:", scheme)
print("Available Dates:", len(sample))
print("Expected Dates:", len(full_dates))
print("Missing Dates:", missing_dates)
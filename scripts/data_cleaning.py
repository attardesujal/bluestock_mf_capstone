import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

raw_file = BASE_DIR / "data" / "raw" / "02_nav_history.csv"
output_file = BASE_DIR / "data" / "processed" / "clean_nav_history.csv"

df = pd.read_csv(raw_file)

print("Original Shape:", df.shape)

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# Remove duplicates
duplicate_count = df.duplicated().sum()
print("Duplicates Found:", duplicate_count)

df = df.drop_duplicates()

# Remove invalid NAV values
invalid_nav = (df["nav"] <= 0).sum()
print("Invalid NAV Rows:", invalid_nav)

df = df[df["nav"] > 0]

# Sort values
df = df.sort_values(
    by=["amfi_code", "date"]
)

print("Clean Shape:", df.shape)

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

df.to_csv(output_file, index=False)

print(f"\nSaved Clean File: {output_file}")
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

input_file = BASE_DIR / "data/raw/08_investor_transactions.csv"
output_file = BASE_DIR / "data/processed/clean_transactions.csv"

df = pd.read_csv(input_file)

print("Original Shape:", df.shape)

# Convert date
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"],
    errors="coerce"
)

# Duplicate check
duplicates = df.duplicated().sum()
print("Duplicates:", duplicates)

# Remove duplicates
df = df.drop_duplicates()

# Validate amount
invalid_amounts = (df["amount_inr"] <= 0).sum()
print("Invalid Amount Rows:", invalid_amounts)

df = df[df["amount_inr"] > 0]

# Transaction types
print("\nTransaction Types:")
print(df["transaction_type"].value_counts())

# KYC Status
print("\nKYC Status:")
print(df["kyc_status"].value_counts())

print("\nClean Shape:", df.shape)

df.to_csv(
    output_file,
    index=False
)

print("\nSaved:", output_file)
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data" / "raw"

csv_files = sorted(DATA_DIR.glob("*.csv"))

print(f"\nFound {len(csv_files)} CSV files\n")

print(DATA_DIR)

for file in csv_files:
    print("=" * 80)
    print(f"Dataset: {file.name}")

    df = pd.read_csv(file)

    print("Shape:", df.shape)
    print(df.head())
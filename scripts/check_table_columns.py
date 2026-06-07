import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

files = [
    "01_fund_master.csv",
    "07_scheme_performance.csv"
]

for file in files:
    print("\n" + "=" * 80)
    print(file)

    df = pd.read_csv(
        BASE_DIR / "data/raw" / file
    )

    print(df.columns.tolist())
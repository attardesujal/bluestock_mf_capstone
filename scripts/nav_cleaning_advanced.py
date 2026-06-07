import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

input_file = BASE_DIR / "data" / "processed" / "clean_nav_history.csv"
output_file = BASE_DIR / "data" / "processed" / "clean_nav_history_filled.csv"

df = pd.read_csv(input_file)

df["date"] = pd.to_datetime(df["date"])

all_funds = []

for amfi_code, group in df.groupby("amfi_code"):

    group = group.sort_values("date")

    full_dates = pd.date_range(
        start=group["date"].min(),
        end=group["date"].max(),
        freq="D"
    )

    group = (
        group
        .set_index("date")
        .reindex(full_dates)
    )

    group["amfi_code"] = amfi_code

    # Forward fill NAV
    group["nav"] = group["nav"].ffill()

    group = group.reset_index()

    group.rename(
        columns={"index": "date"},
        inplace=True
    )

    all_funds.append(group)

final_df = pd.concat(
    all_funds,
    ignore_index=True
)

print("Original Rows:", len(df))
print("Final Rows:", len(final_df))

final_df.to_csv(
    output_file,
    index=False
)

print("Saved:", output_file)
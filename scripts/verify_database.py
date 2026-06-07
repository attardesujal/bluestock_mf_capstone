import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

db_file = BASE_DIR / "data" / "db" / "bluestock_mf.db"

conn = sqlite3.connect(db_file)

cursor = conn.cursor()

tables = [
    "fund_master",
    "nav_history",
    "investor_transactions",
    "scheme_performance"
]

for table in tables:
    cursor.execute(
        f"SELECT COUNT(*) FROM {table}"
    )

    count = cursor.fetchone()[0]

    print(f"{table}: {count:,} rows")

conn.close()
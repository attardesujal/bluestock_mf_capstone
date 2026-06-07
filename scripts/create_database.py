import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

db_dir = BASE_DIR / "data" / "db"
db_dir.mkdir(exist_ok=True)

db_file = db_dir / "bluestock_mf.db"

schema_file = BASE_DIR / "sql" / "schema.sql"

conn = sqlite3.connect(db_file)

with open(schema_file, "r") as f:
    conn.executescript(f.read())

conn.commit()
conn.close()

print("Database created successfully.")
print(db_file)
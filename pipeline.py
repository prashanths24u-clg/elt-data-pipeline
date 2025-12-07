import pandas as pd
import sqlite3
from pathlib import Path

# Paths
DATA_PATH = Path("data/customers_raw.csv")
DB_PATH = Path("warehouse.db")

def extract() -> pd.DataFrame:
    """Extract raw CSV data into pandas DataFrame."""
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"CSV file not found at {DATA_PATH}")
    
    df = pd.read_csv(DATA_PATH)
    print(f"[EXTRACT] Loaded {len(df)} rows from {DATA_PATH}")
    return df


def load(df: pd.DataFrame) -> None:
    """Load DataFrame into SQLite table (simulates warehouse load)."""
    conn = sqlite3.connect(DB_PATH)
    
    df.to_sql("customers_raw", conn, if_exists="replace", index=False)
    
    conn.commit()
    conn.close()
    print(f"[LOAD] Data loaded into table 'customers_raw' in {DB_PATH}")


def transform() -> None:
    """Transform data inside SQLite warehouse using SQL."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS customers_cleaned;")

    transform_sql = """
    CREATE TABLE customers_cleaned AS
    WITH cleaned AS (
        SELECT
            id,
            TRIM(LOWER(name)) AS name,
            email,
            UPPER(country) AS country,
            created_at
        FROM customers_raw
        WHERE email IS NOT NULL
    )
    SELECT *
    FROM cleaned
    GROUP BY email;
    """

    cursor.executescript(transform_sql)
    conn.commit()

    print("[TRANSFORM] Created 'customers_cleaned' table. Preview:")
    rows = cursor.execute("SELECT * FROM customers_cleaned LIMIT 5;").fetchall()
    for r in rows:
        print(r)

    conn.close()


def main():
    df = extract()
    load(df)
    transform()
    print("[PIPELINE] ELT Pipeline executed successfully.")


if __name__ == "__main__":
    main()



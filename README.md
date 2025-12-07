# elt-data-pipeline

ELT Data Pipeline using Python & SQL (Ongoing)
This project implements an end-to-end ELT data pipeline, inspired by modern warehouse systems like Snowflake and Databricks.

Extract: Read raw CSV data

Load: Store into a local SQLite warehouse

Transform: Clean & model data using SQL (CTEs, joins, window functions)

Tools Used: Python, SQL, Pandas


After running `python pipeline.py`, the ETL pipeline produces:

[EXTRACT] Loaded 5 rows from data/customers_raw.csv  
[LOAD] Data loaded into table 'customers_raw' in warehouse.db  
[TRANSFORM] Created 'customers_cleaned' table. Preview:
(id, name, email, country, created_at)
[EXTRACT] Loaded 5 rows from data\customers_raw.csv
[LOAD] Data loaded into table 'customers_raw' in warehouse.db
[TRANSFORM] Created 'customers_cleaned' table. Preview:
(1, 'alice', 'alice@gmail.com', 'INDIA', '2024-01-01')
(2, 'bob', 'bob@gmail.com', 'IN', '2024-01-05')
PS C:\Users\praka\Desktop\p1\elt-data-pipeline-main> python pipeline.py
>>
[EXTRACT] Loaded 5 rows from data\customers_raw.csv
[LOAD] Data loaded into table 'customers_raw' in warehouse.db
[TRANSFORM] Created 'customers_cleaned' table. Preview:
(1, 'alice', 'alice@gmail.com', 'INDIA', '2024-01-01')
(2, 'bob', 'bob@gmail.com', 'IN', '2024-01-05')
[EXTRACT] Loaded 5 rows from data\customers_raw.csv
[LOAD] Data loaded into table 'customers_raw' in warehouse.db
[TRANSFORM] Created 'customers_cleaned' table. Preview:
(1, 'alice', 'alice@gmail.com', 'INDIA', '2024-01-01')
(2, 'bob', 'bob@gmail.com', 'IN', '2024-01-05')
[LOAD] Data loaded into table 'customers_raw' in warehouse.db
[TRANSFORM] Created 'customers_cleaned' table. Preview:
(1, 'alice', 'alice@gmail.com', 'INDIA', '2024-01-01')
(2, 'bob', 'bob@gmail.com', 'IN', '2024-01-05')
[TRANSFORM] Created 'customers_cleaned' table. Preview:
(1, 'alice', 'alice@gmail.com', 'INDIA', '2024-01-01')
(2, 'bob', 'bob@gmail.com', 'IN', '2024-01-05')
(4, 'david', 'david@gmail.com', 'UNITED STATES', '2024-01-15')
(1, 'alice', 'alice@gmail.com', 'INDIA', '2024-01-01')
(2, 'bob', 'bob@gmail.com', 'IN', '2024-01-05')
(4, 'david', 'david@gmail.com', 'UNITED STATES', '2024-01-15')
(2, 'bob', 'bob@gmail.com', 'IN', '2024-01-05')
(4, 'david', 'david@gmail.com', 'UNITED STATES', '2024-01-15')
(4, 'david', 'david@gmail.com', 'UNITED STATES', '2024-01-15')
[PIPELINE] ELT Pipeline executed successfully.


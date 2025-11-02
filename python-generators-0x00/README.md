# Python Generators Project - Task 0

## Overview
This project demonstrates the use of Python generators to stream rows from a MySQL database in a memory-efficient way. The script `seed.py` sets up the database, creates a table, inserts sample data from `user_data.csv`, and provides a generator to iterate through the table rows.

## Files
- `seed.py` - Python script to create the database, table, insert data, and provide a generator.
- `user_data.csv` - Sample CSV file with user data.
- `README.md` - Project description and instructions.

## Functions
- `connect_db()` - Connects to MySQL server (without a database).
- `create_database(connection)` - Creates `ALX_prodev` database if it does not exist.
- `connect_to_prodev()` - Connects to the `ALX_prodev` database.
- `create_table(connection)` - Creates `user_data` table if it does not exist.
- `insert_data(connection, csv_file)` - Inserts data from CSV into the table.
- `stream_rows(connection)` - Generator that yields one row at a time.

## Usage
1. Ensure MySQL server is running and update `DB_PASSWORD` in `seed.py`.
2. Place `user_data.csv` in the same directory.
3. Run the script:
```bash
./seed.py

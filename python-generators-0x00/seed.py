#!/usr/bin/python3
import mysql.connector
import csv
import uuid

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = 'your_password'  # replace with your MySQL root password
DB_NAME = 'ALX_prodev'
TABLE_NAME = 'user_data'


def connect_db():
    """Connect to MySQL server (without specifying a database)"""
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None


def create_database(connection):
    """Create database ALX_prodev if it does not exist"""
    try:
        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME};")
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Failed creating database: {err}")


def connect_to_prodev():
    """Connect to the ALX_prodev database"""
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error connecting to {DB_NAME}: {err}")
        return None


def create_table(connection):
    """Create user_data table if it does not exist"""
    try:
        cursor = connection.cursor()
        cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
                user_id CHAR(36) PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                age DECIMAL NOT NULL
            );
        """)
        print(f"Table {TABLE_NAME} created successfully")
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Failed creating table: {err}")


def insert_data(connection, csv_file):
    """Insert data from CSV into user_data table"""
    try:
        cursor = connection.cursor()
        with open(csv_file, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Ensure unique user_id
                user_id = str(uuid.uuid4())
                cursor.execute(f"""
                    INSERT INTO {TABLE_NAME} (user_id, name, email, age)
                    VALUES (%s, %s, %s, %s)
                """, (user_id, row['name'], row['email'], row['age']))
        connection.commit()
        cursor.close()
    except Exception as err:
        print(f"Error inserting data: {err}")


# Optional: generator to stream rows one by one
def stream_rows(connection):
    """Generator that yields one row at a time from user_data"""
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {TABLE_NAME};")
    for row in cursor:
        yield row
    cursor.close()


if __name__ == "__main__":
    conn = connect_db()
    if conn:
        create_database(conn)
        conn.close()
        print("Connection successful")

        conn = connect_to_prodev()
        if conn:
            create_table(conn)
            insert_data(conn, 'user_data.csv')

            print("First 5 rows from generator:")
            gen = stream_rows(conn)
            for _ in range(5):
                print(next(gen))

            conn.close()

#!/usr/bin/python3
import mysql.connector

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = 'your_password'  # عدل الباسورد هنا
DB_NAME = 'ALX_prodev'
TABLE_NAME = 'user_data'


def stream_users_in_batches(batch_size):
    """Generator to fetch rows in batches from user_data"""
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        cursor = connection.cursor(dictionary=True)
        offset = 0
        while True:
            cursor.execute(f"SELECT * FROM {TABLE_NAME} LIMIT {batch_size} OFFSET {offset};")
            batch = cursor.fetchall()
            if not batch:
                break
            for row in batch:
                yield row
            offset += batch_size
        cursor.close()
        connection.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")


def batch_processing(batch_size):
    """Process each batch and filter users over age 25"""
    users_generator = stream_users_in_batches(batch_size)
    for user in users_generator:
        if user['age'] > 25:
            print(user)

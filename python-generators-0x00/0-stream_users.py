#!/usr/bin/python3
import mysql.connector

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = 'your_password'  # عدل الباسورد هنا
DB_NAME = 'ALX_prodev'
TABLE_NAME = 'user_data'


def stream_users():
    """Generator that streams rows from user_data table one by one"""
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        cursor = connection.cursor(dictionary=True)
        cursor.execute(f"SELECT * FROM {TABLE_NAME};")
        for row in cursor:
            yield row
        cursor.close()
        connection.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")

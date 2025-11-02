#!/usr/bin/python3
seed = __import__('seed')


def stream_user_ages():
    """Generator that yields user ages one by one"""
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT age FROM user_data;")
    for row in cursor:
        yield row['age']
    cursor.close()
    connection.close()


def calculate_average_age():
    """Calculate average age using generator without loading all data"""
    total = 0
    count = 0
    for age in stream_user_ages():  # loop 1
        total += age
        count += 1
    if count == 0:
        print("No users found.")
        return
    average = total / count
    print(f"Average age of users: {average}")


if __name__ == "__main__":
    calculate_average_age()

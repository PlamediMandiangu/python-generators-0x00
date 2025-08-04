#!/usr/bin/python3

seed = __import__('seed')

# Step 1: Connect to MySQL server
connection = seed.connect_db()
if connection:
    seed.create_database(connection)
    connection.close()
    print("connection successful")

    # Step 2: Connect to ALX_prodev
    connection = seed.connect_to_prodev()

    if connection:
        seed.create_table(connection)
        seed.insert_data(connection, 'user_data.csv')

        # Step 3: Confirm database exists
        cursor = connection.cursor()
        cursor.execute(
            "SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = 'ALX_prodev';")
        result = cursor.fetchone()
        if result:
            print("Database ALX_prodev is present")

        # Step 4: Use generator to stream rows
        print("\nStreaming user_data one row at a time:")
        for row in seed.stream_user_data(connection):
            print(row)

        cursor.close()

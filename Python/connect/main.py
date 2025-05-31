import psycopg2

# Database connection parameters
db_params = {
    "dbname": "dvdrental",
    "user": "postgres",
    "password": "1234",
    "host": "localhost",
    "port": "5432"  # Default PostgreSQL port
}

try:
    # Establish connection
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()

    # Execute query
    cursor.execute("SELECT FIRST_NAME, LAST_NAME FROM CUSTOMER WHERE ACTIVE = 0;")

    # Fetch and display results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close cursor and connection
    cursor.close()
    conn.close()

except psycopg2.Error as e:
    print("Error connecting to PostgreSQL:", e)

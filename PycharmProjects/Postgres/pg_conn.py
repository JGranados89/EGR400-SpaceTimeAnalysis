import psycopg2
from psycopg2 import Error
try:
    connection = psycopg2.connect(user = "postgres",
                                  password = "wed37dyy2410",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "space_time_app")

    cursor = connection.cursor()
    # Print PostgreSQL Connection Properties
    print(connection.get_dsn_parameters(), "\n")

    # Print PostgreSQL Version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to -", record, "\n")

except(Exception, psycopg2.Error) as error :
    print("Error while connecting to PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")


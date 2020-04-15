import psycopg2
from psycopg2 import Error

try:
    connection = psycopg2.connect(user = "postgres",
                                  password = "wed37dyy2410",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "space_time_app")

    cursor = connection.cursor()

    create_table_query = '''CREATE TABLE time
            (ID INT PRIMARY KEY     NOT NULL,
            LOCATION        TEXT    NOT NULL,
            LATITUDE     INT     NOT NULL); '''

    cursor.execute(create_table_query)
    connection.commit()
    print("Table created successfully in space_time_app")

except(Exception, psycopg2.DatabaseError) as error:
    print("Error while creating table", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

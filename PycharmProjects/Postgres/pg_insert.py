import psycopg2
from psycopg2 import Error


def multiple_insert(records):
    try:
        connection = psycopg2.connect(user = "postgres",
                                      password = "wed37dyy2410",
                                      host = "127.0.0.1",
                                      port = "5432",
                                      database = "space_time_app")

        cursor = connection.cursor()
        postgres_insert_query = """ INSERT INTO time (ID, LOCATION, LATITUDE) 
        VALUES  (%s,%s,%s)"""

        result = cursor.executemany(postgres_insert_query, records)
        connection.commit()
        count = cursor.rowcount
        print(count, "Records inserted successfully into table")

    except (Exception, psycopg2.Error) as error:
        print("Error while inserting records into Postgres table", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


records_to_insert = [ (1, 'Los Angeles', 54),(2, 'Austin', 32),
                      (3, 'Olympia', 98),(4, 'Rochester', 10),
                      (5, 'Salt Lake City', 68),(6, 'Sioux City', 93),]
multiple_insert(records_to_insert)

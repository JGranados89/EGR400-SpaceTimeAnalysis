import psycopg2
from psycopg2 import Error


def delete_data(time_id2):
    try:
        connection = psycopg2.connect(user = "postgres",
                                      password = "wed37dyy2410",
                                      host = "127.0.0.1",
                                      port = "5432",
                                      database = "space_time_app")

        cursor = connection.cursor()

        # View record before deletion
        print("Time records")
        select = """select * from time where id = %s"""
        cursor.execute(select, (time_id2, ))
        record = cursor.fetchone()
        print(record)

        # Deleting the Olympia location

        delete = """Delete from time where id = %s"""
        cursor.execute(delete, (time_id2, ))
        connection.commit()
        count = cursor.rowcount
        print(count, "Record deleted successfully")

    except (Exception, psycopg2.Error) as error:
        print("Error in delete operation", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("Database connection closed successfully")


id = 6
delete_data(id)

import psycopg2


def update_table(time_id1, location):
    try:
        connection = psycopg2.connect(user = "postgres",
                                      password = "wed37dyy2410",
                                      host = "127.0.0.1",
                                      port = "5432",
                                      database = "space_time_app")

        cursor = connection.cursor()

        print("Table before updating record ")
        sql_select_query = """select * from time where id = %s"""
        cursor.execute(sql_select_query, (time_id1, ))
        record = cursor.fetchone()
        print(record)

        # Update record now
        sql_update_query = """Update time set location = %s where id = %s"""
        cursor.execute(sql_update_query, (location, time_id1))
        connection.commit()
        count = cursor.rowcount
        print(count, "Record Updated Successfully")

        print("Table after updating record")
        sql_select_query = """select * from time where id = %s"""
        cursor.execute(sql_select_query, (time_id1,))
        record = cursor.fetchone()
        print(record)

    except (Exception, psycopg2.Error) as error:
        print("Error in update operation", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


id = 5
location = "Minneapolis"
update_table(id, location)
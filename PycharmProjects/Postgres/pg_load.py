import csv
import psycopg2
conn = psycopg2.connect(user="postgres",
                        password="wed37dyy2410",
                        host="127.0.0.1",
                        port="5432",
                        database="space_time_app")
cur = conn.cursor()

create_table_query = '''CREATE TABLE space
           (ID INT PRIMARY KEY     NOT NULL,
           LOCATION        TEXT    NOT NULL,
           LATITUDE     INT     NOT NULL); '''

cur.execute(create_table_query)

print("Table created successfully in space_time_app")

with open('/Users/KyleVanderMeulen/Desktop/space_time.csv', 'r') as f:
    next(f) # Skip the header row.
    cur.copy_from(f, 'space', sep=',')
    conn.commit()
    print("Data successfully imported")



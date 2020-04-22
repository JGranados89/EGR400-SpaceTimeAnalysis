import psycopg2
conn = psycopg2.connect("host=localhost dbname=space_time_app user=postgres")
cur = conn.cursor()
with open('/Users/KyleVanderMeulen/Desktop/EGR400-SpaceTimeAnalysis/usa_covid_cases.csv', 'r') as f:
    # Notice that we don't need the `csv` module.
    next(f)  # Skip the header row.
    cur.copy_from(f, 'covid')

conn.commit()

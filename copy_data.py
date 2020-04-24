import psycopg2
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:wed37dyy2410@localhost/space_time_app', echo=False)

dataframe = pd.read_csv("usa_covid_cases.csv")

conn = psycopg2.connect("host=localhost dbname=space_time_app user=postgres")
cur = conn.cursor()

dataframe.to_sql('covid', con = engine.connect(), if_exists='append', index = False)

engine.execute("SELECT usa_covid_cases.csv * INTO covid")
conn.commit()

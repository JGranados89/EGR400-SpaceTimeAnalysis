import psycopg2
import pandas as pd
from sqlalchemy import create_engine


class Database():

    def __init__(self):
        # self.engine = create_engine('postgresql://postgres:wed37dyy2410@localhost/space_time_app', echo=False)
        self.engine = create_engine('postgresql://postgres:password@localhost/space_time_app', echo=False)
        
        
        self.conn = psycopg2.connect(
            host = "localhost",
            database="space_time_app",
            user="postgres",
            password="password"
        )

        self.cur = self.conn.cursor()    

    def insert_data(self):
        df = pd.read_csv("usa_covid_cases.csv")
        #df = pd.read_csv("../../../EGR400-SpaceTimeAnalysis/usa_covid_cases.csv")

        print(df.head())
        engine = self.engine

        # self.engin.execute('''CREATE TABLE covid()''')
        df.to_sql('covid', con =engine.connect(), if_exists='append', index = False)
        self.engine.execute("SELECT usa_covid_cases.csv * INTO covid")
        self.conn.commit()

    def retrieve_data(self):

        self.engine.execute("SELECT * FROM covid")
        result = self.cur.fetchall()
        print('Printing results from covid database')
        print(result)
        return result

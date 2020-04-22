import pandas as pd
import urllib

url = "https://raw.githubusercontent.com/imdevskp/covid_19_jhu_data_web_scrap_and_cleaning/master/usa_county_wise.csv"
response = urllib.request.urlopen(url)
# print(response)
df = pd.read_csv(url)
# print(df.head())
df.to_csv('usa_covid_cases.csv')
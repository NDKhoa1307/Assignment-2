import sqlite3
import pandas as pd

con = sqlite3.connect("C:/Users/Admin/Downloads/portal_mammals.sqlite") 
df = pd.read_sql_query("SELECT * from surveys", con)

print(df.head())

con.close()
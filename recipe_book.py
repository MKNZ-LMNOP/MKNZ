import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("mssql+pyodbc://@ingrid/recipeDB?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes") #CONNECTION IS SUCCESSFUL

query = """SELECT Title, Cleaned_Ingredients 
            FROM dbo.recipeBook
            WHERE Cleaned_Ingredients 
            LIKE '%%'""" 

df = pd.read_sql(query, engine)

print(df)





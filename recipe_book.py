import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("mssql+pyodbc://@ingrid/recipeDB?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes") #CONNECTION IS SUCCESSFUL

class Recipebook():

    def recipe_check(x):
        x = ''
        query = f"""SELECT Top 5 Title, Cleaned_Ingredients 
                FROM dbo.recipeBook 
                WHERE Cleaned_Ingredients 
                LIKE '%{x}%'
                ORDER BY NEWID()""" 
        df = pd.read_sql(query, engine)
        
        return print(df['Cleaned_Ingredients'])


Recipebook.recipe_check('egg')




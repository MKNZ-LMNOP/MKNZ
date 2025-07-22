import pandas as pd
from sqlalchemy import create_engine, text
from datetime import datetime


engine = create_engine(
        "mssql+pyodbc://@ingrid/recipeDB?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
    )
    

def add_grocery_item():
    # Get user input
    item_name = input("Enter grocery item name: ")
    quantity = input("How much do you have? ")
    purchase_date = datetime.now().strftime('%d-%m-%Y')  # Auto-set today's date
    
    new_item = pd.DataFrame({
        'grocery_item': [item_name],
        'quantity':[quantity],
        'purchase_date': [purchase_date]
    })
    
    # Insert into database
    new_item.to_sql(
        'fridge',
        engine,
        schema='dbo',
        if_exists='append',
        index=False
    )
    
    print(f"Successfully added '{item_name}' to the fridge!")


def remove_grocery_item():
    item_name = input("Enter item name to delete: ")

    with engine.begin() as conn:
        conn.execute(
            text("DELETE FROM dbo.fridge WHERE grocery_item = :item"), 
            {"item": item_name}
        )
        print(f"Deleted {item_name} from fridge")

def list_grocery_items():

    look = pd.read_sql('SELECT * FROM fridge', engine)
    print(look)



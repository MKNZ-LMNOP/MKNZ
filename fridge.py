import pandas as pd
from sqlalchemy import create_engine, text
from datetime import datetime

engine = create_engine(
<<<<<<< HEAD
    "mssql+pyodbc://@ingrid/fridgeDB?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
)
=======
        "mssql+pyodbc://********/recipeDB?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
    )
    
>>>>>>> f26b0abcfdda4098f7f08c6710ba5fe1c0d46a4c

def add_grocery_item(item_name, qty_type, quantity=None):  # Make quantity optional
    date_purchased = datetime.now().strftime('%Y-%m-%d')  # Auto-set today's date
    
    new_item = pd.DataFrame({
        'grocery_item': [item_name],
        'quantity': [quantity],
        'qty_type': [qty_type],
        'date_purchased': [date_purchased]
        

    })
    
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
    look = pd.read_sql('SELECT * FROM dbo.fridge', engine)
    print(look)



list_grocery_items()


import pandas as pd
from datetime import datetime, date
from csv import DictWriter

class Fridge():

    def add_item(n, qty, qty_type, date_purchased=datetime):
        fields = ['name', 'qty', 'qty_type', 'date_purchased']
        new_row = {'name': n, 'qty': qty, 'qty_type': qty_type, 'date_purchased': date.today()}
        with open('stock.csv', 'a', newline='') as f:
            writer = DictWriter(f, fieldnames=fields)
            writer.writerow(new_row)

    def remove_item(x):
        df = pd.read_csv('stock.csv')
        df = df[df['name'] != x]
        df.to_csv('stock.csv', index=False)

    def look_inside():
        return pd.read_csv('stock.csv')
    



Fridge.add_item('brocolo', 300, 'sprigs')

Fridge.remove_item('brocolo')

print(Fridge.look_inside())













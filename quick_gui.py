import tkinter as tk
from fridge import Fridge
from recipe_book import Recipebook

window = tk.Tk()


def search_fridge():
    Fridge.look_inside()

def fridgeVSbook(): 

    pantry = Fridge.look_inside()
    recipes = Recipebook.recipe_check(pantry)

    fridge_ing = tk.Label(window, text="Fridgeratr Ingredients:", font=('Arial', 10))
    ing_list = tk.Label(window, text=f"{pantry}", font=('Arial', 10))
    fridge_ing.pack(pady=5)
    ing_list.pack(pady=5)

    recipe_header = tk.Label(window, text="Possible Recipes:", font=('Arial', 10))
    recipe_list = tk.Label(window, text=f"{recipes}", font=('Arial', 10))
    recipe_header.pack(pady=5)
    recipe_list.pack(pady=5)


def submit_food(): # Submit to the DB
    sub = nfood.get()
    q = qty_.get()
    qt = q_type.get()
    Fridge.add_item(sub, qt, q) 

label = tk.Label(window, text='FRIDGERATR', font='impact, 20')
label.pack()

textboxprompt = tk.Label(window, text="What do you have in your Fridgeratr?", font=('Arial', 10))
textboxprompt.pack(pady=5)

nfood = tk.Entry(window, textvariable='new_food')
qty_ = tk.Entry(window, textvariable='qty')
q_type = tk.Entry(window, textvariable='qtype')
nfood.pack(pady=10)
qty_.pack(pady=10)
q_type.pack(pady=10)




button = tk.Button(window, text="Submit", font=('Arial', 10), command=search_fridge)
button = tk.Button(window, text="Submit", font=('Arial', 10), command=submit_food)
button.pack(pady=10)


button = tk.Button(window, text="What's on the menu?", font=('Arial', 10), command=fridgeVSbook)
button.pack(pady=10)



window.geometry("500x500")
window.title("Fridgeratr")
window.mainloop()
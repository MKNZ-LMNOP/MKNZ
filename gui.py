import tkinter as tk
from fridge import add_grocery_item, remove_grocery_item, list_grocery_items

window = tk.Tk()

def search_fridge():
    add_grocery_item()

window.geometry("500x500")
window.title("Fridgeratr")

label = tk.Label(window, text="Fridgeratr", font=('Arial', 20))
label.pack()

textboxprompt = tk.Label(window, text="What do you have in your Fridgeratr?", font=('Arial', 10))
textboxprompt.pack(pady=5)

entry = tk.Entry(window)
entry.pack(pady=10)

button = tk.Button(window, text="Submit", font=('Arial', 10), command=search_fridge)
button.pack(pady=10)

window.mainloop()
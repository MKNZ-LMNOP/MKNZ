import tkinter as tk
from fridge import Fridge
from recipe_book import Recipebook


class Index(tk.Frame):

    def __init__(self, root):
        self.backgroundcolor = "#6DE2FF"
        self.headercolor = "#FF00FF"

        super().__init__(
            root,
            bg=self.backgroundcolor
            )
        
        self.mainframe = self
        self.mainframe.pack(fill=tk.BOTH, expand=True)
        self.mainframe.columnconfigure(0, weight=0)

        self.container()

    def container(self):

        self.title_container()
        self.body()
        self.input_box()
        self.recipe_box()

    def title_container(self):
        self.title = tk.Frame(
            self.mainframe,
            bg=self.headercolor,
            height=200,
            width=500
        )

        self.title.columnconfigure(0, weight=0)
        self.title.rowconfigure(0, weight=0)
        self.title.grid(column=0, row=0, sticky="EW")
    

    def body(self):
        pass

    def input_box(self):
        pass

    def recipe_box(self):
        pass
    

root = tk.Tk()
root.title('Fridgeratr')
root.geometry("700x500")
startup = Index(root)
root.mainloop()


    








# def fridgeVSbook(): #all the values are there for this one, just gotta slap a skin on it.
#     pantry = Fridge.look_inside()
#     recipes = recipe_check(pantry['name'])

#     fridge_ing = tk.Label(window, text="Fridgeratr Ingredients:", font=('Arial', 10))
#     ing_list = tk.Label(window, text=f"{pantry}", font=('Arial', 10))
#     fridge_ing.grid(pady=5)
#     ing_list.grid(pady=5)
    
#     recipe_header = tk.Label(window, text="Possible Recipes:", font=('Arial', 10))
#     recipe_list = tk.Label(window, text=f"{recipes}", font=('Arial', 10))
#     recipe_header.grid(pady=5)
#     recipe_list.grid(pady=5)


# def submit_food(): # Submit to the DB
#     sub = nfood.get()
#     q = qty_.get()
#     qt = q_type.get()
#     Fridge.add_item(sub, qt, q) 

    
# window.geometry("500x500")
# window.title("Fridgeratr")

# label = tk.Label(window, text="Fridgeratr", font=('Arial', 20))
# label.grid(column=1, row=0)

# textboxprompt = tk.Label(window, text="What do you have in your Fridgeratr?", font=('Arial', 10))
# textboxprompt.grid(pady=5)

# nfood = tk.Entry(window, textvariable='new_food')
# qty_ = tk.Entry(window, textvariable='qty')
# q_type = tk.Entry(window, textvariable='qtype')
# nfood.grid(row=2, column=0, pady=10)
# qty_.grid(row=3, column=1, pady=10)
# q_type.grid(row=4, column=2, pady=10)

# button = tk.Button(window, text="Submit", font=('Arial', 10), command=submit_food)
# button.grid(pady=10)

# button = tk.Button(window, text="What's on the menu?", font=('Arial', 10), command=fridgeVSbook)
# button.grid(pady=10)



# window.mainloop()
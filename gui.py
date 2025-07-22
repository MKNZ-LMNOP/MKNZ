import tkinter as tk

root = tk.Tk()

root.geometry("500x500")
root.title("Fridgeratr")

label = tk.Label(root, text="Fridgeratr", font=('Arial', 20))
label.pack()

entry = tk.Entry(root)
entry.pack(pady=10)

button = tk.Button(root, text="Submit", font=('Arial', 10))
button.pack(pady=10)

root.mainloop()
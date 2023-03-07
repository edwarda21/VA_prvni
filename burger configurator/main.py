import tkinter as tk
import tkinter.ttk as ttk
from lib import *

window = tk.Tk()
window.title("Hello")
window.winfo_height()

elements = []
# TODO: create form GUI
meat_options = ("chicken", "beef", "veal", "pork")
meat_rarity = ("rare", "medium rare", "medium", "well-done")
vegies = ("Tomato", "Salad", "Cucumber", "Onion")
cheese = ("American", "Cheddar")
buns = ("Black", "White")
# frames for different menus
form = tk.Frame(bg="red")
meat_menu = tk.Frame(master=form)
cheese_menu = tk.Frame(master=form)
vegie_menu = tk.Frame(master=form)

name_lbl = ttk.Label(master=form, text="Burger name:")
name_ent = ttk.Entry(master=form)
add_elements(form, buns, "Bun", elements)
print(elements)

add_meat_btn = ttk.Button(master=meat_menu, text="Add meat", command=lambda: add_elements(meat_menu, meat_options,text="", list_of_elements=elements) )
add_meat_btn.pack()
add_elements(meat_menu, meat_options, "Meat", elements)
meat_cooking_cmb = ttk.Combobox(master=form, values=meat_rarity)
add_elements(vegie_menu, vegies, "Vegetables", elements)
add_elements(cheese_menu, cheese, "Cheese", elements)
submit_btn = ttk.Button(master=form, text="Create My Burger", command=create_burger)
meat_menu.pack()
name_lbl.pack()
submit_btn.pack()
cheese_menu.pack()
vegie_menu.pack()
form.pack(fill=tk.BOTH, expand=True)
# TODO: create result GUI
# window mainloop()
window.mainloop()

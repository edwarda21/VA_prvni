import tkinter as tk
import tkinter.ttk as ttk
from lib import *

window = tk.Tk()
window.title("Hello")
window.winfo_height()

elements = {"meat": [], "rarity": [], "vegies": [], "cheese": [], "bun": [], "sauce": [], "name": []}
# TODO: create form GUI
meat_options = ("chicken", "beef", "veal", "pork")
meat_rarity = ("rare", "medium rare", "medium", "well-done")
vegies = ("Tomato", "Salad", "Cucumber", "Onion")
cheese = ("American", "Cheddar")
sauce = ("Ketchup", "Mayonnaise", "Mustard", "Chilli")
buns = ("Black", "White")
# frames for different menus
form = tk.Frame(bg="red")
meat_menu = tk.Frame(master=form)
cheese_menu = tk.Frame(master=form)
vegie_menu = tk.Frame(master=form)
sauce_menu = tk.Frame(master=form)
bun_menu = tk.Frame(master=form)
name_menu = tk.Frame(master=form)

name_lbl = ttk.Label(master=name_menu, text="Burger name:")
name_ent = ttk.Entry(master=name_menu)
elements["name"].append(name_ent)
name_lbl.grid()
name_ent.grid()

add_elements(bun_menu, buns, "Bun", elements["bun"])

add_meat_btn = ttk.Button(master=meat_menu, text="Add meat",
                          command=lambda: [add_elements(meat_menu, meat_options, text="Meat",
                                                        list_of_elements=elements["meat"]),
                                           add_elements(meat_menu, meat_rarity, text="",
                                                        list_of_elements=elements["rarity"])])
add_cheese_btn = ttk.Button(master=cheese_menu, text="Add cheese",
                            command=lambda: add_elements(cheese_menu, cheese, "Cheese", elements["cheese"]))
add_vegies_btn = ttk.Button(master=vegie_menu, text="Add veggies",
                            command=lambda: add_elements(vegie_menu, vegies, "Veggies", elements["vegies"]))
add_meat_btn.grid(row=0, column=0, columnspan=2, sticky="N")
add_cheese_btn.grid(row=0, column=0, columnspan=2, sticky="N")
add_vegies_btn.grid(row=0, column=0, columnspan=2, sticky="N")
add_elements(meat_menu, meat_options, "Meat", elements["meat"])
add_elements(meat_menu, meat_rarity, "", elements["rarity"])
add_elements(vegie_menu, vegies, "Vegetables", elements["vegies"])
add_elements(cheese_menu, cheese, "Cheese", elements["cheese"])
add_elements(sauce_menu, sauce, "Sauce", elements["sauce"])
submit_btn = ttk.Button(master=form, text="Create My Burger", command=lambda:create_burger(elements))

name_menu.grid(padx=10, pady=10, ipadx=5, ipady=5)
bun_menu.grid(padx=10, pady=10, ipadx=5, ipady=5)
meat_menu.grid(padx=10, pady=10, ipadx=5, ipady=5)
cheese_menu.grid(padx=10, pady=10, ipadx=5, ipady=5)
vegie_menu.grid(padx=10, pady=10, ipadx=5, ipady=5)
sauce_menu.grid(padx=10, pady=10, ipadx=5, ipady=5)
submit_btn.grid(padx=10, pady=10, ipadx=5, ipady=5)
form.pack(fill=tk.BOTH, expand=True)
# TODO: create result GUI
# window mainloop()
window.mainloop()

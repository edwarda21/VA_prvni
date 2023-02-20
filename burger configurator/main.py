import tkinter as tk
import tkinter.ttk as ttk

window = tk.Tk()
window.title("Hello")
window.winfo_height()
# TODO: create form GUI
meat_options = ("chicken","beef","veal","pork")
form = tk.Frame(bg="red")
name_lbl = ttk.Label(master=form, text="Burger name:")
name_ent = ttk.Entry(master=form)
meat_lbl = ttk.Label(master=form, text="Meat")
meal_cmb = ttk.Combobox(master=form, values = meat_options)
name_lbl.pack()
name_ent.pack()
meat_lbl.pack()
meal_cmb.pack()
form.pack(fill=tk.BOTH, expand=True)
# TODO: create result GUI
# window mainloop()
window.mainloop()
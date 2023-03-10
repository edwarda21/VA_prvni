import tkinter.ttk as ttk
import tkinter as tk


def create_burger(elements):
    for category in elements:
        for element in category:
            print(element.get())


def add_elements(frame, values, text="", list_of_elements=[]):

    lbl = ttk.Label(master=frame, text=text + f":")
    cmb = ttk.Combobox(master=frame, values=values)
    if text != "":
        lbl.grid(row=frame.grid_size()[1]+1, column=0)
    col = 1
    if len(frame.grid_slaves(frame.grid_size()[1])) == 1:
        col = 2
    cmb.grid(row=frame.grid_size()[1]+1, column= col)
    list_of_elements.append(cmb)
    print(cmb.grid_info())

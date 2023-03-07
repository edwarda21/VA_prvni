import tkinter.ttk as ttk


def create_burger():
    print("Hello")


def add_elements(frame,values, text="", list_of_elements=[]):
    lbl = ttk.Label(master=frame, text=text+f":")
    cmb = ttk.Combobox(master=frame, values=values)
    if text != "":
        lbl.pack()
    cmb.pack()
    list_of_elements.append(cmb)

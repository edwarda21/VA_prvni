import tkinter.ttk as ttk
import tkinter as tk
import PIL as pil
img_paths = {"veal":"veal.png",
             "chicken":"chicken.png",
             "beef":"beef.png",
             "pork":"pork.png",

             }
def create_burger(elements):
    burger_win = tk.Tk()
    burger_win.title(elements["name"][0].get())
    print(elements)
    for category in elements:
        print(category)
        for element in elements[category]:
            print(element.get())
    burger_win.mainloop()



def add_elements(frame, values, text="", list_of_elements=[]):

    lbl = ttk.Label(master=frame, text=text + f":")
    cmb = ttk.Combobox(master=frame, values=values)
    if text != "":
        lbl.grid(row=frame.grid_size()[1]+1, column=0)
    col = 1
    if len(frame.grid_slaves(frame.grid_size()[1])) == 1:
        col = 2
    cmb.current(0)
    cmb.grid(row=frame.grid_size()[1]+1, column= col)
    list_of_elements.append(cmb)
    print(cmb.grid_info())

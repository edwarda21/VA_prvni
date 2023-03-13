import tkinter.ttk as ttk
import tkinter as tk
from PIL import Image, ImageTk
import os
image_root = "./images/"
img_paths = {"veal": "veal.png",
             "chicken": "chicken.png",
             "beef": "beef.png",
             "pork": "pork.png",

             }


def create_burger(elements, burger_frame, main_frame):
    burger_name = ttk.Label(master=burger_frame, text=f"{elements['name'][0].get()}")
    bun_type = elements["bun"][0].get().lower()
    bun_top_img = Image.open(f"{image_root}{bun_type}_top.png")
    bun_bot_img = Image.open(f"{image_root}{bun_type}_bottom.png")
    bun_top_img = ImageTk.PhotoImage(bun_top_img)
    bun_bot_img = ImageTk.PhotoImage(bun_bot_img)
    top_lbl = tk.Label(burger_win,image=bun_top_img)
    bot_lbl = tk.Label(burger_win,image=bun_bot_img)
    top_lbl.pack()
    bot_lbl.pack()

    burger_win.mainloop()


def add_elements(frame, values, text="", list_of_elements=[]):
    lbl = ttk.Label(master=frame, text=text + f":")
    cmb = ttk.Combobox(master=frame, values=values)
    if text != "":
        lbl.grid(row=frame.grid_size()[1] + 1, column=0)
    col = 1
    if len(frame.grid_slaves(frame.grid_size()[1])) == 1:
        col = 2
    cmb.current(0)
    cmb.grid(row=frame.grid_size()[1] + 1, column=col)
    list_of_elements.append(cmb)
    print(cmb.grid_info())

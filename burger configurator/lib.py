import tkinter.ttk as ttk
import tkinter as tk
import PIL as pil
image_root = "images/"
img_paths = {"veal": "veal.png",
             "chicken": "chicken.png",
             "beef": "beef.png",
             "pork": "pork.png",

             }


def create_burger(elements):
    burger_win = tk.Tk()
    burger_win.title(elements["name"][0].get())
    bun_top_img = pil.Image.open(f"{image_root}{elements['bun']}_top.png")
    bun_bot_img = pil.Image.open(f"{image_root}{elements['bun']}_bottom.png")

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

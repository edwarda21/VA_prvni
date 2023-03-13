import tkinter.ttk as ttk
from PIL import Image, ImageTk
import tkinter as tk

image_root = "./images/"


def create_burger(elements, burger_frame, main_frame):
    global images
    categories = ["vegies", "cheese", "sauce", "meat"]
    images = []
    main_frame.pack_forget()
    burger_name = ttk.Label(master=burger_frame, text=f"{elements['name'][0].get()}")
    bun_type = elements["bun"][0].get().lower()
    bun_top_img = Image.open(f"{image_root}{bun_type}_top.png")
    bun_bot_img = Image.open(f"{image_root}{bun_type}_bottom.png")
    bun_top_img = ImageTk.PhotoImage(bun_top_img)
    bun_bot_img = ImageTk.PhotoImage(bun_bot_img)
    top_bun = tk.Label(master=burger_frame, image=bun_top_img)
    top_bun.grid()
    for cat in categories:
        for element in elements[cat]:
            print(f"{image_root}{element.get().lower()}.png")
            img = Image.open(f"{image_root}{element.get().lower()}.png")
            img = ImageTk.PhotoImage(img)
            lbl = tk.Label(master=burger_frame, image=img)
            images.append(img)
            lbl.grid
    bot_lbl = ttk.Label(master=burger_frame, image=bun_bot_img)
    burger_name.grid()
    bot_lbl.grid()
    burger_frame.pack()
    images.append(bun_top_img)
    images.append(bun_bot_img)


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


class Burger:
    def __init__(self, name, elements, b_frame, m_frame):
        self.name = name
        self.images = {}
        self.inputs = elements
        self.order = ["vegies", "cheese", "sauce", "meat"]
        self.frame = b_frame
        self.main_frame = m_frame
        self.get_images()
        self.show_burger()

    def get_images(self):
        for category in self.inputs:
            self.images[category] = []
            for user_input in self.inputs[category]:
                if category == "bun":
                    continue
                try:
                    img = Image.open(f"{image_root}{user_input.get().lower()}.png")
                    img = ImageTk.PhotoImage(img)
                    self.images[category].append(img)
                except FileNotFoundError:
                    continue

    def show_burger(self):
        self.main_frame.pack_forget()
        top_bun = Image.open(f"{image_root}{self.inputs['bun'][0].get()}_top.png")
        bot_bun = Image.open(f"{image_root}{self.inputs['bun'][0].get()}_bottom.png")
        top_bun = ImageTk.PhotoImage(top_bun)
        bot_bun = ImageTk.PhotoImage(bot_bun)
        self.images["bun"] = []
        self.images["bun"].append(top_bun)
        self.images["bun"].append(bot_bun)
        top_lbl = tk.Label(master=self.frame, image=top_bun)
        bot_lbl = tk.Label(master=self.frame, image=bot_bun)
        top_lbl.pack()
        for cat in self.order:
            for i, v in enumerate(self.images[cat]):
                lbl = tk.Label(master=self.frame, image=v)
                lbl.image = v
                lbl.pack()
                print(i)
        bot_lbl.pack()
        self.frame.pack()
        top_lbl.image = top_bun
        bot_lbl.image = bot_bun

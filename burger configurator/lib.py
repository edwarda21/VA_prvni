import tkinter.ttk as ttk
from PIL import Image, ImageTk, ImageEnhance
import tkinter as tk

image_root = "./images/"


def add_elements(frame, values, text="", list_of_elements=[]):
    # creates a new set of combobox and label
    lbl = ttk.Label(master=frame, text=text + f":")
    cmb = ttk.Combobox(master=frame, values=values)
    if text != "":
        lbl.grid(row=frame.grid_size()[1] + 1, column=0)
    col = 1
    if len(frame.grid_slaves(frame.grid_size()[1])) == 1:
        col = 2
    cmb.current(0)
    #shows combobox and label, adds to the list of elements
    cmb.grid(row=frame.grid_size()[1] + 1, column=col)
    list_of_elements.append(cmb)


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

    def __del__(self):
        print("Burger has been deleted")
    def get_images(self):
        # gets all the images necessary for the burger based on the input values, if needed it darkens the meat
        for category in self.inputs:
            self.images[category] = []
            for i,user_input in enumerate(self.inputs[category]):
                darkness = 1
                if category == "bun":
                    continue
                if category == "meat":
                    rarity = self.inputs["rarity"][i].get()
                    if rarity == "medium":
                        darkness = 0.6
                    elif rarity == "well-done":
                        darkness = 0.3
                    else:
                        darkness = 1
                try:
                    # create, darken image and add to list of images
                    img = Image.open(f"{image_root}{user_input.get().lower()}.png")
                    img = ImageEnhance.Brightness(img)
                    img = img.enhance(darkness)
                    img = ImageTk.PhotoImage(img)
                    self.images[category].append(img)
                except FileNotFoundError:
                    continue

    def show_burger(self):
        # draw and show the burger to the window
        self.main_frame.pack_forget()
        name_lbl = ttk.Label(master=self.frame, text=self.inputs["name"][0].get())
        top_bun = Image.open(f"{image_root}{self.inputs['bun'][0].get()}_top.png")
        bot_bun = Image.open(f"{image_root}{self.inputs['bun'][0].get()}_bottom.png")
        top_bun = ImageTk.PhotoImage(top_bun)
        bot_bun = ImageTk.PhotoImage(bot_bun)
        self.images["bun"] = []
        self.images["bun"].append(top_bun)
        self.images["bun"].append(bot_bun)
        top_lbl = tk.Label(master=self.frame, image=top_bun)
        bot_lbl = tk.Label(master=self.frame, image=bot_bun)
        name_lbl.pack()
        top_lbl.pack()
        # shows all the things inside the burger based on the order defined earlier
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
        back_btn = ttk.Button(master=self.frame,command=self.go_back,text="Go Back")
        back_btn.pack()

    def go_back(self):
        # switches back to the form frame and destroys burger instance
        self.frame.pack_forget()
        self.main_frame.pack()
        # runs through all widgets in frame and destroys them
        for widget in self.frame.winfo_children():
            widget.destroy()
        self.__del__()


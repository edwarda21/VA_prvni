from tkinter import *


class Calculator:
    def __init__(self, window):
        self.answer = None
        self.memory = None
        self.window = window
        self.layout = [
            ["AC", "Ans", "**2", "/"],
            ["7", "8", "9", "+"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "*"],
            ["0", ".", "=", "√"]
        ]
        self.main = Frame()

    def build(self):
        # entry box for equation
        entry = Entry(self.window)
        entry.pack()
        # frame for buttons
        btn_frame = Frame(self.window)
        btn_frame.pack()
        # generate buttons based on layout
        for i, btn_row in enumerate(self.layout):
            row = i + 1
            for i, l_btn in enumerate(btn_row):
                column = i + 1
                print(l_btn)
                btn = Button(btn_frame, text=l_btn, command=lambda val=l_btn: self.btn_press(val))
                btn.grid(row=row, column=column)

    def btn_press(self, btn):
        print(btn)

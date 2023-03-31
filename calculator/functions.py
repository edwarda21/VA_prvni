from tkinter import *
from tkinter.ttk import *


def string_difference(string1, string2):
    length = min(len(string1), len(string2))

    difference = ""
    for i in range(length):
        if string1[i] != string2[i]:
            difference += string2[i]
    if len(string1) > len(string2):
        difference += string1[length:]
    else:
        difference += string2[length:]
    return difference


class Calculator:
    def __init__(self, window):
        self.answer = None
        self.memory = None
        self.window = window
        self.layout = [
            ["AC", "Ans", "x²", "/"],
            ["7", "8", "9", "+"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "*"],
            ["0", ".", "=", "√x"]
        ]
        self.operations = {
            "+": "+",
            "-": "-",
            "*": "*",
            "x²": "(x**2)",
            "√x": "(x**(1/2))",
            "/": "/",

        }
        self.actions = [
            "AC",
            "Ans",
            "="
        ]
        self.main = Frame()
        self.entry_b = None
        self.equation = []

    def build(self):
        # entry box for equation
        self.entry_b = Entry(self.window)
        self.entry_b.pack(fill=BOTH)
        # frame for buttons
        btn_frame = Frame(self.window)

        # generate buttons based on layout
        for i, btn_row in enumerate(self.layout):
            row = i + 1
            for i, l_btn in enumerate(btn_row):
                column = i + 1
                btn = Button(btn_frame, text=l_btn, command=lambda val=l_btn: self.btn_press(val))
                btn.grid(row=row, column=column, ipadx=10, ipady=5)
        btn_frame.pack(pady=15)

    def btn_press(self, btn):
        if btn.isdigit():
            self.entry_b.insert(END, btn)
        else:
            self.get_last_expression(btn)


    def get_last_expression(self, value):
        ent_box_eq = self.entry_b.get()
        # get difference between stored equation and entry box equation
        diff = string_difference("".join(self.equation), ent_box_eq)
        print(f"STORED EQUATION: {self.equation}")
        print(f"ENTRY BOX EQUATION: {self.entry_b.get()}")
        print(f"DIFFERENCE:{diff}")
        print(f"TO ADD:{diff+value}")
        if diff != '':
            if "x" in self.operations[value]:
                append = self.operations[value].replace("x", diff,1)
            else:
                append = [diff, value]

            self.entry_b.insert(END, self.operations[value].replace("x", diff,1))
            self.equation += append

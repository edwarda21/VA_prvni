from tkinter import *
from tkinter.ttk import *
import logging

logging.basicConfig(level = logging.DEBUG, format = "%(levelname)s - %(message)s")
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
        self.answer = ""
        self.window = window
        self.layout = [
            ["AC", "Ans", "x²", "/"],
            ["7", "8", "9", "+"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "*"],
            ["0", ".", "=", "√x"]
        ]
        self.operators = {
            "+": "+",
            "-": "-",
            "*": "*",
            "/": "/",

        }
        self.actions = [
            "AC",
            "Ans",
            "="
        ]
        self.functions = {
            "x²": "(x**2)",
            "√x": "(x**(1/2))",
        }
        self.main = Frame()
        self.entry_b = None
        self.equation = []
        self.current_expression = []

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
        # check what the value sent to the function is and use the respective function for it
        if btn.isdigit():
            self.add_number(btn)
        elif btn in self.operators:
            self.add_operator(btn)
        elif btn in self.functions:
            self.use_function(btn)
        elif btn in self.actions:
            if btn == "=":
                self.evaluate()
            elif btn == "AC":
                self.clear_all()
            elif btn == "Ans":
                self.get_answer()
        #self.get_last_expression(btn)

    def evaluate(self):
        logging.info("EVALUATE RUNNING")
        equation = "".join(self.equation+self.current_expression)
        self.answer = eval(equation)
        self.clear_all()
        self.entry_b.insert(0, self.answer)

    def clear_all(self):
        logging.info("CLEAR ALL RUNNING")
        self.entry_b.delete(0, END)
        self.equation = []
        self.current_expression = []

    def add_number(self, number):
        logging.info("ADD NUMBER RUNNING")
        self.current_expression.append(number)
        self.entry_b.insert(END, number)

    def add_operator(self, operator):
        logging.info("ADD OPERATOR RUNNING")
        if len(self.current_expression) > 0:
                self.equation.append([''.join(self.current_expression), operator])
                self.current_expression = []
                self.entry_b.insert(END, operator)

    def use_function(self, function):
        logging.info("USE FUNCTION RUNNING")
        if len(self.current_expression) > 0:
            logging.debug("CURRENT EXPRESSION IS LONGER THAN 0")
            expression = self.functions[function].replace("x", "".join(self.current_expression))
            logging.debug(f"THE CURRENT EXPRESSION AFTER USING THE FUNCTION IS: {expression}")
            # remove the current expression from entry box and replace with new function
            len_to_delete = len("".join(self.current_expression))
            entry_box_text = self.entry_b.get()[:-len_to_delete]
            entry_box_text += "".join(expression)
            # update the entry box text to the new expression
            self.current_expression = [expression]
            self.entry_b.delete(0, END)
            self.entry_b.insert(0, entry_box_text)


    def get_answer(self):
        logging.info("GET MEMORY RUNNING")

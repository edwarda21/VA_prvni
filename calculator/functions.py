from tkinter import *
from tkinter.ttk import *
import logging
import sympy

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s - %(message)s")


class Calculator:
    def __init__(self, window):
        self.answer = ""
        self.window = window
        self.layout = [
            ["AC", "Ans", "x²", "/"],
            ["+/-", "sin", "cos", "tan"],
            ["7", "8", "9", "+"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "*"],
            ["0", ".", "=", "√x"]
        ]
        self.operators = [
            "+",
            "-",
            "*",
            "/",
            "."

        ]
        self.actions = [
            "AC",
            "Ans",
            "="
        ]
        self.functions = {
            "x²": "(x**2)",
            "√x": "(x**(1/2))",
            "+/-": "(-x)",
            "sin": "sin(x)",
            "cos": "cos(x)",
            "tan": "tan(x)"
        }
        self.keyboard_functions_map = {
            "s": "sin",
            "c": "cos",
            "t": "tan",
            "r": "√x",
            "q": "x²",
            "n": "+/-"
        }
        self.keyboard_actions_map = {
            "a": "Ans",
            "=": "=",  # equal sign
            "Return": "=",  # enter key
            "BackSpace": "AC"
        }
        self.keyboard_operators_map = {
            "plus": "+",
            "minus": "-",
            "asterisk": "*",
            "slash": "/",
            "period": "."
        }
        self.main = Frame()
        self.entry_b = None
        self.entry_box_value = StringVar()
        self.equation = []
        self.current_expression = []

    def build(self):
        logging.info("SYMPY VERSION: " + sympy.__version__)
        logging.info("BUILDING CALCULATOR")
        entry_box_height = 0.15
        button_frame_height = 0.85
        # entry box for equation
        self.entry_b = Entry(self.window, state="readonly", font=("Arial", 20), textvariable=self.entry_box_value)
        self.entry_b.place(relwidth=1, relheight=entry_box_height, relx=0, rely=0)
        # frame for buttons
        btn_frame = Frame(self.window)

        # generate buttons based on layout
        for i, btn_row in enumerate(self.layout):
            row = i
            Grid.rowconfigure(btn_frame, row, weight=1)
            for i, l_btn in enumerate(btn_row):
                column = i
                Grid.columnconfigure(btn_frame, column, weight=1)
                btn = Button(btn_frame, text=l_btn, command=lambda val=l_btn: self.btn_press(val))
                btn.grid(row=row, column=column, ipadx=10, ipady=5, sticky="nsew")
        btn_frame.place(relwidth=1, relheight=button_frame_height, relx=0, rely=entry_box_height)
        # set binding functions for keyboard input and font size change
        self.window.bind("<Key>", self.keyboard_input)
        self.entry_b.bind("<Configure>", self.change_font_size)

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

    def evaluate(self):
        logging.info("EVALUATE RUNNING")
        # if the current expression is empty it either means there is nothing to evaluate or the last thing entered was
        # an operator
        if not self.current_expression:
           pass
        else:
            # if the last thing entered was a number then add it to the equation and evaluate it
            equation = "".join(self.equation + self.current_expression)
            answer = sympy.sympify(equation);
            answer = str(answer.evalf()).rstrip('0').rstrip('.')
            self.clear_all()
            self.entry_box_value.set(answer)
            self.current_expression = [answer]
            self.answer = answer

    def clear_all(self):
        # clear the entry box, the equation and the current expression
        logging.info("CLEAR ALL RUNNING")
        self.entry_box_value.set("")
        self.equation = []
        self.current_expression = []

    def add_number(self, number):
        logging.info("ADD NUMBER RUNNING")
        # if the last thing entered was a closing bracket then add a multiplication sign before the number
        if len(self.current_expression) > 0 and "".join(self.current_expression)[-1] == ")":
            self.equation += [''.join(self.current_expression), "*"]
            self.current_expression = []
            self.entry_box_value.set(self.entry_box_value.get() + "*")
        # add the number to the current expression and the entry box
        self.current_expression.append(number)
        self.entry_box_value.set(self.entry_box_value.get() + number)

    def add_operator(self, operator):
        logging.info("ADD OPERATOR RUNNING")
        # if there is a current expression then add it to the equation and clear the current expression
        # then add the operator to the entry box
        if len(self.current_expression) > 0:
            # if the passed operator is a period then check if there is already a period in the current expression
            if operator == "." and self.current_expression[-1] != ")":
                if "." not in "".join(self.current_expression):
                    logging.debug("ADDING COMA")
                    self.entry_box_value.set(self.entry_box_value.get() + operator)
                    self.current_expression.append(operator)
            else:
                self.equation += [''.join(self.current_expression), operator]
                self.current_expression = []
                self.entry_box_value.set(self.entry_box_value.get() + operator)

    def use_function(self, function):
        logging.info("USE FUNCTION RUNNING")
        # if there is a current expression then use the function on it and replace the current expression with the
        # function result
        if len(self.current_expression) > 0:
            expression = self.functions[function].replace("x", "".join(self.current_expression))
            # remove the current expression from entry box and replace with new function
            len_to_delete = len("".join(self.current_expression))
            entry_box_text = self.entry_box_value.get()[:-len_to_delete]
            entry_box_text += "".join(expression)
            # update the entry box text to the new expression
            self.current_expression = [expression]
            self.entry_box_value.set(entry_box_text)

    def get_answer(self):
        # if there is an answer then add it to the entry box and the current expression
        logging.info("GET MEMORY RUNNING")
        if self.answer != "" and self.current_expression == []:
            self.entry_box_value.set(self.entry_box_value.get() + self.answer)
            self.current_expression.append(self.answer)

    def keyboard_input(self, event):
        # check what key was pressed and use the respective function for it
        key = event.keysym
        logging.info(f"KEYBOARD INPUT: {key}")
        if key in self.keyboard_operators_map:
            self.add_operator(self.keyboard_operators_map[key])
        elif key in self.keyboard_functions_map:
            self.use_function(self.keyboard_functions_map[key])
        elif key in self.keyboard_actions_map:
            key = self.keyboard_actions_map[key]
            if key == "=":
                self.evaluate()
            elif key == "AC":
                self.clear_all()
            elif key == "Ans":
                self.get_answer()
        elif key.isdigit():
            self.add_number(key)

    def change_font_size(self, event):
        # dynamically change entry box font size based on window size
        current_height = event.height
        font_size = int(current_height / 3)
        self.entry_b.config(font=("Arial", font_size))
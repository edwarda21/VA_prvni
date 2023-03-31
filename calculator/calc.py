from tkinter import Tk
from functions import *
win = Tk()
win.geometry("500x500")
calc = Calculator(win)
calc.build()

win.mainloop()

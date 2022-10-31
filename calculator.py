import time


class Person:
    def __init__(self):
        self.solved_equations = []

    def solve_equation(self, a, b, operator):
        print(f"{a}{operator}{b}")
        try:
            eval(f"{a}{operator}{b}")
        except:
            print("Something went wrong stop monkeying around >:L")
        else:
            self.solved_equations.append({"equation": f"{a}/{b}", "answer": a / b})
            print(eval(f"{a}{operator}{b}"))

    def interview(self):
        self.name = input("Hello user, What is your name? \n")
        self.surname = input(f"Hello {self.name}, what is your surname? \n")
        while True:
            self.age = input(f"What is ur age, {self.name}? \n")
            if not self.age.isdigit():
                print("Please enter your age in the form of a number")
            else:
                break
        self.fav_food = input(f"What is your favourite food? \n")


person = Person()
person.interview()
print(f"Well hello there {person.name}, nice to meet you")
continues = True
while (continues):
    operators = ["+", "-", "*", "/", "//", "%"]
    while True:
        choice = input("Choose an operator to use +,-,*,/,//,%\n")
        if choice in operators:
            print("yayaya")
            operator = choice
            break
        else:
            print("Please choose a valid operator >:L \n")
    a = float(input("Enter number 1: \n"))
    b = float(input("Enter number 2: \n"))
    person.solve_equation(a, b, operator)
    answered = True
    while True:
        cont = input("Do you want to do another equation? Y / N \n")
        if (cont == "N" or cont == "n"):
            time.sleep(5)
            continues = False

            break
        elif (cont == "Y" or cont == "y"):
            break
        else:
            continue


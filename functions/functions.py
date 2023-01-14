import random
import sys

# define a function using the def keyword
# example: function to calculate the area of a square or rectangle
def calculate_area(a, b=None):
    if b is None:
        return a * a
    return b * a


print(calculate_area(a=8))
fib_len = 100000
fib_memo = {}


def fib(n, memo):
    if 1 == n or n == 0:
        return n
    elif n in memo:
        return memo[n]
    else:
        memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
        return memo[n]


for i in range(fib_len):
    print(fib(i, fib_memo))


# create a function that accepts and infinite amount of number to add up with an addition keyword argument
def add(*number, multiplication=1):
    output = 0
    for i in number:
        output += i
    return output * multiplication


# this allows to add as many numbers as we want, and we can define multiplication by using the keyword
# print(add(1, 2, 3, 4, 5, multiplication=5))

# create rock,paper, scissors (need random library that is imported at the start of file)


def rps():
    user_move = input('''Please select one of the following as your move:
    (R)ock
    (P)aper
    (S)cissors =>''')
    user_move = user_move.lower()[0]
    moves = ["r","p","s"]
    print (user_move)
    computer_move = random.choice(moves)
    if user_move ==  computer_move:
        return f"Draw, the computer also chose {computer_move}"
    elif user_move == "r":
        if (computer_move == "p"):
            return "Sorry you lose the computer chose paper"
        else:
            return "Congratulations you won!"
    elif user_move == "p":
        if computer_move == "s":
            return "Sorry, you lose. The computer chose scissors"
        else:
            return "Congratulations! You won"
    elif user_move == "s":
        if computer_move == "r":
            return "Sorry, you lose. The computer chose rock"
        else:
            return "Congratulation! You won"

# print(rps())

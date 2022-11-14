import time

# YO THIS IS A RANDOM ASS COMMENT
# Favourite
# Favorite
# color
# colour
# aluminium
# aluminum
# sht
x = [9, 98, 2, 657, 357, 61, 6876848, 79, 87, 6543, 69, 789, 79, 79, 16876, 7986, 6579, 7987, 513798, 768435497, 684]


def bubble_sort(list_to_sort):
    lts = list_to_sort.copy()
    while True:
        done = True
        for i in range(len(lts) - 1):
            if lts[i] > lts[i + 1]:
                lts[i], lts[i + 1] = lts[i + 1], lts[i]
                done = False
        if done:
            break
    print(lts)


start = time.process_time_ns()
bubble_sort(x)
end = time.process_time_ns()
total = end - start
print(total)


def quicksort(list_to_sort):
    lts = list_to_sort.copy()
    buffer = lts[0]
    print(buffer)


quicksort(x)
# --------------------
# get user input as integer > 0
# output the area and circumference of square
"""
while True:
    side = input("Please input the side of a square: \n")
    try:
        side = float(side)
    except:
        print("Please input a number")
    else:
        print("The area is", side ** 2)
        print("The circumference is ", side*4)
        break
# --------------------
# multiple line string is created with """ """triple quotes this can also be used for multiline comments
print(type(1))  # <class 'int'>
print(type("a"))  # <class 'str'>

print(isinstance(1, int))  # checks if a value is an instance of certain data type. This would result in True

print(int(9))  # 9
print(int(5.3))  # 5

print(float(8.3))  # 8.3
"""
# ----------------
# get user input as string
# run through string and count number of vowels, symbols, numbers and consonants
vowels = consonants = numbers = symbols = 0
word = input("please input a string:\n =>").lower()
for i in word:
    if i in "aeiou":
        vowels += 1
    elif i in "qzxswdcvfrtgnhyjmklp":
        consonants +=1
    elif isinstance(i, int):
        numbers += 1
    else:
        symbols += 1
        print(i)
print(f"In the string {word} there are {vowels} vowels, {consonants} consonants, {numbers} numbers and {symbols} other symbols")
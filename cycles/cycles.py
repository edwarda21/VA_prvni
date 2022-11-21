def square(side):  # task 1
    for i in range(side):
        print("#"*side)


def empty_square(side):  # task 2
    print("#"*side)
    for i in range(side-2):
        print("#"+" "*(side-2)+"#")
    print("#" * side)


def right_angle_pyramid(height):  # task 3
    for i in range(height):
        print("#"*(i+1))


def pyramid(height):  # task 4
    final_width = 2*height-1
    for i in range(height):
        i+=1
        number_of_hashes = 2*i-1
        number_of_spaces = (final_width-number_of_hashes)//2
        print("."*number_of_spaces+"#"*number_of_hashes+"."*number_of_spaces)


def cross(length):  # task 5
    i = 0
    x = length-2
    if length%2==0: 
        modifier = -1
    else: 
        modifier = 0
    while i < length//2+modifier:
        print(" "*i+"#"+" "*x+"#")
        i+=1
        x -=2
    print(" "*i+"#"+" "*x)
    i-=1
    x+=2
    while -1<i < length:
        print(" "*i+"#"+" "*x+"#")
        i-=1
        x +=2


def diamond(side):  # task 6
    final_width = 2 * side - 1
    for i in range(side):
        i += 1
        number_of_hashes = 2 * i - 1
        number_of_spaces = (final_width - number_of_hashes) // 2
        print("." * number_of_spaces + "#" * number_of_hashes + "." * number_of_spaces)
    for x in range(side-1,0,-1):
        number_of_hashes = 2 * x - 1
        number_of_spaces = (final_width - number_of_hashes) // 2
        print("."*number_of_spaces+"#"*number_of_hashes+ "." * number_of_spaces)


def circle(radius):  # task 7
    pass


def chess_board_fixed(side):  # task 8
    char_dict = {1:"#",-1:"."}
    current_char = 1
    for i in range(side):  # loop through number of rows
        row = ""
        for x in range(side):  # create row
            row += char_dict[current_char]
            current_char *= -1
        print(row)
        current_char *= -1
        
        
def chess_board_resizable(side, space_size):
    char_dict = {1:"#",-1:"."}
    current_char = 1
    for i in range(side):  # loop through number of rows
        row = ""
        for x in range(side):  # create row
            row += char_dict[current_char]*space_size
            current_char *= -1
        print("\n".join([row]*space_size))
        current_char *= -1
        
        
n = 10       
m = 5        

square(n)
print("-"*20)
empty_square(n)
print("-"*20)
right_angle_pyramid(n)
print("-"*20)
pyramid(n)
print("-"*20)
cross(n)
print("-"*20)
diamond(n)
print("-"*20)
chess_board_fixed(n)
print("-"*20)
chess_board_resizable(n,m)
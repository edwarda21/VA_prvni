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
    for i in range(length):
        print()


def diamond(side):
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


def circle(radius):

square(5)
print("-"*20)
empty_square(5)
print("-"*20)
right_angle_pyramid(7)
print("-"*20)
pyramid(11)
print("-"*20)
cross(9)
print("-"*20)
diamond(11)
import math


def check_prime(n: int):
    if n <= 1:
        return False
    for i in range(2, math.ceil(n**(1/2)+1)):
        if n % i == 0:
            return False
    return True


def print_list(input):
    for i in input:
        print(i)

'''
primes_to_thousand = []
for i in range(1001):
    if check_prime(i):
        primes_to_thousand.append(i)
print_list(primes_to_thousand)

'''


# list comprehension

nums = [i for i in range(1001)]
print_list(nums)
primes_to_thousand = [i for i in range(1001) if check_prime(i)]  # saves i for i in the range of 1000 only if check_prime returns true for i

# make a table of multiples
table = []
for i in range(1,10):
    row = [x*i for x in range(1,10)]
    table.append(row)

print_list(table)
print("*"*20)

table_test = [[x*i for x in range(1,10)] for i in range(1,10)]
print_list(table_test)
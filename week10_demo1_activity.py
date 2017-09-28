"""
Write a function that takes an integer and prints the numbers from that down to 0.
"""

def print_down(x):
    for i in range(x, -1, -1):
        print(i)

print_down(10)


def print_down_while(x):
    while x >= 0:
        print(x)
        x -= 1

print_down_while(10)


def print_down_recursion(x):
    print_down_recursion(x) # recursion, function that calls itself


"""
def count_number_to_zero(number):
    for i in range(number,-1,-1):
        print(i)

input_num = int(input("Input number"))
count_number_to_zero(input_num)
"""



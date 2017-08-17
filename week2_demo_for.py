#for i in range(10):
#    print(i)

"""
Define a function that accepts a number and print multiplication according to the number
eg of calling: multiply(5) will print table for number 5
"""

def multiply(num):
    for i in range(11):
        # 0 x 5 = 0
        print("{} * {} = {}".format(i, num, i*num))

def multiply_while(num):
    count = 0
    while count <= 10:
        print("{} x {} = {}".format(count, num, count * num))
        count += 1 #count = count + 1

getNum = int(input("Enter the number:\n"))
#multiply(getNum)
multiply_while(getNum)


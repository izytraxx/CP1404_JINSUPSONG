"""
Write a program that asks the user for their age and then prints whether it is odd or even.
The program should not crash if the user enters a non-number
The program should not allow an invalid age number (reject <0, >120)
Re-prompt until a valid number is entered
"""

# userAge = int(input("Enter your age:\n"))
# while userAge > 120 or userAge < 0:
#     print("Invalid value.")
#     userAge = int(input("Enter your age:\n"))
#
# if userAge%2 == 0:
#     print("Even.")
# elif userAge%2 == 1:
#     print("Odd.")

def get_age(): #function definition
    while True:
        try:
            age = int(input("Enter your age:"))
            if age < 0 or age > 120:
                print("Age out of range.")
            else:
                if age%2 == 0:
                    print("EVEN NUMBER")
                else:
                    print("ODD NUMBER")
                print("Age accepted.")
                break
        except ValueError:
            print("Enter a numeric number.")

get_age() #function calling
get_age()
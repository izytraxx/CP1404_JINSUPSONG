"""
Create a program that asks the user to enter the following inputs:
1. The number of hours user slept last night
2. The budget for getting a coffee
The program will help the user to choose the right size of coffee based on the above inputs.
If you hours of sleep > 8 hrs -> tall cup ($6)
else if between 6 to 8 hours inclusive -> grande cup ($7)
else if < 6 hours verte cup ($7.50)
if ....... :
 ....
elif ..... :
...
else:
....
"""


# if hoursSlept >= 8 :
#     if budgetCoffee < 6 :
#         print("You don't have enough budget to buy a Tall cup $6")
#     else:
#         print("Tall cup $6")
# elif hoursSlept >= 6 and hoursSlept < 8 :
#     if budgetCoffee < 7 :
#         print("You don't have enough budget to buy a Grande cup $7. You can buy a Tall cup $6 instead.")
#     else:
#         print("Grande cup $7")
# else:
#     if budgetCoffee < 7.50 :
#         print("You don't have enough budget to buy a Verte cup $7.50. You can buy a Tall cup $6 or a Grande cup $7 instead.")
#     else:
#         print("Verte cup $7.50")

exit = False

while exit == False:
    hoursSlept = int(input("Enter the hours you slept last night."))
    budgetCoffee = float(input("Enter the budget for getting a coffee."))
    if hoursSlept > 8 and budgetCoffee >= 6:
        print("Let me get you a tall cup of coffee.")
    elif hoursSlept > 6 and budgetCoffee >= 7:
        print("Let me get you a grande cup of coffee.")
    elif hoursSlept < 6 and budgetCoffee >= 7.5:
        print("Let me get you a verte cup of coffee.")
    else:
        print("Sorry, I can't get you a coffee.")
    continue_menu = input("Continue? (Y/N)").upper()
    if continue_menu == "N":
        exit = True
print("Goodbye.")






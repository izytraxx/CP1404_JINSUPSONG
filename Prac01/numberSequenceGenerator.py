x = int(input("Enter X value: "))
y = int(input("Enter Y value: "))
MENU = '1. Show the even numbers from x to y\n2. Show the odd numbers from x to y\n3. Show the squares from x to y\n4. Exit the program'
print(MENU)
userChoice = input(">>> ")
while userChoice != "4":
    if userChoice == "1":
        for i in range(x,y+1):
            if i%2 == 0:
                print(i, end=' ')
    elif userChoice == "2":
        for i in range(x,y+1):
            if i%2 == 1:
                print(i, end=' ')
    elif userChoice == "3":
        for i in range(x,y+1):
            if i**2 >= x and i**2 <= y:
                print(i**2, end=' ')
        if i ** 2 < x or i ** 2 > y:
            print("No squares.")
    print("\n")
    print(MENU)
    userChoice = input(">>> ")
print("Finished")
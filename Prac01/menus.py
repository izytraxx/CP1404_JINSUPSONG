name = str(input("Enter your name: "))
MENU = '(H)ello\n(G)oodbye\n(Q)uit'
print(MENU)
userChoice = str(input(">>> ")).upper()

while userChoice != "Q":
    if userChoice == "H":
        print("Hello " + name)
    elif userChoice == "G":
        print("Goodbye " + name)
    else:
        print("Invalid input!")
    print(MENU)
    userChoice = str(input(">>> ")).upper()
print("Finished.")

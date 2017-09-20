from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    prius = Taxi("Prius", 100)
    limo = SilverServiceTaxi("Limo", 100, 2)
    hummer = SilverServiceTaxi("Hummer", 200, 4)
    taxis = [prius, limo, hummer]
    print("Let's drive!")
    menu_selection = select_menu()
    bill_to_date = 0
    taxi_selection = -1
    while menu_selection != "q":
        if menu_selection == "c":
            taxi_selection = choose_taxi(taxis, bill_to_date)
            menu_selection = select_menu()
        if menu_selection == "d" and taxi_selection == -1:
            print("Choose a taxi")
            menu_selection = select_menu()
        if menu_selection =="d" and taxi_selection != -1:
            bill_to_date = drive_taxi(taxis, taxi_selection, bill_to_date)
            menu_selection = select_menu()
    if menu_selection == "q":
        print("Total trip cost: ${:.2f}".format(bill_to_date))
        print("Taxis are now: ")
        for i in taxis:
            print("{} - {}".format(taxis.index(i), i))


def select_menu():
    valid_menu_choice = ["q", "c", "d"]
    menu_selection = input("q)uit, c)hoose taxi, d)rive\n>>> ").lower()
    while menu_selection not in valid_menu_choice:
        print("Invalid input")
        menu_selection = input("q)uit, c)hoose taxi, d)rive\n>>> ").lower()
    return menu_selection

def choose_taxi(taxis, bill_to_date):
    valid_taxi_selection = []
    for i in taxis:
        print("{} - {}".format(taxis.index(i), i))
        valid_taxi_selection.append(taxis.index(i))
    while True:
        try:
            taxi_selection = int(input("Choose taxi: "))
            while taxi_selection not in valid_taxi_selection:
                print("Invalid input")
                taxi_selection = int(input("Choose taxi: "))
            else:
                print("Bill to date: ${:.2f}".format(bill_to_date))
                #print("Bill to date: ${:.2f}".format(taxis[taxi_selection].get_fare()))
                return taxi_selection
        except ValueError:
            print("Invalid input")


def drive_taxi(taxis, taxi_selection, bill_to_date):
    while True:
        try:
            drive_distance = int(input("Drive how far? "))
            taxis[taxi_selection].drive(drive_distance)
            print("Your {} trip cost you ${:.2f}".format(taxis[taxi_selection].name, taxis[taxi_selection].get_fare()))
            bill_to_date += taxis[taxi_selection].get_fare()
            print("Bill to date: ${:.2f}".format(bill_to_date))
            return bill_to_date
        except ValueError:
            print("Input must be numeric")

main()
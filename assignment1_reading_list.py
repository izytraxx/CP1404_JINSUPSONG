"""
CP1404 Assignment 1 - Reading List 1.0
by JINSUP SONG (JC460494) 
2017/09/01

A program to let users read and write reading list to keep track of books that is completed reading or required to read.
users can see lists of required and completed books and mark a required book as completed when they are finished reading. (but it cannot be done reversely.)
they can also add new books into the reading list by entering books details such as title, author and pages.

GitHub repository
https://github.com/CP1404-JCUS/a1-reading-list-izytraxx

*Pseudocode
read data from books.csv
reformat it and save it into new list
display a main menu
    if user input is NOT "q"
        if user input is "r"
            show list of required books
            if there is no books to display, print "no books" message
        if user input is "c"
            show list of completed books
            if there is no books to display, print "no books" message
        if user input is "a"
            let users enter title, author and pages of the book they want to add
            if users enter an invalid input, display an error message
            if users enter a valid input, add it to the reading list
        if user input is "m"
            show list of required books
            if there is no books to display, print "no required books" message
            let users enter the number of a book they want to mark as completed
            if users enter an invalid input, display an error message
            if users enter a valid input, change the value 'r' to 'c' and overwrite to the reading list
    if user input is "q"
        overwrite the processed reading list data to books.csv
        display a farewell message and quit the program
"""
from operator import itemgetter
DATAFILE = "books.csv"


# Calls out the main selection menu
def main_menu():
    menu_selection = input("Menu:\nR - List required books\nC - List completed books\nA - Add new book\nM - Mark a book as completed\nQ - Quit\n>>> ").upper()
    return menu_selection


# A function to import data from books.csv file
# reads books.csv line by line and store it in to a variable called 'data'
def read_file(DATAFILE):
    in_file = open(DATAFILE, "r")
    data = in_file.readlines()
    in_file.close()
    return data


# A function to export data to books.csv file
# writes the processed result data into books.csv and overwrites existing data
def write_file(DATAFILE, data):
    out_file = open(DATAFILE, "w")
    for each in range(len(data)):
        print("{},{},{},{}".format((data[each])[0], (data[each])[1], (data[each])[2], (data[each])[3]), file=out_file)
    out_file.close()


# A function for reformatting to divide each index values into 4 different categories (title, author, pages, and marking)
# saves reformatted values in a list so it can be 'list-in-list' form
# sorts its value by Author, and then pages using itemgetter
def list_reformatting(data):
    new_list = []
    for each in data:
        each = each.replace("\n", "")
        title = each.split(',')[0]
        author = each.split(',')[1]
        pages = each.split(',')[2]
        marking = each.split(',')[3].lower()
        new_data = [str(title), str(author), int(pages), str(marking)]
        new_list.append(new_data)
    new_list.sort(key=itemgetter(1, 2))
    return new_list


# Calls out the list of required books which is stored in a 'data' list made by read_file() function
# displays only data with the marking value 'r'
# counts the number of books required and sums every pages of those and prints it
# if there is no book to display, print a message that there is no books
def required_books(data):
    print("Required books:")
    book_count = 0
    page_sum = 0
    for i in range(len(data)):
        if (data[i])[3] == "r" or (data[i])[3] == "R":
            book_count += 1
    if book_count == 0:
        print("no books")
    else:
        for i in range(len(data)):
            if (data[i])[3] == "r" or (data[i])[3] == "R":
                page_sum += (data[i])[2]
                print("{}. {:<50s} by {:<20s} {} pages".format(i, (data[i])[0], (data[i])[1], (data[i])[2]))
        print("Total pages for {} books: {}".format(book_count, page_sum))


# Calls out the list of completed books which is stored in a 'data' list made by read_file() function
# displays only data with the marking value 'r'
# counts the number of books completed and sums every pages of those and prints it
# if there is no book to display, print a message that there is no books
def completed_books(data):
    print("Completed books:")
    book_count = 0
    page_sum = 0
    for i in range(len(data)):
        if (data[i])[3] == "c" or (data[i])[3] == "C":
            book_count += 1
    if book_count == 0:
        print("no books")
    else:
        for i in range(len(data)):
            if (data[i])[3] == "c" or (data[i])[3] == "C":
                page_sum += (data[i])[2]
                print("{}. {:<50s} by {:<20s} {} pages".format(i, (data[i])[0], (data[i])[1], (data[i])[2]))
        print("Total pages for {} books: {}".format(book_count, page_sum))


# A function to add books to the data list
# asks an user to input title, author and pages of the book an user wants to add
# displays error messages if the input is invalid
# appends the data an user entered into the 'data' list
def add_books(data):
    add_title = input("Title: ")
    while add_title == "":
        print("Input can not be blank")
        add_title = input("Title: ")
    add_author = input("Author: ")
    while add_author == "":
        print("Input can not be blank")
        add_author = input("Author: ")
    while True:
        try:
            add_pages = int(input("Pages: "))
            while add_pages == "":
                print("Input can not be blank")
                add_pages = int(input("Pages: "))
            if add_pages < 0:
                print("Number must be >= 0")
            print("{} by {}, ({} pages) added to reading list".format(add_title, add_author, add_pages))
            data.append([add_title, add_author, add_pages, "r"])
            break
        except ValueError:
            print("Invalid input; enter a valid number")


# A function to mark required books that user selects as completed
# displays required books list first
# if there is no required books, prints a message that there is no required books
# if an user enters the number that is not on the list, it displays a message that the book is already completed
def mark_books(data):
    book_count = 0
    page_sum = 0
    required_book_list = []
    for i in range(len(data)):
        if (data[i])[3] == "r" or (data[i])[3] == "R":
            book_count += 1
    if book_count == 0:
        print("No required books")
    elif book_count != 0:
        print("Required books:")
        for i in range(len(data)):
            if (data[i])[3] == "r" or (data[i])[3] == "R":
                page_sum += (data[i])[2]
                print("{}. {:<50s} by {:<20s} {} pages".format(i, (data[i])[0], (data[i])[1], (data[i])[2]))
                required_book_list.append(i)
        print("Total pages for {} books: {}".format(book_count, page_sum))
        print("Enter the number of a book to mark as completed")
        while True:
            try:
                mark_book = int(input(">>> "))
                break
            except ValueError:
                print("Invalid input; enter a valid number")
        if mark_book not in required_book_list:
            print("That book is already completed")
        if mark_book in required_book_list:
            print("{} by {} marked as completed".format((data[mark_book])[0], (data[mark_book])[1]))
            (data[mark_book])[3] = (data[mark_book])[3].replace("r", "c")


# A main function of the program
# calls out each function when it is needed
# displays an error message if an user enters an invalid input for menu selection
# displays farewell message, writes the processed data into books.csv and overwrites it when an user quits the program
def main():
    print("Reading List 1.0 - by Jinsup Song")
    data = read_file(DATAFILE)
    data = list_reformatting(data)
    menu_selection = main_menu()
    valid_menu_choice = ["R", "C", "A", "Q", "M"]
    while menu_selection != "Q":
        if menu_selection not in valid_menu_choice:
            print("Invalid menu choice")
        if menu_selection == "R":
            required_books(data)
        elif menu_selection == "C":
            completed_books(data)
        elif menu_selection == "A":
            add_books(data)
        elif menu_selection == "M":
            mark_books(data)
        print("")
        menu_selection = main_menu()
    print("{} books saved to books.csv\nHave a nice day :)".format(len(data)))
    write_file(DATAFILE, data)
main()

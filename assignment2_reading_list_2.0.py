"""
Name: Jinsup Song
Date: 
Brief Project Description:
GitHub URL: https://github.com/CP1404-JCUS/a2-reading-list-izytraxx
"""

from kivy.app import App
from kivy.lang import Builder
from operator import itemgetter
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from book import Book
from booklist import Booklist
import csv

DATAFILE = "books.csv"

# Create your main program in this file, using the ReadingListApp class

class ReadingListApp(App):

    def build(self):
        self.title = "CP1404 Assignment 2 - Reading List 2.0 by JINSUP SONG"
        self.root = Builder.load_file('app.kv')
        self.create_widgets()
        self.root.ids.pages_input.focus = True
        return self.root

    def read_file(self, DATAFILE):
        data = []
        with open(DATAFILE, "r") as file_obj:
            read_line = csv.reader(file_obj)
            for each in read_line:
                #print(each)
                book_obj = Book(each[0], each[1], each[2], each[3])
                data.append(str(book_obj))
                #Booklist(data)
            return data

    def write_file(self, DATAFILE, data):
        for each in range(len(data)):
            print(data[each])
        with open(DATAFILE, "w") as out_file:
            for each in range(len(data)):
                out_file.writelines(data[each]+"\n")

    def create_widgets(self):
        self.data = self.read_file(DATAFILE)
        for each in self.data:
            book_marking = each.split(",")[3].lower()
            book_title = each.split(",")[0]
            if book_marking == "r":
                temp_button = Button(text=book_title, background_color=(1.0, 1.0, 0.0, 1.0))
                #temp_button.bind(on_release=self.required_to_completed)
                self.root.ids.list_label.add_widget(temp_button)
            if book_marking == "c":
                temp_button = Button(text=book_title, background_color=(0.0, 1.0, 1.0, 1.0))
                self.root.ids.list_label.add_widget(temp_button)

    def create_required_books_widgets(self):
        self.data = self.read_file(DATAFILE)
        total_required_pages = 0
        for each in self.data:
            book_marking = each.split(",")[3].lower()
            book_pages = each.split(",")[2]
            book_author = each.split(",")[1]
            book_title = each.split(",")[0]
            if book_marking == "r":
                total_required_pages += int(book_pages)
                temp_button = Button(text=book_title, background_color=(1.0, 1.0, 0.0, 1.0))
                temp_button.bind(on_release=self.required_to_completed)
                self.root.ids.list_label.add_widget(temp_button)
        self.root.ids.label_lower.text = "Click books to mark them as completed"
        self.root.ids.label_upper.text = "Total pages to read: {}".format(total_required_pages)

    def create_completed_books_widgets(self):
        self.data = self.read_file(DATAFILE)
        total_completed_pages = 0
        for each in self.data:
            book_marking = each.split(",")[3].lower()
            book_pages = each.split(",")[2]
            book_author = each.split(",")[1]
            book_title = each.split(",")[0]
            if book_marking == "c":
                total_completed_pages += int(book_pages)
                temp_button = ToggleButton(text=book_title, background_color=(0.0, 1.0, 1.0, 1.0), group='c_books')
                temp_button.bind(on_press=self.completed_books_click)
                self.root.ids.list_label.add_widget(temp_button)
        self.root.ids.label_lower.text = "Click an item to see details"
        self.root.ids.label_upper.text = "Total pages completed: {}".format(total_completed_pages)

    def completed_books_click(self, instance):
        self.data = self.read_file(DATAFILE)
        button_name = instance.text
        if instance.state == 'down':
            for each in self.data:
                book_marking = each.split(",")[3].lower()
                book_pages = each.split(",")[2]
                book_author = each.split(",")[1]
                book_title = each.split(",")[0]
                if book_title == button_name:
                    #book_marking == 'c':
                    self.root.ids.label_lower.text = "{} by {}, {} pages {}".format(book_title, book_author, book_pages,
                                                                                        '(completed)')
                    #elif book_marking == 'r':
                    #    self.root.ids.label_lower.text = "{} by {}, {} pages {}".format(book_title, book_author, book_pages,
                    #                                                                    '(required)')
        else:
            self.root.ids.label_lower.text = "Click an item to see details"

    def required_to_completed(self, instance):
        self.data = self.read_file(DATAFILE)
        button_name = instance.text
        for each in self.data:
            book_marking = each.split(",")[3].lower()
            book_pages = each.split(",")[2]
            book_author = each.split(",")[1]
            book_title = each.split(",")[0]
            if book_title == button_name:
                self.data[self.data.index(each)] = "{},{},{},c".format(book_title, book_author, book_pages)
                self.write_file(DATAFILE, self.data)
        self.clear_all()
        self.create_required_books_widgets()


    def required_button_check(self):
        if self.root.ids.required_books_button.state == 'normal':
            self.clear_all()
            self.create_widgets()
            self.root.ids.label_upper.text = "Reading List"
            self.root.ids.label_lower.text = "Click on the menu on the left"

    def completed_button_check(self):
        if self.root.ids.completed_books_button.state == 'normal':
            self.clear_all()
            self.create_widgets()
            self.root.ids.label_upper.text = "Reading List"
            self.root.ids.label_lower.text = "Click on the menu on the left"

    def clear_text(self):
        self.root.ids.title_input.text = ""
        self.root.ids.author_input.text = ""
        self.root.ids.pages_input.text = ""

    def clear_all(self):
        self.root.ids.list_label.clear_widgets()

    def add_book(self):
        self.data = self.read_file(DATAFILE)
        add_title = self.root.ids.title_input.text
        add_author = self.root.ids.author_input.text
        add_pages = self.root.ids.pages_input.text
        if add_title == "" or add_author == "" or add_pages == "":
            self.root.ids.label_lower.text = "All fields must be completed"
        else:
            while True:
                try:
                    add_book_obj = Book(str(add_title), str(add_author), int(add_pages), 'r')
                    self.data.append(str(add_book_obj))
                    #print(self.data)
                    self.write_file(DATAFILE, self.data)
                    #data = self.data
                    #return data
                    self.clear_text()
                    self.clear_all()
                    self.create_required_books_widgets()
                    self.root.ids.required_books_button.state = 'down'
                    self.root.ids.completed_books_button.state = 'normal'
                    self.root.ids.title_input.focus = ''
                    break
                except ValueError:
                    self.root.ids.pages_input.text = ""
                    self.root.ids.label_lower.text = "Please enter a valid number"
                    self.root.ids.pages_input.on_focus = True
                    break

ReadingListApp().run()

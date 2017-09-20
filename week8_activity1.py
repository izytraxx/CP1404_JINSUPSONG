"""
Create the following classes:
Student - derived from Person,
also has student_id

Musician - derived from Person,
also has play(text)
(Person has a name and an age with an __init__ that defines these.)
"""

class Person:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    def __str__(self):
        return "{} class {} age.".format(self.name, self.age)

    def __add__(self, other):
        return "{} and {}".format(self.name, other.name)

    def __eq__(self, other):
        if self.name == other.name:
            return True
        return False

class Student(Person):
    next_id = 1 #class variable, global variable, all objects shared the same value
    def __init__(self, name="", age=0):
        super().__init__(name, age)
        #self.student_id = student_id
        self.student_id = Student.next_id #instance variable, 1 object 1 value
        Student.next_id += 1
        print("student id = {}".format(self.student_id))

class Musician(Person):
    def play(self, text):
        print("Playing {}".format(text))

stud_a = Student("A", 20)
stud_b = Student("B", 25)
print()
# john = Student("John", 20, 12345)
# mozart = Musician("Mozart", 60)
# print(john)
# print(mozart)
#
# print(type(john))
# print(isinstance(john, Musician))
#
# x = 10 + 5
# print(x)
#
# y = "abc" + "def"
# print(y)
#
# z = john + mozart
# print(z)
#
# print(john == mozart)
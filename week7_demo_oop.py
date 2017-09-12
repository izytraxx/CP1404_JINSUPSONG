"""
Inheritance: A class (subclass) inherits all properties from superclass
"""
class Hero:
    def __init__(self, name="", health=0):
        self.name = name
        self.health = health

    def __str__(self):
        return "I am hero {}, my health is {}".format(self.name, self.health)

class Superman(Hero): #Superman inherits from Hero
    def __str__(self):
        return "I am Superman {}, my health is {}".format(self.name, self.health)

class AnotherClass(Superman):
    def eat(self, food):
        if food == "apple":
            self.health += 20
        elif food == "fried chicken":
            self.health -= 50
        return "Health is now {}".format(self.health)

# hero1 = Hero("Teddy", 100)
# print(hero1)
#
# hero2 = Hero("John", 60)
# print(hero2)
#
# heroes = [hero1, hero2]
# for each in heroes:
#     print(each, end="***")

superman1 = Superman("Super", 100)
print(superman1)

x = AnotherClass("New Hero", 100)
print(x.eat("apple"))

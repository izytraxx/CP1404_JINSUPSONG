"""
Create a Fruit class with appropriate methods.
Fruit class contains another method called isHighCalorie and returns true if the calorie > 100

Next, create another subclass of Fruit that overrides the isHighCalorie to return True for calorie > 80.
This class should be called AsianFruit.
"""
class Fruit:
    __secretVar = 50 #hidden variable that can only be accessed within the same class.

    def __init__(self, name, calorie):
        self.calorie = calorie #instance attribute
        self.name = name

    def isHighCalorie(self):
        if self.calorie > 100:
            return True
        return False

    def __str__(self):
        return "This is fruit {} with calorie {}.".format(self.name, self.calorie)

    def revealSecret(self):
        print(self.__secretVar)

class AsianFruit(Fruit):
    def __init__(self, name, calorie):
        super().__init__(name, calorie) #follow the init() from superclass
        #super().revealSecret()

    def isHighCalorie(self): #overriding, under the condition that name, input, return must be the same as super
        if self.calorie > 80:
            return True
        return False

#Polymorphism
fruits = [Fruit("Rockmelon", 60), AsianFruit("Durian", 100)]


kiwi = Fruit("Kiwi", 30)
print(kiwi)
print(str(kiwi))

fruits.append(kiwi)

print(fruits)
for each in fruits:
    print(each.isHighCalorie()) #polymorphism, dynamic binding

#print(kiwi.__secretVar)
#kiwi.revealSecret()

"""
OOP, two very important relationship 
1. is-a relationship (eg. AsianFruit is a Fruit -> inheritance)
2. has-a relationship (eg. Fruit has calorie -> composition)
"""


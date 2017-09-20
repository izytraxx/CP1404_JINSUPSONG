"""
Create the following classes:
1. Pokemon: that has attributes of name, power (100 as default value). methods attack()
2. Electric: inherits from Pokemon
    - attack(): if attack Electric -> no change in power
                if attack Fire -> Electric increases power by 1
3. Fire: inherits from Pokemon
    - attack(): if attack Fire -> no change in power
                if attack Electric -> Fire decrease power by 1
4. test program that initialise 1 Pikachu (of type Electric), 1 Charmander (of type Fire)
    - randomly generate 10 attacks from any of the character
    - display the final power
"""
import random


class Pokemon:
    def __init__(self, name="", power=100):
        self.name = name
        self.power = power

    def __str__(self):
        return "I am {} power {}".format(self.name, self.power)

    def attack(self, other):
        #isinstance(other, Pokemon) to check the class
        #print(type(self))
        #print(isinstance(self,Pokemon))
        #print("attacking...")
        return self.__str__()

class Electric(Pokemon):
    def attack(self, other):
        if isinstance(other, Fire):
            self.power += 1
        return self.__str__()

    #def __str__(self, name="", power=100):
    #    super().__init__(name, power)

class Fire(Pokemon):
    def attack(self, other):
        if isinstance(other, Electric):
            self.power -= 1
        return self.__str__()

    #def __str__(self, name="", power=100):
    #    super().__init__(name, power)

#Pikachu = Electric(name="Pikachu")
#Charmander = Fire(name="Charmander")
#Pikachu.attack(Charmander)
#print(isinstance(Pikachu, Electric))

characters = []
pikachu = Electric("Pika")
charmander = Fire("Charmander")
characters.append(pikachu)
characters.append(charmander)

for i in range(10):
    rand = random.randrange(0, 2)
    if rand == 0:
        print(characters[0].attack(characters[1]))
    else:
        print(characters[1].attack(characters[0]))
    #print(characters[rand].attack())
#print(random.randrange(0,len(characters)))

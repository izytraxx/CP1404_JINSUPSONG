from taxi import Taxi

prius = Taxi("Prius 1", 100)
prius.drive(40)
print(prius)
print(prius.get_fare())
print(Taxi.get_fare(prius)) #same as prius.get_fare()
prius.start_fare()
prius.drive(100)
print(prius.get_fare())


#taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

#lousy = UnreliableCar("Lousy", 100, 50)
#for i in range(10):
#    lousy.drive(5)
#    print(lousy)
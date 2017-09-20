from car import Car
import random

class UnreliableCar(Car):

    price_per_km = 1.23

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability
        self.current_fare_distance = 0

    def drive(self, distance):
        rand = random.randrange(0,101)
        if rand < self.reliability:
            distance_driven = super().drive(distance)
            self.current_fare_distance += distance_driven
            return distance_driven

    def __str__(self):
        return "{}, {}km on current fare, ${:.2f}/km".format(super().__str__(), self.current_fare_distance, self.price_per_km)



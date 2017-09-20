from taxi import Taxi

class SilverServiceTaxi(Taxi):

    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.current_fare_distance = 0

    def __str__(self):
        return "{}, fuel={}, odometer={}, {}km on current fare, ${:.2f}/km plus flagfall of " \
               "${:.2f}".format(self.name, self.fuel, self.odometer, self.current_fare_distance, (self.fanciness * self.price_per_km), self.flagfall)

    def get_price_per_km(self):
        self.new_price_per_km = self.fanciness * Taxi.price_per_km
        return self.new_price_per_km

    #def drive(self, distance):
    #    distance_driven = super().drive(distance)
    #    self.current_fare_distance += distance_driven
    #    return distance_driven

    def get_fare(self):
        return self.flagfall + ((Taxi.price_per_km * self.fanciness) * self.current_fare_distance)


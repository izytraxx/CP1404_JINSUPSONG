class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self):
        age = 2017 - self.year
        return age

    def is_vintage(self):
        if age >= 50:
            return True
        return False

    def __str__(self):
        return "{} ({}) : ${}".format(self.name, self.year, self.cost)

gibson = Guitar("Gibson L-5 CES", 1992, 16035.40)
another = Guitar("Another Guitar", 2012, 12000)
print(gibson)
print(another)
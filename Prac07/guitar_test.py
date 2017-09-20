from guitar import Guitar

gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
another = Guitar("Another Guitar", 2012, 12000)

print("{} get_age() - Expected 95. Got {}".format(gibson.name, gibson.get_age()))
print("{} get_age() - Expected 5. Got {}".format(another.name, another.get_age()))
print("{} is_vintage() - Expected True. Got {}".format(gibson.name, gibson.is_vintage()))
print("{} is_vintage() - Expected False. Got {}".format(another.name, another.is_vintage()))
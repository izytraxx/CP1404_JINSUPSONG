words = {}
words["avalanche"] = """
An avalanche is a rapid flow of snow down a sloping surface. 
Avalanches are typically triggered in a starting zone from a mechanical failure in 
the snowpack when the forces on the snow exceed its strength but sometimes only with 
gradually widening. """

"""names = ["John", "Amy", "Ann"] 
ages = [20, 40, 30]"""

name_age_dict = {"John":20, "Amy":40, "Ann":30}
name_age_dict["Jack"] = 25
print(name_age_dict)

for each in name_age_dict:
    print("{} -> {}".format(each, name_age_dict[each]))

for key, value in name_age_dict.items():
    print("{:10s}: {:10d}".format(key, value))
string1 = "a, b, + c, d"
#split_data = string1.split(",") #split according to comma
#split_data = string1.split() #split according to space
split_data = string1.split("+")
print(string1)
print(split_data)
print(split_data[1])

#alignment of string format
greet = "How are you"
name = "John"
day = "Monday"
num = 99.8889678
#new_str = "{0:^50s}, {1}?\n Good {2}".format(greet, name, day)
new_str = "{:>50s}, {}?\n Good {}. number is {:.2f}".format(greet, name, day, num)
print(new_str)

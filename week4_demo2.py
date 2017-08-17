list_a = [11, 22]
list_b = [11, 22]
print(list_a == list_b)
print(list_a is list_b)
print(id(list_a))
print(id(list_b))

list_c = list_a
print(list_c is list_a)

num_list = []
for each in range(10):
    num_list.append(each * each)
print(num_list)

#list comprehension
list_comprehension = [each * each for each in range(10)]
print(list_comprehension)

second_comp = [[each*2, each*each] for each in range(10)]
print(second_comp)

def get_values():
    return 11, 22

print(get_values())
ret_tuples = get_values() #(11, 22)
print(ret_tuples[0])
#ret_tuples[0] = 33 cannot do that due to immutable nature

my_str = "abc"
my_list = list(my_str) #convert to list
my_tuple = tuple(my_list) #convert to tuples
print(my_str)
print(my_list)
print(my_tuple)

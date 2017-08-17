name_list = ["John", "Alex", "Kate", "Chris", "Michael"]
age_list = [25, 50, 65, 9, 30]
def get_oldest():
    print(name_list[age_list.index(max(age_list))])
get_oldest()



"""
Write code for a function that takes two lists:
a list of names
a corresponding list of ages
(That is, elements at the same list index represent the same person.)
The function should return the name of the oldest person in the list.
(Return the first name if multiple people have the same oldest age.)
"""

# def get_oldest(name_list, age_list):
#     #get the index number of the oldest age from age_list -> max()
#     #return the name of the same index from name_list
#     pass
#
# names = ["John", "Amy", "Ann"]
# ages = [20, 40, 30]
# print(get_oldest(names,ages)) #print only "Amy"
#
#print(max(ages))
#print(ages.index(max(ages)))
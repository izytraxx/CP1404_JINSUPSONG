"""
Write a function that takes in a number (0 to 6) as input parameter.
And returns the corresponding day of the week. eg 0 as input will get "Sun" as return

Write another function that will return 3 kinds of food randomly by default, or return
the number of meals according to input parameter.
"""
import random

def get_food(num=3): #default value for num is now 3
    foods = ["Sandwich", "Burger", "Fried Chicken", "Udon", "Fried Rice"]
    ret_food = []
    for i in range(num):
        ret_food.append(foods[random.randint(0,len(foods)-1)])
    return ret_food

def get_day(num): #0
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    num = 4
    return days[num] #0

def get_day_v2(num, days):
    days.append("???") #affect days list
    return days[num]

#Sharing immutable -> doesn't affect original value
org_num = 2
print(get_day(org_num))
print(org_num) #????

#Sharing mutable
num_v2 = 3
days_v2 = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
print(get_day_v2(num_v2, days_v2))
print(days_v2) #original value is modified by function and affect subsequent calling

print(get_food())
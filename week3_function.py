"""
Function demo
"""

def get_food_item(food_list):
    food = str(input("Enter the food you have eaten:"))
    food_list.append(food)
    return food

def check_calorie(food):
    if "fried" in food:
        return 200
    elif "steam" in food:
        return 100
    return 50

def check_range(calorie=50): #give a default value in cases where user did not provide one.
    if calorie > 500:
        return "Watch your diet!!!"
    elif calorie > 300:
        return "You are at borderline."
    else:
        return "You are pretty safe."

print(check_range(500))

food_master_list = []
total_calorie = 0
for each in range(3):
    each_food = get_food_item(food_master_list)
    total_calorie += check_calorie(each_food)


print(food_master_list)
print("total calorie = {}\n{}".format(total_calorie, check_range(total_calorie)))
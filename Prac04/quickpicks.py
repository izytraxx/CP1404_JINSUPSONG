"""
import random

quick_picks_generated = int(input("Enter the number of how many quick picks you wish to generate."))
num_list = []
for each in range(quick_picks_generated):
    nums = []
    rand = random.sample(range(1,46),6)
    for each in range(6):
        nums.append(rand[each])
    nums.sort()
    num_list.append(nums)
for each in range(quick_picks_generated):
    print(num_list[each])

"""

import random

num_list = []
user_input = int(input("Enter number of picks:"))

for num in range(user_input):
    nums = [] #small list with 6 nums
    while len(nums) < 6:
        rand = random.randint(1, 46)
        while rand in nums:
            rand = random.randint(1, 46)
        nums.append(rand)
    nums.sort()
    num_list.append(nums)

for each in range(user_input):
    print(num_list[each])

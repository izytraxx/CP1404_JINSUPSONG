"""
with open("data.csv", "r") as my_file:
    for each in my_file:
        print(each)
"""

import csv

file_obj = open("data.csv", "r")
csv_obj = csv.reader(file_obj)
for row in csv_obj:
    print(row)
file_obj.close()

print("*"*100)

"""
counter = 0
with open("data.csv", "r") as file_obj:
    csv_obj = csv.reader(file_obj)
    for row in csv_obj:
        counter += 1
        print("counter = {}".format(counter))
"""

counter = 0
counter_list = []
csv_out = open("out.txt", "w")
csv_wrapper = csv.writer(csv_out) #csv wrapper to ensure data written to csv is comma separated
with open("data.csv", "r") as file_obj:
    csv_obj = csv.reader(file_obj)
    for row in csv_obj:
        counter += 1
        print("counter = {}".format(counter))
        counter_list.append("counter = {}".format(counter))
    print(counter_list)
    csv_wrapper.writerow(counter_list) #goes hand in hand with csv.writer
    #csv_out.writerow(counter_list)
csv_out.close()


"""
file_obj = open("data.csv", "r")
for row in file_obj:
    print(row)
file_obj.close()
"""



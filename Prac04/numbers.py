number_list = []
for each in range(1,6):
    number_input = int(input("Number {}:".format(each)))
    number_list.append(number_input)
print("The first number is {}".format(number_list[0]))
print("The last number is {}".format(number_list[-1]))
print("The smallest number is {}".format(min(number_list)))
print("The largest number is {}".format(max(number_list)))
print("The average of the numbers is {}".format(sum(number_list)/len(number_list)))
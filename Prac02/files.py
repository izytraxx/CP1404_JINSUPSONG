out_file = open("name.txt", 'w')
userName = input("Enter your name.\n")
out_file.write(userName)
out_file.close()

input_file = open("name.txt", 'r')
data = input_file.readline()
print("Your name is {}.\n".format(data))
input_file.close()

input_number = open("numbers.txt", 'r')
numData = input_number.readlines()
print(int(numData[0]) + int(numData[1]))
input_number.close()
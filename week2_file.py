#file writing
"""
string1 = "a, b, c, d"
output_file = open("data.txt", "w")
output_file.write(string1)
output_file.close()
"""

#file reading
input_file = open("data.txt", "r")
data = input_file.readline()
for each in data:
    print(each)
input_file.close()

str_1 = "This is a normal string."
str_2 = """
This 
            is
multiline
string
"""

str_3 = "This comes with escape characters. \nNext\t\tline." #\n for new line, \t for tab space \', \"
#print(str_3)

#print(ord('A')) #65 print the ordinal value associated with the character
#print(ord('a')) #97
#print(chr(65)) #A

#for i in range(32, 101):
#    print("{} -> {}".format(i, chr(i)))
str_4 = "abcdefg"
str_5 = "0123456"
print(str_4[0]) #first character
print(str_4[3])
print(str_4[-3])
print(str_4[0:3]) #abc
print(str_4[0:7:2]) #print alternate characters
print(str_4[-3:-1])
print(str_4[:])
print(str_4[::-1])

"""
Given the string "abcdefghij", write code that will print the following:
1. 'jihgfedcba'
2. 'adgj'
3. 'igeca'
"""

str_abc = "abcdefghij"
print("1. " + str_abc[::-1])
print("2. " + str_abc[::3])
print("3. " + str_abc[-2::-2])

#str_abc[1] = "z" #Not allowed, Immutable, cannot change the string partially
#str_abc = "azghjg" #This is re-assignment

for each in str_abc:
    print(each)

for index, value in enumerate(str_abc):
    if value in "cz":
        print("{} -> {}".format(index, value))

print("W" in str_abc)
print(len(str_abc))

print(str_abc.upper())
print(str_abc.isupper())



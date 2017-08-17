"""
Get into group of 2-5 students and solve the following:
1. Write a function that will read a password from user. (eg. "ab")
2. Write a function that will encode the password and return the encoded word to user.
   (Encoding algorithm: ascii number of encoded word - 65 * 2, separated by ",")
   (eg. "ab" will be encoded to "64,65")
3. Write a function that will print the encoded words to a text file "secret.txt"
4. Control the functions calling in main()
Each group submit the working file to learnjcu "Assessment" -> "Group Project" -> "Week 3 Group Project"
Append the names of all group members on top of the source code, 1 group submit only 1 file.
"""
#print(ord("a"))
#print((ord("a")-65)*2)
OUT_FILE = "secret.txt"
out_file =  open(OUT_FILE, "w")


def getPassword():
    password = str(input("Enter a password:\n"))
    return password

def encode(password):
    encoded_pw = ""
    for each in range(len(password)):
        if each != len(password)-1:
            encoded_pw += str((ord(password[each])-65)*2) + ","
        else:
            encoded_pw += str((ord(password[each])-65)*2)
    return encoded_pw

def print_to_file(encoded):
    print(encoded)
    print(encoded, file=out_file)

def main():
    password = getPassword()
    encoded = encode(password)
    print_to_file(encoded)
main()


out_file.close()

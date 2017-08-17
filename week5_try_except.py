"""
Get 3 inputs from user, each input is separated by comma.
Re-prompt if the user is not entering the right format.
"""
input_flag = True
while input_flag:
    try:
        user_input = input("Enter 3 values separated by comma:")
        datum = user_input.split(",")
        count = 0
        while count <3:
            print(datum[count])
            count += 1
        input_flag = False
    except IndexError: #ValueError, typeError when does it come out???
        print("Data insufficient")



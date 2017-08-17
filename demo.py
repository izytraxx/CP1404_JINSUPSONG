# input_flag = True
# while input_flag:
#     try :
#         userinput = int(input("Enter an integer"))
#         print("Number : {}".format(userinput))
#         input_flag = False
#     except ValueError:
#         print("Value Error")

try:
    x = int("zero")
    print(10/x)
except ZeroDivisionError:
    print("div")
except NameError:
    print("name")
except ValueError:
    print("value")
except:
    print("other")
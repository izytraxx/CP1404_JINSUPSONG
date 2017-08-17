from operator import itemgetter

def get_subject(subject_code:str, subject_name:str) -> str:
    """
    This function formats a string according to input
    :param subject_code: Code associated with subject
    :param subject_name: Name of subject
    :return: 
    """
    string_msg = "This subject {:^10s} is {}.".format(subject_code, subject_name)
    return string_msg

def func(num):
    """
    
    :param num: 
    :return: 
    """


print(get_subject("CP1404", "Programming I"))
print(get_subject.__doc__)
print(get_subject.__annotations__)
print(get_subject.__name__)
print(get_subject.__dict__)

name_list = [["John", 20, "Black"], ["Alice", 25, "Yellow"], ["Amy", 18, "White"]]
name_list.sort()
print(name_list)

name_list.sort(key=itemgetter(1, 2), reverse=True) #sort multi layer
print(name_list)

str_msg = "abcde"
print("-->".join(str_msg)) #string join operator


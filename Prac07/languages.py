from programming_language import ProgrammingLanguage


ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)


language_list = [ruby, visual_basic, python]
print("The dynamically typed languages are:")
for each in language_list:
    if each.typing == "Dynamic" :
        print("{}".format(each.name))

print()




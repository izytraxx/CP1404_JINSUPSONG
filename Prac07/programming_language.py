class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        if self.typing == "Dynamic":
            return True
        else:
            return False

    def __str__(self):
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name, self.typing, self.reflection, self.year)


ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)

language_list = ['ruby', 'visual_basic', 'python']
for each in language_list:
    print(each)


#ruby = ["Ruby", "Dynamic", True, 1995]
#visual_basic = ["Visual Basic", "Static", False, 1991]
#python = ["Python", "Dynamic", True, 1991]

#language_list = []
#language_list.append(ruby)
#language_list.append(visual_basic)
#language_list.append(python)

#print((language_list[0])[0])


#for each in language_list:
#    if each.is_dynamic() == True:
#        print(each)




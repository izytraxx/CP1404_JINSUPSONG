from operator import itemgetter
FILENAME = "speech.txt"

file_obj = open(FILENAME, "r", encoding="utf8")
data = file_obj.read()
word_list = data.split(" ") #["I", "the".....]
word_dict = {} #{I: 50, dropped: 3}

for each in word_list:
    if each not in word_dict: #if it never exists in my dictionary
        word_dict[each] = 1
    else:
        word_dict[each] += 1


sorted_value = sorted(word_dict.items(), key=itemgetter(1), reverse=True)

for key, value in sorted_value:
    print("{} : {}".format(key, value))
print(sorted_value)
file_obj.close()
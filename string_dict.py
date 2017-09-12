from operator import itemgetter

TEXT = "this is a collection of words of nice words this is a fun thing it is"
word_list = TEXT.split(" ")

word_dict = {}
for each in word_list:
    if each not in word_dict:
        word_dict[each] = 1
    else:
        word_dict[each] += 1


sorted_value = sorted(word_dict.items(), key=itemgetter(0))

print("Text: {}".format(TEXT))
for k, v in sorted_value:
    print("{} : {}".format(k, v))
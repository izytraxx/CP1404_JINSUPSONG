"""
Pull Request
1. VCS - Git - Branches
2. Add new things to the branch
3. Commit to repository
4. Create a pull request
5. Review and Comment
6. Merge Pull Request
7. Check out master

Todo:
1. state_names.py
2. color-names.py
3. string_dict.py
"""
length = 50
word1 = "xx"
word2 = 10

print("{:{}}: {}".format(word1, length, word2))

test = {"aaa": 3, "dddddddddddddddddddd": 10}
longest_word = max(test, key=len)
print(longest_word)
longest_size = len(longest_word)
print(longest_size)

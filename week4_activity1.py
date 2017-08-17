"""
Get user name
initialise counter to be 0
Loop through each character in the name
if the character is any of the "aeiou"
Increment a counter
Print out after looping the final string.
"""

username = str(input("Enter your name.").lower())
counter = 0
for each in username:
    if each in "aeiou": #아니면 유저네임의 lower를 지우고 if each in "aeiouAEIOU" 이런식으로 해도 됨
        counter += 1

print("Out of {} letters, {} has {} vowels.".format(len(username), username, counter))

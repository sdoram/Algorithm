import string
word = input()
for alpha in string.ascii_uppercase:
    if alpha not in word:
        print(alpha)
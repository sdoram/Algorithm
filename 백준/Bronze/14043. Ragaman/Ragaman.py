import string
alphabet = list(string.ascii_lowercase)
A = input()
B = input()
check = True
for alpha in alphabet:
    if A.count(alpha) < B.count(alpha):
        check = False

print('A' if check else 'N')    
import sys, string

input = sys.stdin.readline
alphabet = list(string.ascii_lowercase)

while True:
    sentence = input().rstrip()
    if sentence == '*':
        break
    check = True
    for alpha in alphabet:
        if alpha not in sentence:
            check = False
    if check:
        print('Y')
    else:
        print('N')
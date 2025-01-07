import sys, string

input = sys.stdin.readline

alphabet = list(string.ascii_lowercase)

while True:
    sentence = input().rstrip()
    if sentence == '#':
        break
    print(len([1 for alpha in alphabet if alpha in sentence.lower()]))
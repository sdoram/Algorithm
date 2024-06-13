import string
alphabet = list(string.ascii_lowercase)

def pangram(word):
    check = [a for a in alphabet if a not in word]
    return 'pangram' if len(check) == 0 else f'missing {"".join(check)}'

for _ in range(int(input())):
    print(pangram(input().lower()))
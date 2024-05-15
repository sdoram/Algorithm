import sys, string
input = sys.stdin.readline
ALPHABET = list(string.ascii_uppercase+'A')
n = int(input())
for i in range(1,n+1):
    print(f'String #{i} \n{"".join([ALPHABET[ALPHABET.index(x)+1] for x in input().rstrip()])}')
    if i != n:
        print()
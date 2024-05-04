import sys, string
input = sys.stdin.readline
ALPHABET = list(string.ascii_uppercase)
for _ in range(int(input())):
    A, N = input().split('-')
    LICENSE_PLATE = sorted([ALPHABET.index(A[0])*26**2 + ALPHABET.index(A[1])*26 + ALPHABET.index(A[2]), int(N)])
    print('nice' if LICENSE_PLATE[1] - LICENSE_PLATE[0] <= 100 else 'not nice')

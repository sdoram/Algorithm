from sys import stdin

N = int(stdin.readline())
DATA = list(map(int, stdin.readline().split()))
STORAGE = int(stdin.readline())
print(sum([((data - 1) // STORAGE + 1) * STORAGE for data in DATA]))
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    i, x = input().split()
    print(x * int(i))
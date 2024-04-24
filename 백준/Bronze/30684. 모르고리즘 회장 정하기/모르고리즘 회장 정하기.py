import sys
input = sys.stdin.readline
NAME_LIST = [input().rstrip() for _ in range(int(input()))]
PRESIDENT_NAME = sorted([n for n in NAME_LIST if len(n) == 3])[0]
print(PRESIDENT_NAME)
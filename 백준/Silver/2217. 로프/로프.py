import sys

input = sys.stdin.readline
print(max([r*i for i, r in enumerate(sorted([int(input()) for _ in range(int(input()))], reverse=True), start=1)]))
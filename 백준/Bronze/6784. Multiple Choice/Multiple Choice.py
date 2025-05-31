import sys

input = sys.stdin.readline

N = int(input())
print(len([1 for i in [input() for _ in range(N)] if i == input()]))
import sys

input = sys.stdin.readline

N = int(input())
V = int(input())
print('S' if V >= max([int(input()) for _ in range(N-1)]) else 'N')
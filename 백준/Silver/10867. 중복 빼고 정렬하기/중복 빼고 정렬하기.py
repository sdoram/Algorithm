import sys

N = int(input())
N_list = sorted(set(map(int, sys.stdin.readline().split())))
print(*N_list)

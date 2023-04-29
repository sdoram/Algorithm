import sys
N = int(sys.stdin.readline())
N_list = set(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().split()))

answer_list = [1 if m in N_list else 0 for m in M_list]
print(*answer_list)
import sys
N, M = map(int, sys.stdin.readline().split())
N_M1 = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
N_M2 = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
answer = []
for I, N in enumerate(N_M1):
    num_list = []
    for i, n in enumerate(N):
        num = n + N_M2[I][i]
        num_list.append(num)
    answer.append(num_list)
for num in answer:
    print(*num)
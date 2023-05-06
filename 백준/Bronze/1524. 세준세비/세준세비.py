import sys
T = int(input())
for _ in range(T):
    input()
    N, M = map(int, input().split())
    N_power = sorted(
        list(map(int, sys.stdin.readline().lstrip().rstrip().split())))
    M_power = sorted(
        list(map(int, sys.stdin.readline().lstrip().rstrip().split())))
    while N and M:
        if N_power[0] == M_power[0]:
            M_power.pop(0)
            M -= 1
            continue
        if N_power[0] < M_power[0]:
            N_power.pop(0)
            N -= 1
        else:
            M_power.pop(0)
            M -= 1
    print('S' if N != 0 else 'B')

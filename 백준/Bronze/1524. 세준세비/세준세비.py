T = int(input())

for _ in range(T):
    input()
    N, M = map(int, input().split())
    N_power = sorted(list(map(int, input().split())), reverse=True)
    M_power = sorted(list(map(int, input().split())), reverse=True)
    while len(N_power) != 0 and len(M_power) != 0:
        if N_power[-1] == M_power[-1]:
            M_power.pop()
            continue
        N_power.pop() if N_power[-1] < M_power[-1] else M_power.pop()
    print('S' if len(N_power) != 0 else 'B')

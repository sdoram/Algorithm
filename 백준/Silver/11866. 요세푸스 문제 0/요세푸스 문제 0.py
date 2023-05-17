from sys import stdin

N, K = list(map(int, stdin.readline().split()))
N_list = list(range(1, N + 1))
K_list = []
COUNT = 0
while len(K_list) != N:
    for n in N_list[::]:
        COUNT += 1
        if COUNT == K:
            N_list.remove(n)
            K_list.append(n)
            COUNT = 0
print(f"<{(str(K_list))[1:-1]}>")
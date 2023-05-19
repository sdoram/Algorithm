N = int(input())
N_set = set(list(range(1, N + 1)))
COUNT = 0
while len(N_set) != 1:
    for num in sorted(list(N_set)):
        COUNT += 1
        if COUNT % 2 == 1:
            N_set.remove(num)
print(*N_set)
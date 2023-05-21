M, N = map(int, input().split())
num_list = [False] * 2 + [True] * (N)
for num in range(2, int(N**0.5) + 1):
    if num_list[num]:
        for n in range(num + num, N + 1, num):
            num_list[n] = False
print(*[i for i in range(M, N + 1) if num_list[i]], sep="\n")

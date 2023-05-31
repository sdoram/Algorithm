N, M = map(int, input().split())
min_package = 1000
min_single = 1000
for _ in range(M):
    package, single = map(int, input().split())
    min_package = min(min_package, package)
    min_single = min(min_single, single)

I, J = divmod(N, 6)

print(min(N * min_single, (I + 1) * min_package, I * min_package + J * min_single))


N, M = map(int, input().split())
min_package = 1000
min_single = 1000
for _ in range(M):
    package, single = map(int, input().split())
    min_package = min(min_package, package)
    min_single = min(min_single, single)

I, J = divmod(N, 6)
if min_package / 6 > min_single:
    print(N * min_single)
elif min_package < min_single * J:
    print((I + 1) * min_package)
else:
    print(I * min_package + J * min_single)
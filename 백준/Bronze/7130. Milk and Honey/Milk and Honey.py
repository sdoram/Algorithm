total = 0

M, H = map(int, input().split())
for _ in range(int(input())):
    C, B = map(int, input().split())

    total += max(M*C, H*B)
print(total)
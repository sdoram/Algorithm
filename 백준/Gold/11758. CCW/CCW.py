from sys import stdin

P1 = list(map(int, stdin.readline().split()))
P2 = list(map(int, stdin.readline().split()))
P3 = list(map(int, stdin.readline().split()))

V1 = [P2[0] - P1[0], P2[1] - P1[1]]
V2 = [P3[0] - P2[0], P3[1] - P2[1]]
vector_product = (V1[0] * V2[1]) - (V1[1] * V2[0])

if vector_product > 1:
    print(1)
elif vector_product == 0:
    print(0)
elif vector_product < 0:
    print(-1)

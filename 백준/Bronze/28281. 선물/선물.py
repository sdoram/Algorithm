from sys import stdin

A, B = map(int, stdin.readline().split())
price_list = list(map(int, stdin.readline().split()))
print(min([price_list[i] * B + price_list[i + 1] * B for i in range(A - 1)]))

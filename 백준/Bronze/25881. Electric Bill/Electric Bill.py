A, B = map(int, input().split())
for _ in range(int(input())):
    n = int(input())
    if n <= 1000:
        print(n, n * A)
    else:
        print(n, 1000 * A + (n-1000) * B)
import sys
input = sys.stdin.readline
while True:
    try:
        n, k = map(int, input().split())
        c = n
        while c >= k:
            n, c  = n+c//k, c//k + c%k
        print(n)
    except ValueError:
        break
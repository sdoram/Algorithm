import sys 

input = sys.stdin.readline

for _ in range(int(input())):
    input()
    N = list(map(int, input().split()))
    print(min(N), max(N))
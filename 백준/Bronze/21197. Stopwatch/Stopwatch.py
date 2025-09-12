N = int(input())
time = [int(input()) for _ in range(N)]
print('still running' if N % 2 != 0 else sum([-t if i % 2 == 0 else t for i, t in  enumerate(time)]))
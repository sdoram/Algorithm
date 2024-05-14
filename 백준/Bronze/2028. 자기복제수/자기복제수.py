import sys
input = sys.stdin.readline
for _ in range(int(input())):
    N = int(input())
    print('YES' if N**2 % 10**len(str(N)) == N else 'NO')
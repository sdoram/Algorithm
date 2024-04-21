import sys 
input = sys.stdin.readline
S = list(input().rstrip())
for _ in range(int(input())):
    A, B = map(int,input().split())
    S[A] , S[B] = S[B], S[A]
print(*S, sep='')
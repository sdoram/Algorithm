import sys
input = sys.stdin.readline

def escape_school():
    N, M = map(int, input().split())
    patrol = [list(input().rstrip()) for _ in range(N)]
    for m in range(M):
        if [patrol[n][m] for n in range(N)].count('X') == N:
            return m+1
    return 'ESCAPE FAILED'

print(escape_school())
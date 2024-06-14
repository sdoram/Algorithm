import sys
input = sys.stdin.readline

M, N = map(int, input().split())
U, L, R, D = map(int, input().split())
puzzle = [['#' if i % 2 == 0 else '.'for i in range(N+L+R)] if j % 2 == 0 else 
          ['.' if i % 2 == 0 else '#'for i in range(N+L+R)] for j in range(M+U+D)]

for m in range(0, M):
    word = input().rstrip()
    for i, w in enumerate(word, start=0):
        puzzle[U+m][L+i] = w

for p in puzzle:
    print(*p, sep='')
import sys
N = int(sys.stdin.readline())
for i, n in enumerate(range(1, N+1)[::-1]):
    print(' '*i, '*'*(n*2-1), sep='')

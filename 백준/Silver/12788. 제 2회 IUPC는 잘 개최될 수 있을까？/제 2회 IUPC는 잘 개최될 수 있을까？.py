import sys

input = sys.stdin.readline

def IUPC():
    input()
    M, K = map(int, input().split())
    A = sorted(list(map(int, input().split())), reverse=True)
    need_pen = M * K
    for i, a in enumerate(A, start=1):
        need_pen -= a
        if need_pen <= 0:
            return i
    return 'STRESS'

print(IUPC())
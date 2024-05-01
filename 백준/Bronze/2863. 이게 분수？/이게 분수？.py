import sys
input = sys.stdin.readline
A, B = map(int, sys.stdin.readline().split())
C, D = map(int, sys.stdin.readline().split())
NUM_LIST = [A/C + B/D, C/D + A/B, D/B + C/A, B/A + D/C]
print(NUM_LIST.index(max(NUM_LIST)))
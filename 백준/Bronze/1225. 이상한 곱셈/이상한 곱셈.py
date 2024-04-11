import sys
A, B = sys.stdin.readline().split()
print(sum(map(int, A)) * sum(map(int, B)))